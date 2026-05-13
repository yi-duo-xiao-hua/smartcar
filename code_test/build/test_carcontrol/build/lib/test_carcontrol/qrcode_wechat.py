#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from origincar_msg.msg import Sign
from std_msgs.msg import Int32
import cv2
import numpy as np
from cv_bridge import CvBridge

from test_carcontrol.code_test_paths import config_path
from test_carcontrol.ros_qos import SIGN4RETURN_QOS

class QRcodeScanNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.bridge = CvBridge()
        self.depro = str(config_path("detect.prototxt"))
        self.decaf = str(config_path("detect.caffemodel"))
        self.srpro = str(config_path("sr.prototxt"))
        self.srcaf = str(config_path("sr.caffemodel"))
        self.subscription = self.create_subscription(Image, "/aurora/rgb/image_raw", self.image_callback, 10)
        self.runsub = self.create_subscription(
            Int32, '/sign4return', self.sign_callback, SIGN4RETURN_QOS
        )
        # self.subscription = self.create_subscription(CompressedImage, "/image", self.image_callback, 10)
        self.sign_switchpublisher = self.create_publisher(Sign,'/sign_switch',10)
        self.runpub = self.create_publisher(Int32, '/sign4return', SIGN4RETURN_QOS)
        self.numpub = self.create_publisher(Int32, '/num_output', 10)
        self.sign = Int32()
        self.numoutput = Int32()
        self.isover = 0


    def sign_callback(self, msg):
        if msg.data == 6:
            self.isover = 0
    
    
    def image_callback(self, msg):
        if self.isover == 0:
            # np_arr = np.frombuffer(msg.data, np.uint8)
            # image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            detector = cv2.wechat_qrcode_WeChatQRCode(self.depro, self.decaf, self.srpro, self.srcaf)
            barcodes, points = detector.detectAndDecode(gray_image)
            for data in barcodes:
                print(data)
                if int(data) % 2 == 1:
                    msg_sign = Sign()
                    msg_sign.sign_data = 3
                    self.sign_switchpublisher.publish(msg_sign)
                else:
                    msg_sign = Sign()
                    msg_sign.sign_data = 4
                    self.sign_switchpublisher.publish(msg_sign)
                self.sign.data = 5
                self.numoutput.data = int(data)
                self.runpub.publish(self.sign)
                self.numpub.publish(self.numoutput)
                self.isover = 1
        '''
        decoded_objects = decode(gray_image)
        if decoded_objects:
            for obj in decoded_objects:
                # print('Type:', obj.type)
                data = obj.data.decode('utf-8')
                print('DataType:', type(data))
                print('Data:', data)  # 解码二维码数据
                if int(data) % 2 == 1:
                    msg_sign = Sign()
                    msg_sign.sign_data = 3
                    self.sign_switchpublisher.publish(msg_sign)
                else:
                    msg_sign = Sign()
                    msg_sign.sign_data = 4
                    self.sign_switchpublisher.publish(msg_sign)
                # self.get_logger().info(f'Publishing: {msg_sign.sign_data}')
                self.sign.data = 5
                self.numoutput.data = int(data)
                self.runpub.publish(self.sign)
                self.numpub.publish(self.numoutput)
                self.isover = 1.
        '''


def main(args=None):
    rclpy.init(args=args)
    node = QRcodeScanNode("QRcode_scan_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

# if __name__ == "__main__":
#     main()