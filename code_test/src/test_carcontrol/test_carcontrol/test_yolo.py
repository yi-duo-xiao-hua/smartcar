import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from test_interface.msg import ObjPosition
import numpy as np
from ai_msgs.msg import PerceptionTargets
import threading

class YOffsetsMaxPublisher(Node):

    def __init__(self):
        super().__init__('y_offsets_max_publisher')
        self.YoloV5Subscriber = self.create_subscription(
            PerceptionTargets,
            'hobot_dnn_detection',
            self.YoloV5_listener_callback,
            100)
        self.yolopub = self.create_publisher(ObjPosition, '/obstacle_position', 10)
        self.data_store = {
            "y_offsets_conf": 150,  # 示例值，根据实际情况调整
            "needzhuanwan": False
        }
        self.lock = threading.Lock()
        

    def YoloV5_listener_callback(self, msg):
        result_list = msg.targets 
        obj_len = len(result_list)
        obj_x = 0
        obj_y = 0
        obj_w = 0
        obj_h = 0
        # self.obj_x = np.full(8, -1)  # 存坐标
        # self.obj_y = np.full(8, -1)
        max_area = 0  # 用于存储最大面积
        position = ObjPosition()
        with self.lock:
            for i in range(obj_len):
                if not result_list[i].rois:
                    continue
                for roi in result_list[i].rois:
                    box = roi.rect  # 直接获取 roi 的 rect 属性
                    x_offset = box.x_offset
                    y_offset = box.y_offset
                    width = box.width
                    height = box.height
                    area = width * height
                    if area > max_area:
                        max_area = area
                        obj_x = x_offset
                        obj_y = y_offset
                        obj_w = width
                        obj_h = height
                    # id = result_list[i].track_id
            # if max_area > 30000:
            if True:
                self.get_logger().info(f'obj_x: {obj_x + int(obj_w/2)},obj_y: {obj_y},area: {max_area}')
                position.x = obj_x + int(obj_w/2)
                position.x_left = obj_x
                position.x_right = obj_x +obj_w
                position.area = max_area
                position.y = obj_y + int(obj_h/2)
                position.y_up = obj_y
                position.y_down = obj_y + obj_h
                self.yolopub.publish(position)
            else:
                position.x = 0
                position.x_left = 0
                position.x_right = 0
                position.area = 0
                position.y = 0
                position.y_up = 0
                position.y_down = 0
                self.yolopub.publish(position)
                    

def main(args=None):
    rclpy.init(args=args)
    y_offsets_max_publisher = YOffsetsMaxPublisher()
    rclpy.spin(y_offsets_max_publisher)
    y_offsets_max_publisher.destroy_node()
    rclpy.shutdown()

# if __name__ == '__main__':
#    main()