#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node

# 导入ROS和RDK的官方消息类型
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from ai_msgs.msg import PerceptionTargets
from sensor_msgs.msg import Image

# 导入自定义消息类型
from test_interface.msg import VideoLogMsg
from test_interface.msg import ObjPosition
from test_interface.msg import ResnetMsg
from test_interface.msg import ObjectMsg

# 导入其他需要的python库
import numpy as np
import time
import math
from io import TextIOWrapper
import threading

from test_carcontrol.code_test_paths import config_path, get_code_test_root

import shapely
from shapely.geometry import Polygon, Point
from operator import attrgetter
from collections import deque
import yaml

# 识别的物体类
class object():
    def __init__(self, obj_type, box):
        if obj_type is not None and box is not None:
            self.obj_type = obj_type        # 物体类别
            self.xL = box.x_offset
            self.yU = box.y_offset
            self.width = box.width
            self.height = box.height

            self.area = self.width * self.height
            self.x = self.xL + int(self.width / 2)
            self.y = self.yU + int(self.height / 2)
            self.xR = self.xL + self.width
            self.yD = self.yU + self.height

            self.rect_area = Polygon([(self.xL, self.yU), (self.xR, self.yU), (self.xR, self.yD), (self.xL, self.yD)])
        else:
            self.obj_type = "None"
            self.xL = -1
            self.yU = -1
            self.width = -1
            self.height = -1

            self.area = -1
            self.x = -1
            self.y = -1
            self.xR = -1
            self.yD = -1
            self.rect_area = Polygon([(0,0), (0,1), (1,1), (1,0)])

# 写log文件
class PIDLogger():
    def __init__(self):
        self.start_time = 0     # 开始自动控制的时间
        self.error = False      # 是否正常打开log文件
        
        # 创建并打开log文件
        root = get_code_test_root()
        log_dir = root / "log" / "new_yolo"
        log_dir.mkdir(parents=True, exist_ok=True)
        str = time.strftime("%m%d_%H%M%S", time.localtime())
        self.log_path = str(log_dir / f"log_{str}.txt")
        self.log_file = open(self.log_path, "a", encoding="utf-8", buffering=1)
        # 如果打开失败，则将错误位置位
        if self.log_file is None:
            print("[Error]: Cannot open log file.")
            self.error = True
            return
        
        # 写log文件开始的内容
        str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_file.write("--------------------| Log Start: new_yolo_d |--------------------\n")
        self.log_file.write(f"Log start at {str1}.\n")

    # 每次自动控制开始时刷新开始时间，并写入自动控制开始
    def refresh_start(self):
        if not self.error:
            self.start_time = time.time()
            self.log_file.write("\n------------| SelfCtrl Start |------------\n")

    # 写log文件内容
    def write_info(self, infostr: str):
        if not self.error:
            t = time.time() - self.start_time
            str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write(f"[{str}][{t:8.4f}][Info]: {infostr}\n")

    # log文件写入障碍物信息
    def write_obj(self, obj:object):
        if not self.error:
            t = time.time() - self.start_time
            str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write(f"[{str}][{t:8.4f}][Info]: [OBJ]: type={obj.obj_type}, x={obj.x}, y={obj.y}.\n")
            self.log_file.write(f"                                xL={obj.xL}, xR={obj.xR}, yU={obj.yU}, yD={obj.yD}.\n")
            self.log_file.write(f"                                width={obj.width}, height={obj.height}, area={obj.area}.\n")

    # 类被销毁时关闭log文件并写入结束语
    def __del__(self):
        if (not self.error) and self.log_file is not None:
            str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write("--------------------| Log End |--------------------\n")
            self.log_file.write(f"Log end at {str1}.\n")
            self.log_file.close()

# 输出为ROS接口信息
def output_obj(obj:object):
    obj_msg = ObjectMsg()
    obj_msg.obj_type = obj.obj_type
    obj_msg.xl = obj.xL
    obj_msg.xr = obj.xR
    obj_msg.yd = obj.yD
    obj_msg.yu = obj.yU
    obj_msg.distance = int(obj.area)
    return obj_msg

