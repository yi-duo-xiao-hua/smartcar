#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from origincar_msg.msg import Sign
from std_msgs.msg import Int32
import cv2
from pyzbar.pyzbar import decode
from cv_bridge import CvBridge

from test_carcontrol.ros_qos import SIGN4RETURN_QOS

class QRcodeScanNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(CompressedImage, "/image", self.image_callback, 10)
        self.sign_switchpublisher = self.create_publisher(Sign,'/sign_switch',10)
        self.runpub = self.create_publisher(Int32, '/sign4return', SIGN4RETURN_QOS)
        self.runsub = self.create_subscription(
            Int32, '/sign4return', self.sign_callback, SIGN4RETURN_QOS
        )
        self.numpub = self.create_publisher(Int32, '/num_output', 10)
        self.sign = Int32()
        self.numoutput = Int32()
        self.isover = 0


    def sign_callback(self, msg):
        if msg.data == 6:
            self.isover = 0

    def image_callback(self, msg):
        # /image 为 sensor_msgs/CompressedImage（MJPEG），须用 compressed_imgmsg_to_cv2
        if self.isover == 0:
            image = self.bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="bgr8")
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
                    self.isover = 1
                    '''
                    if int(data) % 2 == 1:
                        print('顺时针')
                    else:
                        print('逆时针')
                    '''

def main(args=None):
    rclpy.init(args=args)
    node = QRcodeScanNode("QRcode_scan_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

# if __name__ == "__main__":
#     main()