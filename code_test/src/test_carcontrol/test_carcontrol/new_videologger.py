#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from ai_msgs.msg import PerceptionTargets
from sensor_msgs.msg import CompressedImage

from test_interface.msg import VideoLogMsg
from test_interface.msg import ObjPosition
from test_interface.msg import ResnetMsg
from test_interface.msg import ObjectMsg

import numpy as np
import time
import math
from io import TextIOWrapper
import threading
import time

import cv2
import yaml

from test_carcontrol.code_test_paths import config_path, get_code_test_root
from test_carcontrol.ros_qos import CMD_VEL_QOS

# 识别的物体类
class object():
    def __init__(self, x:ObjectMsg):
        if x is not None:
            self.obj_type = x.obj_type      # 物体类别
            self.xL = x.xl                  # 矩形框左侧边x坐标
            self.xR = x.xr                  # 矩形框右侧边x坐标
            self.yU = x.yu                  # 矩形框上边y坐标
            self.yD = x.yd                  # 矩形框下边y坐标
            # 原本是矩形框的面积，后来改了距离识别后改成了distance，距离判断启用后这里没改，但恢复成了原来的传输面积
            self.distance = x.distance      

class VideoLogger(Node):
    def __init__(self):
        super().__init__("VideoLoggerNode")
        self.subscription = self.create_subscription(CompressedImage, "/image", self.image_callback,
                                                     10)  # 订阅摄像头发布的image信息
        self.line_sub = self.create_subscription(ResnetMsg, "/topic_ResnetMsg", self.resnet_callback, 10)       # 订阅Resnet识别结果
        self.VideoLog_sub = self.create_subscription(VideoLogMsg, "/topic_VideoLogMsg", self.videolog_callback, 10)     # 订阅自动控制程序的输出话题
        self.cmd_vel_sub = self.create_subscription(
            Twist, "/cmd_vel", self.cmd_vel_callback, CMD_VEL_QOS
        )

        time_str = time.strftime("%m%d_%H%M%S", time.localtime())        # 获取当前时间，用于输出视频的命名
        _vd = get_code_test_root() / "output" / "videolog"
        _vd.mkdir(parents=True, exist_ok=True)
        self.video_path = str(_vd / f"video_{time_str}.avi")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')        # 使用opencv库输出视频
        self.out = cv2.VideoWriter(self.video_path, fourcc, 30, (640,480))

        # 配置文件，可以配置输出视频中各类信息的显示
        with open(config_path("config_videologger.yaml"), "r", encoding="utf-8") as config_file:
            self.params = yaml.safe_load(config_file)
        print(f"VideoLogger config: {self.params}")

        # 字体配置
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.6
        self.font_color = (0, 0, 255)
        self.font_thickness = 1

        # resnet注意点
        self.line_x = 0
        self.line_y = 0

        # 自动控制程序有关的信息
        self.isturning = False      # 是否在避障
        self.refer = 0.0            # 参考值
        self.linear = 0.0           # 输出的速度值
        self.angular = 0.0          # 输出的角速度
        
        # 速度话题的信息
        self.cmd_linear = 0.0
        self.cmd_angular = 0.0

        # 物体的信息
        self.obs_list = None
        self.qrcode = None
        self.park = None

        self.lock = threading.Lock()
    
    # image回调函数，接收摄像头的信息后触发计算
    def image_callback(self, msg):
        # 使用CvBridge将ROS图像消息转换为OpenCV图像
        np_arr = np.frombuffer(msg.data, np.uint8)
        # 使用OpenCV解码MJPG数据
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        self.write_frame(frame)
    
    # 接收速度话题的信息
    def cmd_vel_callback(self, msg:Twist):
        self.cmd_linear = msg.linear.x
        self.cmd_angular = msg.angular.z

    # 接收Yolo控制程序发出的信息
    def videolog_callback(self, msg):
        # 接收有关信息
        self.isturning = msg.isturning
        self.refer = msg.refer
        self.linear = msg.linear
        self.angular = msg.angular

        self.qrcode = None
        self.obs_list = []

        # 将物体信息加入对应的列表
        temp_list = msg.obj_list
        for x in temp_list:
            type = x.obj_type
            if type == "obstacle":
                self.obs_list.append(object(x))
            elif type == "park":
                self.park = object(x)
            elif type == "qrcode":
                self.qrcode = object(x)

    # 接收Resnet输出的注意点
    def resnet_callback(self, msg):
        self.line_x = msg.line_x
        self.line_y = msg.line_y

    # 输出视频帧
    def write_frame(self, frame):
        # 绘制网格
        if self.params["grid"]:
            for i in range(0, 640, 100):
                cv2.line(frame, (i, 0), (i, 480), color=(128,128,128), thickness=1)
            for i in range(0, 480, 100):
                cv2.line(frame, (0, i), (640, i), color=(128,128,128), thickness=1)
        
        # 小车行驶前方区域
        if self.params["car_front"]:
            cv2.line(frame, (45,480), (255, 260), color=(255, 0, 255), thickness=2)
            cv2.line(frame, (335, 260), (545, 480), color=(255, 0, 255), thickness=2)

        # 黑线圆点
        if self.params["black_line"]:
            cv2.circle(frame, (int(self.line_x), int(self.line_y)), 8, (0,0,255), -1)

        # 物体信息
        if self.params["objects"]:
            if self.obs_list is not None and self.obs_list:
                for obj in self.obs_list:
                    cv2.rectangle(frame, (obj.xL, obj.yU), (obj.xR, obj.yD), (0, 255, 0), 2)
                    cv2.putText(frame, f"{obj.distance}", (obj.xL, obj.yU + 20), self.font,
                            self.font_scale, self.font_color, self.font_thickness)
            if self.qrcode is not None:
                cv2.rectangle(frame, (self.qrcode.xL, self.qrcode.yU), (self.qrcode.xR, self.qrcode.yD), (0, 0, 255), 2)
            if self.park is not None:
                cv2.rectangle(frame, (self.park.xL, self.park.yU), (self.park.xR, self.park.yD), (0, 0, 255), 2)
        
        # 输出信息
        if self.params["text"]:
            text_line = [
                f"Is_Turning={self.isturning}",
                f"Black Line: x={self.line_x}, y={self.line_y}.",
                f"New_yolo: linear={self.linear:.4f}, Angular={self.angular:.4f}.",
                f"Cmd_vel: linear={self.cmd_linear:.4f}, Angular={self.cmd_angular:.4f}."
            ]
            for i, text in enumerate(text_line):
                cv2.putText(frame, text, (10, 25+i*30), self.font,
                            self.font_scale, self.font_color, self.font_thickness)
        
        # 参考线
        if self.params["refer"]:
            cv2.line(frame, (int(self.refer), 0), (int(self.refer), 480), color=(255,0,0), thickness=1)
            cv2.putText(frame, "Refer", (int(self.refer)+5, 460), self.font,
                        self.font_scale, self.font_color, self.font_thickness)
        
        self.out.write(frame)
    
    def __del__(self):
        self.out.release()
        


def main(args=None):
    rclpy.init(args=args)
    car_videologger = VideoLogger()
    rclpy.spin(car_videologger)
    car_videologger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()