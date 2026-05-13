#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 功能：实现小车pid的自动控制，完成子任务1和3，接收黑线位置和障碍物位置进行控制
import os
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import CompressedImage
from test_interface.msg import ObjPosition
from std_msgs.msg import Int32
import cv2
import numpy as np
from hobot_dnn import pyeasy_dnn as dnn

from test_carcontrol.code_test_paths import default_resnet_nv12_model

import time
import math
from shapely.geometry import Polygon


def convert_bgr_to_nv12(cv_image):
    # 首先将BGR图像转换为YUV格式
    yuv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2YUV)
    # 提取Y通道
    y_channel = yuv_image[:, :, 0]
    # 对U和V通道进行下采样
    u_channel = yuv_image[::2, ::2, 1]
    v_channel = yuv_image[::2, ::2, 2]
    # 交错U和V通道以形成UV通道
    uv_channel = np.empty((u_channel.shape[0], u_channel.shape[1] * 2), dtype=u_channel.dtype)
    uv_channel[:, ::2] = u_channel
    uv_channel[:, 1::2] = v_channel
    # 将Y通道和UV通道合并为NV12格式
    nv12_image = np.concatenate((y_channel.flatten(), uv_channel.flatten()))
    return nv12_image

# 一个类存放障碍物信息
class obstacle():
    def __init__(self, msg:ObjPosition):
        self.x = msg.x
        self.xL = msg.x_left
        self.xR = msg.x_right
        self.y = msg.y
        self.yU = msg.y_up
        self.yD = msg.y_down

        self.width = self.xR - self.xL
        self.height = self.yD - self.yU
        self.area = msg.area

        self.rect = Polygon([(self.xL, self.yU), (self.xL, self.yD), (self.xR, self.yD), (self.xR, self.yU)])

    def info_print(self):
        print("[OBJ]: x = {0}, y = {1}".format(self.x, self.y))
        print("       xL = {0}, xR = {1}, yU = {2}, yD = {3}".format(self.xL, self.xR, self.yU, self.yD))
        print("       width = {0}, height = {1}, area = {2}".format(self.width, self.height, self.area))
        

class ResNetControlNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.cmd_vel_pub = self.create_publisher(Twist, "/cmd_vel", 10)     # 发布速度与转系那个信息
        self.subscription = self.create_subscription(CompressedImage, "/image", self.image_callback, 10)        # 订阅摄像头发布的image信息
        self.objsub = self.create_subscription(ObjPosition, '/obstacle_position', self.yolo_callback, 10)       # 订阅yolo识别的信息
        self.runsub = self.create_subscription(Int32, '/sign4return', self.sign_callback, 10)   # 订阅控制信息，用于控制是否由此程序控制来自动运行
        self.models = dnn.load(str(default_resnet_nv12_model()))     # resnet模型（见 code_test/src/test_carcontrol/model/）

        # 微调PID参数
        self.Kp = 0.8  # 提高比例系数以增加对偏差的反应速度
        self.Kd = 0.5  # 减少微分系数以避免过冲
        self.Ki = 0.1  # 引入积分系数以帮助消除稳态误差（如果之前未使用）

        # 由于图像像素为640*480，所以设置目标值为320（即保持黑线在图像中点位置）
        self.Target_value = 295.0   # PID目标值
        self.last_Err = 0.0     # 上一次的误差
        self.total_Err = 0.0    # 总误差
        self.output = 0.0       # PID输出值
        self.count = 5  
        self.twist = Twist()    # 发布的速度话题
        self.obj = None
        self.isrunning = 0      # 是否由此程序控制小车自动驾驶

        self.base_area = 25000  # 阈值面积，用障碍物面积除以此面积可以得到障碍物与阈值距离的相对大小
        self.if_turning = False     # 是否处于避障状态标志

        self.car_front = Polygon([(45,480), (255, 260), (335, 260), (545, 480)])

    # 接收控制信息，决定是否由此程序控制小车自动行驶  
    def sign_callback(self, msg):
        if msg.data == 6:
            self.isrunning = 1
        elif msg.data == 5:
            self.if_turning = False
            self.road = False
            self.if_road = True

            self.isrunning = 0
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.cmd_vel_pub.publish(self.twist)
            
    # 接收yolo障碍物位置信息，目标只用到了障碍物中心位置self.obj_x，之后可改进
    def yolo_callback(self, msg):
        self.obj = obstacle(msg)
    
    # image回调函数，接收摄像头的信息后触发计算
    def image_callback(self, msg):
        # 使用CvBridge将ROS图像消息转换为OpenCV图像
        np_arr = np.frombuffer(msg.data, np.uint8)
        # 使用OpenCV解码MJPG数据
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if self.isrunning == 1:
            # 假设模型需要224x224大小的图像
            cv_image_resized = cv2.resize(image_np, (224, 224), interpolation=cv2.INTER_LINEAR)
    
            nv12_image = convert_bgr_to_nv12(cv_image_resized)
            # 转换图像格式以符合模型输入要求（如果需要）
            # 模型推理
            outputs = self.models[0].forward(np.frombuffer(nv12_image, dtype=np.uint8))
            outputs = outputs[0].buffer
            x, y = int(640 * outputs[0][0][0][0]), int(480 * outputs[0][1][0][0])
            # x,y分别为黑线的横坐标和纵坐标，上面的推理不用管，主要是下面的pid控制逻辑

            self.pid_output_test(x, y)
            # self.pid_output(x, y)

            # 发布速度，线速度目前固定，角速度通过output计算得到，可以改进
            if self.if_turning:
                self.twist.linear.x = 0.6
            else:
                self.twist.linear.x = 0.8
            self.twist.angular.z = self.output / 100
            self.cmd_vel_pub.publish(self.twist)
            # print(f"( {x}, {y} )  output = {int(self.output)},total_Err = {self.total_Err}")

    # 计算PID控制器输出-原型
    def pid_output(self, x, y):
        # PID控制逻辑，目前我的思路是：
        # 若self.obj_area == 0（即障碍物面积太小没超过yolo中的阈值时，误差是320-黑线坐标，比如黑线在320左边，error>0，离得越远error越大，角速度越大）
        # 若self.obj_x < x（即障碍物中心位置在黑线位置左边，小车右转，误差上再多一项self.obj_x）
        # 若self.obj_x > x（即障碍物中心位置在黑线位置右边，小车左转）
        if self.obj is None:
            self.Error = self.Target_value - x
        else:
            if self.obj.x <= x:
                self.Error = self.Target_value - x - self.obj.x
            elif self.obj.x > x:
                self.Error = self.Target_value - x + 590 - self.obj.x
        self.total_Err += self.Error
        # self.output为最后的角速度，这里用了pd控制，还可以改进
        self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_Err)
        self.last_Err = self.Error

    # 计算PID控制器输出-测试
    def pid_output_test(self, x, y):
        result = self.pid_TargetAdjust(x, y)
        self.Error = self.Target_value - result

        self.total_Err += self.Error
        self.output = self.Kp * self.Error + self.Kd * (self.Error - self.last_Err)
        self.last_Err = self.Error

    def pid_TargetAdjust(self, x, y):
        if self.obj is None:
            return x
        if self.obj.area >= 20000:
            self.if_turning = True
            if self.pid_TurnJudge(x, y):
                x_f = 21/22 * (self.obj.yD - 480) + 545
                d = x_f - 295
                result = self.obj.xL - d
            else:
                x_f = -21/22 * (self.obj.yD - 480) + 45
                d = 295 - x_f
                result = self.obj.xR + d
            self.obj.info_print()
            if result < 0:
                result = 0
            elif result >= 640:
                result = 640
            print(f"TargetAdjust: xf = {x_f}, result = {result}")
            return result
        else:
            self.if_turning = False
            return x

    def pid_TurnJudge(self, x, y):
        if self.obj.x >= 295:
            return True
        else:
            return False
        

                
    # 判断是否存在面积超过阈值的障碍物
    def pid_ObjJudge(self):
        if self.obj is None:
            return
        if self.obj.area != 0:
            print(f"OBJ: x={self.obj.x}, y={self.obj.y}, yD={self.obj.yD}, width={self.obj.width}, height={self.obj.height}, area={self.obj.area}")
            if self.if_road:
                if self.obj.yD >= 260:
                    xL = -21/22 * (self.obj.yD - 480) + 45
                    xR = 21/22 * (self.obj.yD - 480) + 545
                    if self.obj.x >= xL and self.obj.x <= xR:
                        self.road = not self.road
                        self.if_road = False
    
    def pid_ErrorAdjust(self):
        result = 1
        a = 1.5
        b = -2
        return 1.2
        if self.obj is not None:
            ratio = math.sqrt(self.obj.area / self.base_area)
            result = 1 + (a - 1) * (1 - math.exp(b * (ratio - 1)))
            print("[Time: {0}]: PID AdjustErr={1}".format(time.ctime(), result))
            return result
        else:
            return 1.0


def main(args=None):
    rclpy.init(args=args)
    node = ResNetControlNode("resnet_control_node")
    rclpy.spin(node)
    # os.system('ros2 topic pub --once /cmd_vel geometry_msgs/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"')
    node.destroy_node()
    rclpy.shutdown()

# if __name__ == "__main__":
#     main()