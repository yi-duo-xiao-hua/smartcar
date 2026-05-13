#!/usr/bin/env python
import rospy
import socket
import threading
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

import yaml

from test_carcontrol.code_test_paths import config_path

class CarKeyboardControl:
    def __init__(self):
        rospy.init_node('car_keyboard_control', anonymous=True)
        
        # ROS参数配置
        # self.udp_port = rospy.get_param('~udp_port', 8888)
        # self.cmd_topic = rospy.get_param('~cmd_topic', '/cmd_vel')

        with open(config_path("config_car_keyboard.yaml"), "r", encoding="utf-8") as config_file:
            self.params = yaml.safe_load(config_file)
        print(f"Image compress config: {self.params}.")
        self.udp_port = self.params["udp_port"]
        
        # 创建ROS发布者
        self.vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.active_pub = rospy.Publisher('/keyboard_active', Bool, queue_size=1)
        
        # 初始化键位映射（与原始程序完全兼容）
        self.key_mapping = {
            'up':         {'linear': {'x': 2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}},
            'down':       {'linear': {'x': -2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}},
            'left':       {'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 6.0}},
            'right':      {'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': -4.0}},
            'up_left':    {'linear': {'x': 2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 6.0}},
            'up_right':   {'linear': {'x': 2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': -4.0}},
            'down_left':  {'linear': {'x': -2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 6.0}},
            'down_right': {'linear': {'x': -2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': -4.0}},
            'stop':       {'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}}
        }
        
        # 网络设置
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(('', self.udp_port))
        self.udp_socket.settimeout(0.1)
        
        # 控制状态
        self.last_cmd_time = rospy.Time.now()
        self.current_cmd = "stop"
        self.active = False
        self.timeout = rospy.Duration(0.3)  # 300ms超时
        
        print(f"小车键盘控制节点已启动，监听端口: {self.udp_port}")
        
    def udp_listener(self):
        while not rospy.is_shutdown():
            try:
                data, addr = self.udp_socket.recvfrom(1024)
                cmd = data.decode().strip()
                if cmd in self.key_mapping:
                    self.current_cmd = cmd
                    self.last_cmd_time = rospy.Time.now()
                    if not self.active:
                        self.active = True
                        print("键盘控制激活")
            except socket.timeout:
                pass
                
    def publish_control(self):
        rate = rospy.Rate(50)  # 50Hz
        while not rospy.is_shutdown():
            # 检查超时
            if (rospy.Time.now() - self.last_cmd_time) > self.timeout:
                if self.active:
                    self.active = False
                    self.current_cmd = "stop"
                    print("键盘控制超时停用")
            
            # 发布控制状态
            self.active_pub.publish(Bool(self.active))
            
            # 发布速度命令
            twist = Twist()
            cmd = self.key_mapping[self.current_cmd]
            
            twist.linear.x = cmd['linear']['x']
            twist.linear.y = cmd['linear']['y']
            twist.linear.z = cmd['linear']['z']
            
            twist.angular.x = cmd['angular']['x']
            twist.angular.y = cmd['angular']['y']
            twist.angular.z = cmd['angular']['z']
            
            self.vel_pub.publish(twist)
            rate.sleep()
            
    def run(self):
        # 启动UDP监听线程
        udp_thread = threading.Thread(target=self.udp_listener)
        udp_thread.daemon = True
        udp_thread.start()
        
        # 主控制循环
        self.publish_control()

if __name__ == '__main__':
    try:
        controller = CarKeyboardControl()
        controller.run()
    except rospy.ROSInterruptException:
        pass