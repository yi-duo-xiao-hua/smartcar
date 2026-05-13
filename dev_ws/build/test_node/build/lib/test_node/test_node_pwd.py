import rclpy
from rclpy.node import Node
import time
import os

def main(args=None):
    rclpy.init(args=args)
    node = Node("node_pwd")
    pwd = os.getcwd()

    while rclpy.ok():
        node.get_logger().info(pwd)
        time.sleep(2)

    node.destroy_node()
    rclpy.shutdown()