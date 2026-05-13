import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
import os

from test_carcontrol.ros_qos import CMD_VEL_QOS

class controlPublisher(Node):
    def __init__(self):
        super().__init__('control_publisher')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', CMD_VEL_QOS)
        
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.cmd_vel = Twist()
        self.cmd_vel.linear.x = 0.2
        self.cmd_vel.angular.z = 1.0

    def timer_callback(self):
        self.publisher.publish(self.cmd_vel)
        self.get_logger().info("Publishing: Linear x = {0:.2f}, Angular z = {1:.2f}".format(self.cmd_vel.linear.x, self.cmd_vel.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = controlPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        os.system('ros2 topic pub --once /cmd_vel geometry_msgs/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"')
    
    node.destroy_node()
    rclpy.shutdown()
