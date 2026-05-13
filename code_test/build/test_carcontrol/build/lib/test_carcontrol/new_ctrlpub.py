#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from origincar_msg.msg import Sign
from std_msgs.msg import Int32
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from cv_bridge import CvBridge

import time

from test_carcontrol.ros_qos import SIGN4RETURN_QOS

class CtrlPubNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.foxpub = self.create_publisher(Int32, '/sign_foxglove', 10)
        self.runpub = self.create_publisher(Int32, '/sign4return', SIGN4RETURN_QOS)
        self.sign = Int32()
        self.fox = Int32()
        self.isover = 0

        while(True):
            str1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("Input number to start.")
            print("0 - Stop.")
            print("1 - Self Control.")
            option = int(input(f"[{str1}] Root@OriginCar > "))
            if option == 0:
                self.sign.data = 5
                self.fox.data = 6
                self.runpub.publish(self.sign)
                self.foxpub.publish(self.fox)
            elif option == 1:
                self.sign.data = 6
                self.fox.data = 6
                self.runpub.publish(self.sign)
                self.foxpub.publish(self.fox)
            else:
                continue

def main(args=None):
    rclpy.init(args=args)
    node = CtrlPubNode("CtrlPubNode")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

# if __name__ == "__main__":
#     main()