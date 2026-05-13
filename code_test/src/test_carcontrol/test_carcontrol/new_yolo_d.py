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
import os
import numpy as np
import time
import math
from io import TextIOWrapper
import threading
import time

import shapely
from shapely.geometry import Polygon, Point
from operator import attrgetter
from collections import deque
import yaml

from test_carcontrol.code_test_paths import config_path, get_code_test_root
from test_carcontrol.ros_qos import CMD_VEL_QOS, SIGN4RETURN_QOS

# 使用一个类存储物体的信息
class object():
    def __init__(self, obj_type, box):
        if obj_type is not None and box is not None:        # 确保消息和物体类别不为空
            self.obj_type = obj_type        # 物体类别
            self.xL = box.x_offset          # 矩形框左上角顶点x坐标
            self.yU = box.y_offset          # 矩形框左上角顶点y坐标
            self.width = box.width          # 矩形框的宽
            self.height = box.height        # 矩形框的高

            self.area = self.width * self.height            # 矩形框面积
            self.x = self.xL + int(self.width / 2)          # 矩形框中心x坐标
            self.y = self.yU + int(self.height / 2)         # 矩形框中心y坐标
            self.xR = self.xL + self.width                  # 矩形框右下角顶点x坐标
            self.yD = self.yU + self.height                 # 矩形框右下角顶点y坐标

            # 使用Polygon类存储矩形框
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
        log_dir = root / "log" / "new_yolo_d"
        log_dir.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%m%d_%H%M%S", time.localtime())        # 当前的月日、时分秒格式化输出为字符串
        self.log_path = os.fspath(log_dir / f"log_{stamp}.txt")
        self.log_file = open(self.log_path, "a", encoding="utf-8", buffering=1)     # 打开log文件
        # 如果打开失败，则将错误位置位
        if self.log_file is None:
            print("[Error]: Cannot open log file.")
            self.error = True
            return
        
        # 写log文件最开头的内容
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
            ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write(f"[{ts}][{t:8.4f}][Info]: {infostr}\n")

    # log文件写入障碍物信息
    def write_obj(self, obj:object):
        if not self.error:
            t = time.time() - self.start_time
            ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write(f"[{ts}][{t:8.4f}][Info]: [OBJ]: type={obj.obj_type}, x={obj.x}, y={obj.y}.\n")
            self.log_file.write(f"                                xL={obj.xL}, xR={obj.xR}, yU={obj.yU}, yD={obj.yD}.\n")
            self.log_file.write(f"                                width={obj.width}, height={obj.height}, area={obj.area}.\n")

    # 类被销毁时关闭log文件并写入结束语
    def __del__(self):
        if (not self.error) and self.log_file is not None:
            str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write("--------------------| Log End |--------------------\n")
            self.log_file.write(f"Log end at {str1}.\n")
            self.log_file.close()