class YoloCtrlNode(Node):
    def __init__(self):
        super().__init__("YoloCtrlNode")

        self.YoloV5Subscriber = self.create_subscription(
            PerceptionTargets,
            'hobot_dnn_detection',
            self.YoloV5_listener_callback,
            100)
        self.runsub = self.create_subscription(Int32, '/sign4return', self.sign_callback,
                                               10)  # 订阅控制信息，用于控制是否由此程序控制来自动运行
        self.line_sub = self.create_subscription(ResnetMsg, "/topic_ResnetMsg", self.resnet_callback, 10)

        self.cmd_vel_pub = self.create_publisher(Twist, "/cmd_vel", 5)  # 发布速度与转系那个信息
        self.VideoLog_pub = self.create_publisher(VideoLogMsg, "/topic_VideoLogMsg", 10)

        with open(config_path("config_new_yolo_d.yaml"), "r", encoding="utf-8") as config_file:
            self.params = yaml.safe_load(config_file)
        print(f"New_yolo_d config: {self.params}.")
        self.Kp = self.params["pid"]["Kp"]
        self.Kd = self.params["pid"]["Kd"]
        # self.Ki = self.params["pid"]["Ki"]
        self.speed = self.params["car"]["speed"]
        self.angleRatio = self.params["car"]["angular"]
        self.qrcodeArea = self.params["yolo"]["base_qr_area"]
        self.obsArea = self.params["yolo"]["base_obs_area"]
        self.output_ratio = self.params["pid"]["outputRatio"]

        # self.Kp = 0.8  # 提高比例系数以增加对偏差的反应速度
        # self.Kd = 0.5  # 减少微分系数以避免过冲
        # self.Ki = 0.1  # 引入积分系数以帮助消除稳态误差（如果之前未使用）

        # PID有关参数
        self.Target = self.params["pid"]["Target"]
        self.Error = 0.0
        self.last_err = 0.0
        self.total_err = 0.0
        self.output = 0.0
        self.output_sum = 0.0
        self.twist = Twist()    # 发布的速度信息

        # 当前处于哪个任务，目前没用
        self.task_count = 0

        self.isrunning = 0          # 是否由小车自动控制
        self.isturning = False      # 转向状态标志
        self.turning = 0            # 左转为1，右转为-1，没有转向为0
        self.turningTemp = 0
        self.findqrcode = False     # 是否识别到障碍物
        self.findpark = False       # 是否识别到P点
        self.topark = self.params["yolo"]["to_park"]

        self.obs_list = None        # 存储障碍物信息的列表
        self.max_obs = None         # 当前面积最大的障碍物
        self.max_obs_area = 0       # 最大的障碍物面积
        self.last_max_obs = None    # 上一帧的最大障碍物

        self.qrcode = None          # 存储二维码物体信息
        self.qr_deque = deque(maxlen=5)     # 队列存储连续5帧内的二维码信息
        self.qr_lost = 0            # 无用

        self.park = None            # 存储P点信息
        self.park_deque = deque(maxlen=5)   # 队列存储连续5帧内的p点信息
        self.park_lost = 0

        # 黑线坐标
        self.line_x = 0
        self.line_y = 0
        self.new_line_x = 0

        # 输出日志
        self.logger = PIDLogger()
        # 进程锁
        self.lock = threading.Lock()

        # 小车前行方向区域
        # self.car_front = Polygon([(45,480), (255, 260), (335, 260), (545, 480)])
        self.car_front = Polygon([(35,480), (245, 260), (345, 260), (555, 480)])
        self.isinfront = False
        self.start_detect = False

        self.frame_count = 0

    # 自动控制话题回调
    def sign_callback(self, msg):
        if msg.data == 6:
            self.isrunning = 1
            self.frame_count = 0
            self.task_count += 1

            print(f"[Info]: Receive sign4return: {msg.data}. Self control start. Task count={self.task_count}.")
            # 重置日志开始时间
            self.logger.refresh_start()
            self.logger.write_info("Car Self Control to qrcode Start.")

        elif msg.data == 5:
            self.isturning = False
            self.start_detect = False
            self.turning = 0
            self.output_sum = 0.0

            self.logger.write_info("Car Self Control Over.")
            
            print(f"[Info]: Receive sign4return: {msg.data}. Self control stop.")
            self.isrunning = 0
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.cmd_vel_pub.publish(self.twist)
        
        elif msg.data == 0:
            print(f"[Info]: sign4return: {msg.data}, clear task count.")
            self.task_count = 0

    # resnet话题回调
    def resnet_callback(self, msg):
        self.line_x = msg.line_x
        self.line_y = msg.line_y
        if self.task_count % 2 == 0:
            if self.params["car"]["park_line_mode"] == 1:
                temp = 21/22 * (self.line_y - 480) + 555
                self.new_line_x = self.line_x + 295 - temp
            elif self.params["car"]["park_line_mode"] == -1:
                temp = -21/22 * (self.line_y - 480) + 35
                self.new_line_x = self.line_x + 295 - temp
                # self.new_line_x = self.line_x
            else:
                self.new_line_x = self.line_x
        else:
            if self.params["car"]["qrcode_line_mode"] == 1:
                temp = 21/22 * (self.line_y - 480) + 555
                self.new_line_x = self.line_x + 295 - temp
            elif self.params["car"]["qrcode_line_mode"] == -1:
                temp = -21/22 * (self.line_y - 480) + 35
                self.new_line_x = self.line_x + 295 - temp
                # self.new_line_x = self.line_x
            else:
                self.new_line_x = self.line_x


    # yolo话题回调
    def YoloV5_listener_callback(self, msg: PerceptionTargets):
        result_list = msg.targets
        with self.lock:
            
            # 重置各类信息
            self.findqrcode = False
            self.findpark = False
            self.obs_list = []
            self.qrcode = None
            self.park = None
            self.last_max_obs = self.max_obs
            self.max_obs = None
            self.max_obs_area = 0

            # 将障碍物、二维码、p点存储到对应变量
            for result in result_list:
                if not result.rois:
                    continue
                else:
                    obj = object(result.type, result.rois[0].rect)
                    if obj.obj_type == "qrcode":
                        self.findqrcode = True
                        self.qrcode = obj
                    elif obj.obj_type == "park":
                        self.findpark = True
                        self.park = obj
                    elif obj.obj_type == "obstacle":
                        self.obs_list.append(obj)
                        if obj.area > self.max_obs_area:        # 寻找最大面积的障碍物
                            self.max_obs_area = obj.area
                            self.max_obs = obj
                            self.max_obs_height = obj.height
        
        self.car_control()

    # PID输出
    def car_control(self):
        if self.isrunning:
            self.logger.write_info("--------| Car Control |--------.")
            refer = self.pid_output()   # PID输出并返回参考值

            # 输出速度信息
            if self.start_detect == False:
                self.twist.linear.x = self.speed
            else:
                self.twist.linear.x = self.speed
            self.twist.angular.z = min(self.output / self.angleRatio * self.speed, 3.0 / 4.0 * self.speed)
            self.cmd_vel_pub.publish(self.twist)

            # 将计算得到的信息发布到对应话题
            video_msg = VideoLogMsg()
            video_msg.isturning = self.isturning
            video_msg.refer = float(refer)
            for obj in self.obs_list:
                obj_msg = output_obj(obj)
                video_msg.obj_list.append(obj_msg)
            if self.qrcode is not None:
                obj_msg = output_obj(self.qrcode)
                video_msg.obj_list.append(obj_msg)
            video_msg.linear = self.twist.linear.x
            video_msg.angular = self.twist.angular.z
            self.VideoLog_pub.publish(video_msg)

            if self.frame_count % 15 == 0:
                print(f"[Frame_callback]: Frame_count={self.frame_count}.")
                print(f"                  IsTurning={self.isturning}. Turning={self.turning}.")
                if self.max_obs is not None:
                    print(f"                  Max_obs: x={self.max_obs.x}, y={self.max_obs.y}, area={self.max_obs_area}.")
                print(f"                  PID output: refer={refer}. Angular={self.twist.angular.z}.")
            self.frame_count += 1

    # PID输出
    def pid_output(self):
        refer = self.pid_referAdjust()
        self.Error = self.Target - refer
        # self.total_err += self.Error
        '''
        if not self.isturning:
            if self.turningTemp == 1:
                if self.output_sum > 0:
                    self.output = -self.angleRatio * 1.0
                    self.output_sum -= self.angleRatio * 1.0
                else:
                    self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_err)
            elif self.turningTemp == -1:
                if self.output_sum < 0:
                    self.output = self.angleRatio * 1.0
                    self.output_sum += self.angleRatio * 1.0
                else:
                    self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_err)
        else:
            self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_err)
            self.output_sum += self.output * self.output_ratio
            self.turningTemp = self.turning
        '''
        self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_err)
        self.last_err = self.Error

        self.logger.write_info(f"PID: Refer={refer}, Error={self.Error}.")

        return refer
    
    def pid_referAdjust(self):
        self.logger.write_info(f"Black line: x={self.line_x}, y={self.line_y}.")

        # 如果识别到二维码直接向二维码前进    
        if self.findqrcode and self.qrcode.area > self.qrcodeArea:
            # self.output_sum = 0.0
            self.qr_deque.append(self.qrcode)
            refer = self.qrcode.x
            
            # print(self.qrcode.area)
        # 如果二维码队列中有二维码信息，向最新的一个二维码方向前进
        elif self.qr_deque:     
            refer = self.qr_deque[len(self.qr_deque)-1].x
            self.qr_deque.popleft()
        # 如果均没信息，向黑线前进
        else:
            refer = self.new_line_x

        # if self.findpark and self.park.yD > 400 and self.park.xL < 50:
            # self.topark = True
        if self.topark:
            # 如果识别到P点，向p点前进
            if self.findpark:
                # self.output_sum = 0.0
                self.park_deque.append(self.park)
                refer = self.park.x
            elif self.park_deque:
                refer = self.park_deque[len(self.park_deque)-1].x
                self.park_deque.popleft()

        self.logger.write_info(f"First refer: refer={refer}.")
        self.pid_TurnJudge(refer)

        if self.isturning:
            if self.turning == 1:
                # x_f = 21 / 22 * (self.max_obs.yD - 480) + 545
                x_f = 21 / 22 * (self.max_obs.yD - 480) + 555
                result = self.max_obs.xL - max(100, x_f - 295)
                '''
                if self.isinfront == True:
                    result = self.max_obs.xL - max(100, x_f - 295)
                else:
                    # result = self.max_obs.xL - x_f + 295
                    result = self.max_obs.xL - max(100, x_f - 295)
                '''
                refer = min(refer, result)
            elif self.turning == -1:
                # x_f = -21 / 22 * (self.max_obs.yD - 480) + 45
                x_f = -21 / 22 * (self.max_obs.yD - 480) + 35
                result = self.max_obs.xR + max(100, 295 - x_f)
                '''
                if self.isinfront == True:
                    result = self.max_obs.xR + max(100, 295 - x_f)
                else:
                    # result = self.max_obs.xR + 295 - x_f
                    result = self.max_obs.xR + max(100, 295 - x_f)
                '''
                refer = max(refer, result)
            self.logger.write_info(f"ReferAdjust: turning={self.turning}, xf={x_f}, result={result}.")
            return refer
        else:
            return refer

    def pid_TurnJudge(self, refer):
        # 超过面积阈值，开始转向
        if self.max_obs_area >= self.obsArea and not self.isturning:   # and self.max_obs.rect_area.intersects(self.car_front)
            self.isturning = True
            # self.output_sum = 0.0
            print(f"[Turn]: pid_TurnJudge: isturning={self.isturning}, start turn.")
        
        # 判断左转还是右转
        if self.isturning and self.turning == 0:
            self.logger.write_obj(self.max_obs)
            # 障碍物偏中心位置，通过refer值和障碍物坐标判断
            if shapely.contains(self.car_front, Point(self.max_obs.x, self.max_obs.yD)):
                if refer <= self.max_obs.x:
                    self.turning = 1
                else:
                    self.turning = -1
                self.isinfront = True
            # 障碍物不在中心，直接看障碍物位于视野的位置
            else:
                if self.max_obs.x >= 295:
                    self.turning = 1
                else:
                    self.turning = -1
                self.isinfront = False
            print(f"[Turn]: pid_TurnJudge: turning={self.turning}.")
        elif self.isturning:
            if self.IoUJudge() or self.max_obs_area <= self.obsArea:       # 判断是否已经越过当前障碍物
                self.isturning = False
                self.turning = 0
                print(f"[Turn]: pid_TurnJudge: isturning={self.isturning}, stop turn.")
        elif not self.isturning:
            self.turning = 0
    
    # 计算这一帧与上一帧最大障碍物的IoU，判断是否为同一障碍物，若为同一障碍物返回False
    def IoUJudge(self):
        if self.last_max_obs is None or self.max_obs is None:
            return True
        if self.max_obs.rect_area.intersects(self.last_max_obs.rect_area):
            inter_area = self.max_obs.rect_area.intersection(self.last_max_obs.rect_area).area
        else:
            return True

        union_area = self.max_obs.rect_area.area + self.last_max_obs.rect_area.area - inter_area

        if inter_area / union_area <= 0.3:
            return True
        else:
            return False

def main(args=None):
    rclpy.init(args=args)
    car_controller = YoloCtrlNode()
    rclpy.spin(car_controller)
    car_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()