# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
from hobot_dnn import pyeasy_dnn as dnn

from test_interface.msg import ResnetMsg
from test_carcontrol.code_test_paths import config_path, get_code_test_root, resolve_model_file

import time
import yaml

# 将bgr格式的图像转换为nv12格式
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

"""
写Log文件类，用于将程序运行的信息输出到一个Log文件中
输出的一行格式为
```python
f"[{年月日+时分秒时间}][{从开始记录到写入信息时的浮点数秒数}][{消息类型}]: {消息内容}\n"
```

使用refresh_start()重置开始时间，表示新的一次自动控制阶段开始
使用write_info(infostr)，将一个字符串infostr作为信息写入log文件
类在被销毁，即程序结束时，会自动写入结束语并关闭文件
"""
class PIDLogger():
    def __init__(self):
        self.start_time = 0     # 开始自动控制的时间
        self.error = False      # 是否正常打开log文件
        
        # 创建并打开log文件
        root = get_code_test_root()
        log_dir = root / "log" / "new_resnet"
        log_dir.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%m%d_%H%M%S", time.localtime())
        self.log_path = os.fspath(log_dir / f"resnet_log_{stamp}.txt")
        self.log_file = open(self.log_path, "a", encoding="utf-8", buffering=1)
        # 如果打开失败，则将错误位置位
        if self.log_file is None:
            print("[Error]: Cannot open log file.")
            self.error = True
            return
        
        # 写log文件开始的内容
        str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_file.write("--------------------| Log Start |--------------------\n")
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

    # 类被销毁时关闭log文件并写入结束语
    def __del__(self):
        if (not self.error) and self.log_file is not None:
            str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_file.write("--------------------| Log End |--------------------\n")
            self.log_file.write(f"Log end at {str1}.\n")
            self.log_file.close()

class ResNetControlNode(Node):
    def __init__(self, name):
        super().__init__(name)

        """
        使用配置文件来制定调用的模型路径
        避免每次更换模型都要重新编译代码
        只需要修改对应路径下的配置文件即可实现模型的切换
        配置文件位于 code_test/src/test_carcontrol/config/，根目录由 CODE_TEST_ROOT 或自动探测决定。
        """
        with open(config_path("config_new_resnet.yaml"), "r", encoding="utf-8") as config_file:
            self.params = yaml.safe_load(config_file)
        self.model_path = str(resolve_model_file(self.params["model"]))
        print(f"Config: {self.params}.")            # 打印程序运行的配置

        self.subscription = self.create_subscription(CompressedImage, "/image", self.image_callback,
                                                     10)  # 订阅摄像头发布的image信息
        # self.models = dnn.load(
        #     '/home/sunrise/roscode/code_test/src/test_carcontrol/model/resnet_0804_model_best1000.bin')  # resnet模型
        self.models = dnn.load(self.model_path)  # 调用resnet模型
        print(f"[Info]: Load model {self.model_path}.")

        # 将Resnet输出的注意点的坐标，发布到一个ROS话题中
        self.line_pub = self.create_publisher(ResnetMsg, "/topic_ResnetMsg", 10)

        # 将程序运行过程中的关键输出记录到一个log文件中
        self.logger = PIDLogger()
        self.logger.refresh_start()

        # 帧计数，用于记录每次识别的帧的序号，方便每隔一定数量的帧输出一下结果，确保程序正确运行
        self.frame_count = 0

    # image回调函数，接收摄像头的信息后触发计算
    def image_callback(self, msg):
        # 使用CvBridge将ROS图像消息转换为OpenCV图像
        np_arr = np.frombuffer(msg.data, np.uint8)
        # 使用OpenCV解码MJPG数据
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        # 假设模型需要224x224大小的图像
        cv_image_resized = cv2.resize(image_np, (224, 224), interpolation=cv2.INTER_LINEAR)

        nv12_image = convert_bgr_to_nv12(cv_image_resized)
        # 转换图像格式以符合模型输入要求（如果需要）
        # 模型推理
        outputs = self.models[0].forward(np.frombuffer(nv12_image, dtype=np.uint8))
        outputs = outputs[0].buffer
        x, y = int(640 * outputs[0][0][0][0]), int(480 * outputs[0][1][0][0])
        # x,y分别为黑线的横坐标和纵坐标，上面的推理不用管，主要是下面的pid控制逻辑

        # 黑线识别结果消息的接口
        resnet_msg = ResnetMsg()
        resnet_msg.line_x = x
        resnet_msg.line_y = y

        # 每隔30帧（大约1秒）输出一次当前帧的识别结果
        if self.frame_count % 30 == 0:
            print(f"[Frame_callback]: Frame_count={self.frame_count}.")
            print(f"                  Black Line: x={x}, y={y}.")

        self.frame_count += 1
        self.line_pub.publish(resnet_msg)       # 发布黑线识别结果
        self.logger.write_info(f"Result: x={x}, y={y}.")

def main(args=None):
    rclpy.init(args=args)
    node = ResNetControlNode("new_resnet_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

# if __name__ == "__main__":
#     main()