# 根据物体的类的信息，输出为ROS接口信息
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
            100)        # 订阅Yolo识别结果话题
        self.runsub = self.create_subscription(
            Int32,
            '/sign4return',
            self.sign_callback,
            SIGN4RETURN_QOS,
        )  # 订阅控制信息，用于控制是否由此程序控制来自动运行
        # 订阅Resnet识别的注意点
        self.line_sub = self.create_subscription(ResnetMsg, "/topic_ResnetMsg", self.resnet_callback, 10)

        # 发布速度话题
        self.cmd_vel_pub = self.create_publisher(Twist, "/cmd_vel", CMD_VEL_QOS)
        # 发布视频调试话题
        self.VideoLog_pub = self.create_publisher(VideoLogMsg, "/topic_VideoLogMsg", 10)

        # 打开配置文件
        with open(config_path("config_new_yolo_d.yaml"), "r", encoding="utf-8") as config_file:
            self.params = yaml.safe_load(config_file)
        print(f"New_yolo_d config: {self.params}.")

        # 根据配置文件内容读取对应的参数
        self.Kp = self.params["pid"]["Kp"]          # PID参数Kp
        self.Kd = self.params["pid"]["Kd"]          # PID参数Kd
        # self.Ki = self.params["pid"]["Ki"]
        self.speed = self.params["car"]["speed"]        # 线速度
        self.angleRatio = self.params["car"]["angular"]     # 角速度的一个比例值，用于根据PID输出计算角速度
        self.qrcodeArea = self.params["yolo"]["base_qr_area"]       # 二维码阈值，Yolo识别到二维码后超过多少面积向二维码前进
        self.obsArea = self.params["yolo"]["base_obs_area"]         # 进入避障状态的障碍物面积阈值
        self.output_ratio = self.params["pid"]["outputRatio"]       # 试验性参数，目前已经被弃用

        # self.Kp = 0.8  # 提高比例系数以增加对偏差的反应速度
        # self.Kd = 0.5  # 减少微分系数以避免过冲
        # self.Ki = 0.1  # 引入积分系数以帮助消除稳态误差（如果之前未使用）

        # PID有关参数
        self.Target = self.params["pid"]["Target"]      # 小车行进中心线在摄像头画面上的x坐标
        self.Error = 0.0                # 误差
        self.last_err = 0.0             # 上一帧的误差
        self.total_err = 0.0            # 总误差，使用Ki参数时需要，目前没用
        self.output = 0.0               # PID输出
        self.output_sum = 0.0           # 试验性参数，目前已经被弃用
        self.twist = Twist()    # 发布的速度信息

        # 当前处于哪个任务，偶数为回到P点，奇数为前往二维码
        self.task_count = 0

        self.isrunning = 0          # 是否由小车自动控制
        self.isturning = False      # 转向状态标志
        self.turning = 0            # 左转为1，右转为-1，没有转向为0
        self.turningTemp = 0        # 试验性参数，目前已被弃用
        self.findqrcode = False     # 是否识别到障碍物
        self.findpark = False       # 是否识别到P点
        self.topark = self.params["yolo"]["to_park"]    # 是否启用向P点行进，不启用的话，小车回到P点将只根据黑线行进。

        self.obs_list = None        # 存储障碍物信息的列表
        self.max_obs = None         # 当前面积最大的障碍物
        self.max_obs_area = 0       # 最大的障碍物面积
        self.last_max_obs = None    # 上一帧的最大障碍物

        self.qrcode = None          # 存储二维码物体信息
        self.qr_deque = deque(maxlen=5)     # 队列存储连续5帧内的二维码信息
        self.qr_lost = 0            # 用于计算二维码丢失的帧数，无用

        self.park = None            # 存储P点信息
        self.park_deque = deque(maxlen=5)   # 队列存储连续5帧内的p点信息
        self.park_lost = 0          # 用于计算P点丢失的帧数，无用

        # 黑线坐标
        self.line_x = 0
        self.line_y = 0
        self.new_line_x = 0     # 用于不同行进策略（车中心沿黑线、车左右侧沿黑线）的x坐标转化

        # 输出日志
        self.logger = PIDLogger()
        # 进程锁
        self.lock = threading.Lock()

        # 小车前行方向区域
        # self.car_front = Polygon([(45,480), (255, 260), (335, 260), (545, 480)])
        self.car_front = Polygon([(35,480), (245, 260), (345, 260), (555, 480)])
        self.isinfront = False          # 记录障碍物是否在小车行进方向偏中心的位置，没有具体用处
        # 不是我加个这个参数，加参数的人也忘了这是干什么用的，应该是用于在检测到二维码时改变行进的线速度，目前没用
        self.start_detect = False

        self.frame_count = 0            # 帧计数

    # 自动控制话题回调
    def sign_callback(self, msg):
        # 上位机发送6，开始自动控制
        if msg.data == 6:
            self.isrunning = 1          # 置位自动控制标志
            self.frame_count = 0        # 重置帧计数
            self.task_count += 1        # 任务计数+1

            print(f"[Info]: Receive sign4return: {msg.data}. Self control start. Task count={self.task_count}.")
            # 重置日志开始时间
            self.logger.refresh_start()
            self.logger.write_info("Car Self Control to qrcode Start.")
        # 上位机发送5，停止自动控制
        elif msg.data == 5:
            self.isturning = False          # 转向标志清零
            self.start_detect = False       
            self.turning = 0                # 转向方向重置
            self.output_sum = 0.0


            self.logger.write_info("Car Self Control Over.")
            
            print(f"[Info]: Receive sign4return: {msg.data}. Self control stop.")
            self.isrunning = 0              # 清零自动控制标志
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.cmd_vel_pub.publish(self.twist)        # 发布速度话题，停下小车
        # 重置任务计数
        elif msg.data == 0:
            print(f"[Info]: sign4return: {msg.data}, clear task count.")
            self.task_count = 0

    # resnet话题回调
    def resnet_callback(self, msg):
        self.line_x = msg.line_x
        self.line_y = msg.line_y        # 存储话题发布的数据
        if self.task_count % 2 == 0:    # 任务计数为偶数，是任务三-回到P点
            if self.params["car"]["park_line_mode"] == 1:       # 小车右侧沿着黑线走
                temp = 21/22 * (self.line_y - 480) + 555
                self.new_line_x = self.line_x + 295 - temp
            elif self.params["car"]["park_line_mode"] == -1:    # 小车左侧沿着黑线走
                temp = -21/22 * (self.line_y - 480) + 35
                self.new_line_x = self.line_x + min(295 - temp,150)
                # self.new_line_x = self.line_x
            else:
                self.new_line_x = self.line_x                   # 小车中心线沿着黑线走
        else:                           # 任务计数为奇数，是任务一-前往二维码
            if self.params["car"]["qrcode_line_mode"] == 1:     # 小车右侧沿着黑线走
                temp = 21/22 * (self.line_y - 480) + 555
                self.new_line_x = self.line_x + 295 - temp
            elif self.params["car"]["qrcode_line_mode"] == -1:  # 小车左侧沿着黑线走
                temp = -21/22 * (self.line_y - 480) + 35
                self.new_line_x = self.line_x + min(295 - temp,150)
                # self.new_line_x = self.line_x
            else:
                self.new_line_x = self.line_x                   # 小车中心线沿着黑线走

    # yolo话题回调
    def YoloV5_listener_callback(self, msg: PerceptionTargets):
        result_list = msg.targets       # 取消息信息中的targets集合
        """
        下面的代码使用了进程锁。ROS是并行执行的，因此需要避免其他进程对障碍物列表的修改。
        当然，在我们的代码中应该不会出现这种情况，没有别的函数会修改障碍物列表。
        这里最初是参考别人的代码，进程锁也是那个时候知道的，最后就保留了。
        """
        with self.lock:                 
            
            # 重置各类信息
            self.findqrcode = False         # 是否识别到二维码
            self.findpark = False           # 是否识别到P点
            self.obs_list = []              # 障碍物列表
            self.qrcode = None              # 存储二维码的物体类
            self.park = None                # 存储P点的物体类
            self.last_max_obs = self.max_obs        # 上一帧里的最大面积的障碍物
            self.max_obs = None             # 面积最大的障碍物
            self.max_obs_area = 0           # 最大的障碍物面积

            # 将障碍物、二维码、p点存储到对应变量
            for result in result_list:      # 对targets集合里的所有成员
                if not result.rois:         # 不存在矩形框
                    continue
                else:
                    obj = object(result.type, result.rois[0].rect)      # 将物体的信息用类存储
                    if obj.obj_type == "qrcode":            # 物体是二维码
                        self.findqrcode = True
                        self.qrcode = obj
                    elif obj.obj_type == "park":            # 物体是P点
                        self.findpark = True
                        self.park = obj
                    elif obj.obj_type == "obstacle":        # 物体是障碍物
                        self.obs_list.append(obj)           # 将物体加入列表
                        if obj.area > self.max_obs_area:        # 寻找最大面积的障碍物
                            self.max_obs_area = obj.area
                            self.max_obs = obj
                            self.max_obs_height = obj.height    # 之前在改进代码时尝试使用过高度而非面积，后面被弃用了，这行代码没用
        
        self.car_control()      # 进入PID输出和速度话题发布

    # PID输出
    def car_control(self):
        if self.isrunning:
            self.logger.write_info("--------| Car Control |--------.")
            refer = self.pid_output()   # PID输出并返回参考值

            # 输出速度话题
            if self.start_detect == False:
                self.twist.linear.x = self.speed
            else:
                self.twist.linear.x = self.speed        # 输出小车的线速度
            # 输出小车的角速度
            self.twist.angular.z = min(self.output / self.angleRatio * self.speed, 3.0 / 4.0 * self.speed)
            self.cmd_vel_pub.publish(self.twist)        # 将速度发布到对应话题，从而让小车按照计划行驶

            """
            为了方便调车，这里写了一个自定义的消息类型，用于将计算速度过程中的一些重要信息通过话题的方式传出去。
            然后在另一个节点接收这个话题发布的信息，那个节点会同时接收摄像头的画面，将这些信息嵌入画面中。
            最终形成一个视频输出，可以让我们清晰地看到小车在跑车过程中的情况。
            """
            video_msg = VideoLogMsg()
            video_msg.isturning = self.isturning        # 是否在自动控制
            video_msg.refer = float(refer)              # 参考值
            for obj in self.obs_list:                   # 物体的矩形框
                obj_msg = output_obj(obj)
                video_msg.obj_list.append(obj_msg)
            if self.qrcode is not None:                 # 二维码，这个视频输出是在P点搞出来之前弄得，所以没写P点的部分
                obj_msg = output_obj(self.qrcode)
                video_msg.obj_list.append(obj_msg)
            video_msg.linear = self.twist.linear.x      # 输出的线速度
            video_msg.angular = self.twist.angular.z    # 输出的角速度
            self.VideoLog_pub.publish(video_msg)        # 将信息发布到对应话题

            # 每隔固定数量的帧，在终端中打印信息，这样在减少终端被刷屏的同时也可以通过终端查看程序运行状况
            if self.frame_count % 15 == 0:      # 每隔15帧输出一次，Yolo识别大概是30帧左右，这里也就差不多半秒输出一次
                print(f"[Frame_callback]: Frame_count={self.frame_count}.")     # 打印帧计数
                print(f"                  IsTurning={self.isturning}. Turning={self.turning}.")     # 打印避障信息
                if self.max_obs is not None:        # 打印面积最大的障碍物
                    print(f"                  Max_obs: x={self.max_obs.x}, y={self.max_obs.y}, area={self.max_obs_area}.")
                print(f"                  PID output: refer={refer}. Angular={self.twist.angular.z}.")      # 打印参考值
            self.frame_count += 1

    # PID输出
    def pid_output(self):
        refer = self.pid_referAdjust()      # 计算参考值
        self.Error = self.Target - refer    # 计算误差
        # self.total_err += self.Error

        # 下面是其他人在优化代码时加入的试验性代码，针对转向逻辑的改动，最后效果不好弃用了。
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
        # PID输出
        self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_err)
        self.last_err = self.Error      # 记录这一帧的误差

        self.logger.write_info(f"PID: Refer={refer}, Error={self.Error}.")

        return refer
    
    # 计算参考值
    def pid_referAdjust(self):
        self.logger.write_info(f"Black line: x={self.line_x}, y={self.line_y}.")

        # 如果识别到二维码直接向二维码前进    
        if self.findqrcode and self.qrcode.area > self.qrcodeArea:  
            # self.output_sum = 0.0
            self.qr_deque.append(self.qrcode)   # 将二维码加入队列，防止在前往二维码的途中出现突然有某帧没识别到的情况
            refer = self.qrcode.x               # 二维码的位置作为参考值
            
            # print(self.qrcode.area)
        # 如果二维码队列中有二维码信息，向最新的一个二维码方向前进
        elif self.qr_deque:     
            refer = self.qr_deque[len(self.qr_deque)-1].x   # 取最近一帧的二维码信息
            self.qr_deque.popleft()     # 队列头的二维码类出队列，即将最久的一帧二维码信息出队列
        # 如果均没信息，向黑线前进
        else:
            refer = self.new_line_x

        # if self.findpark and self.park.yD > 400 and self.park.xL < 50:
            # self.topark = True
        if self.topark:     # 通过配置，可以跳过这行代码，小车就不会向P点前进
            # 如果识别到P点，向p点前进
            if self.findpark:
                # self.output_sum = 0.0
                self.park_deque.append(self.park)
                refer = self.park.x
            elif self.park_deque:
                refer = self.park_deque[len(self.park_deque)-1].x
                self.park_deque.popleft()

        self.logger.write_info(f"First refer: refer={refer}.")
        self.pid_TurnJudge(refer)       # 进行避障判断

        # 如果在避障状态，根据避障方向计算参考值。
        if self.isturning:
            if self.turning == 1:       # 向左边避障，使用右侧直线计算
                # x_f = 21 / 22 * (self.max_obs.yD - 480) + 545
                x_f = 21 / 22 * (self.max_obs.yD - 480) + 555
                result = self.max_obs.xL - max(100, x_f - 295)      # 计算得到一个参考值结果
                '''
                if self.isinfront == True:
                    result = self.max_obs.xL - max(100, x_f - 295)
                else:
                    # result = self.max_obs.xL - x_f + 295
                    result = self.max_obs.xL - max(100, x_f - 295)
                '''
                refer = min(refer, result)      # 取前面的参考值和避障参考结果的最小值，这样在黑线在更加左侧的情况下可以直接往黑线走
            elif self.turning == -1:    # 向右边避障，使用左侧直线计算
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
                refer = max(refer, result)      # 与前面同理，如果原先的参考值更靠右，那就以原来的参考值为最终参考值
            self.logger.write_info(f"ReferAdjust: turning={self.turning}, xf={x_f}, result={result}.")
            return refer
        else:
            return refer

    # 避障判断
    def pid_TurnJudge(self, refer):
        # 超过面积阈值，开始转向
        if self.max_obs_area >= self.obsArea and not self.isturning:   # and self.max_obs.rect_area.intersects(self.car_front)
            self.isturning = True
            # self.output_sum = 0.0
            print(f"[Turn]: pid_TurnJudge: isturning={self.isturning}, start turn.")
        
        # 判断左转还是右转
        if self.isturning and self.turning == 0:
            self.logger.write_obj(self.max_obs)
            # 障碍物偏视野中心位置，通过refer值和障碍物坐标判断
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
        if self.last_max_obs is None or self.max_obs is None:   # 有一帧的障碍物是None
            return True     # 结束避障
        if self.max_obs.rect_area.intersects(self.last_max_obs.rect_area):      # 使用shapely判断两个矩形框是否有交集
            inter_area = self.max_obs.rect_area.intersection(self.last_max_obs.rect_area).area      # 计算交集面积
        else:
            return True     # 没有交集，结束避障

        # 并集面积，使用面积和减去交集面积得到
        union_area = self.max_obs.rect_area.area + self.last_max_obs.rect_area.area - inter_area

        # 计算IoU
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