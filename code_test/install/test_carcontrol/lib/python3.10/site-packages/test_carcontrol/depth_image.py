import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from ai_msgs.msg import PerceptionTargets
from test_interface.msg import ObjPosition
import threading
from std_msgs.msg import Float64


class ObstacleDistancePublisher(Node):
    """
    ROS2节点，结合YOLO目标检测和深度图像，计算并发布障碍物中心点距离
    """

    def __init__(self):
        super().__init__('obstacle_distance_publisher')

        # 1. 初始化CvBridge（ROS与OpenCV图像转换工具）
        self.bridge = CvBridge()

        # 2. 订阅YOLO目标检测结果
        self.yolo_sub = self.create_subscription(
            PerceptionTargets,
            'hobot_dnn_detection',
            self.yolo_callback,
            10
        )
        self.get_logger().info("已订阅YOLO检测话题：hobot_dnn_detection")

        # 3. 订阅深度图像话题
        self.depth_sub = self.create_subscription(
            Image,
            '/aurora/depth/image_raw',
            self.depth_callback,
            10
        )
        self.get_logger().info("已订阅深度图像话题：/aurora/depth/image_raw")

        # 4. 发布障碍物位置和距离信息
        self.obstacle_pub = self.create_publisher(ObjPosition, '/obstacle_position', 10)
        self.distance_pub = self.create_publisher(Float64, '/obstacle_distance', 10)
        self.get_logger().info("已创建发布者：/obstacle_position 和 /obstacle_distance")

        # 5. 初始化共享数据
        self.latest_depth_image = None  # 存储最新的深度图像
        self.latest_obstacle_pos = None  # 存储最新的障碍物位置
        self.lock = threading.Lock()  # 线程锁确保数据安全

        # 6. 定时器用于定期处理数据
        self.timer = self.create_timer(0.1, self.process_data)  # 10Hz处理频率

        # 7. 配置参数
        self.min_valid_depth = 300  # 最小有效深度值(mm)
        self.max_valid_depth = 10000  # 最大有效深度值(mm)
        self.min_obstacle_area = 1000  # 最小障碍物面积阈值

    def depth_callback(self, msg):
        """深度图像回调函数：存储最新深度图像"""
        try:
            # 将ROS Image转换为16位OpenCV数组（单位：毫米）
            depth_cv = self.bridge.imgmsg_to_cv2(msg, desired_encoding='mono16')

            with self.lock:
                self.latest_depth_image = depth_cv

        except Exception as e:
            self.get_logger().error(f"深度图像转换失败：{e}")

    def yolo_callback(self, msg):
        """YOLO检测回调函数：处理目标检测结果并存储障碍物位置"""
        result_list = msg.targets
        obj_len = len(result_list)
        obj_x = 0
        obj_y = 0
        obj_w = 0
        obj_h = 0
        max_area = 0  # 用于存储最大面积
        obstacle_found = False

        # 查找最大障碍物
        for i in range(obj_len):
            if not result_list[i].rois:
                continue
            for roi in result_list[i].rois:
                box = roi.rect
                x_offset = box.x_offset
                y_offset = box.y_offset
                width = box.width
                height = box.height
                area = width * height

                # 只考虑足够大的物体
                if area > self.min_obstacle_area and area > max_area:
                    max_area = area
                    obj_x = x_offset
                    obj_y = y_offset
                    obj_w = width
                    obj_h = height
                    obstacle_found = True

        # 创建位置对象
        position = ObjPosition()
        if obstacle_found:
            position.x = obj_x + int(obj_w / 2)  # 中心点X坐标
            position.x_left = obj_x  # 左边界
            position.x_right = obj_x + obj_w  # 右边界
            position.area = max_area  # 占据面积
            position.y = obj_y + int(obj_h / 2)  # 中心点Y坐标
            position.y_up = obj_y  # 上边界
            position.y_down = obj_y + obj_h  # 下边界

            with self.lock:
                self.latest_obstacle_pos = position
        else:
            # 没有检测到障碍物时发送空位置
            position.x = 0
            position.x_left = 0
            position.x_right = 0
            position.area = 0
            position.y = 0
            position.y_up = 0
            position.y_down = 0

            with self.lock:
                self.latest_obstacle_pos = None

    def process_data(self):
        """处理数据：结合深度图像和障碍物位置计算距离"""
        with self.lock:
            depth_image = self.latest_depth_image
            obstacle_pos = self.latest_obstacle_pos

        # 检查是否有有效数据
        if depth_image is None:
            self.get_logger().debug("等待深度图像...")
            return

        if obstacle_pos is None:
            # 没有障碍物时发布距离为0
            distance_msg = Float64()
            distance_msg.data = 0.0
            self.distance_pub.publish(distance_msg)
            return

        # 获取障碍物中心点坐标
        center_x = int(obstacle_pos.x)
        center_y = int(obstacle_pos.y)

        # 检查坐标是否在图像范围内
        if (center_x < 0 or center_x >= depth_image.shape[1] or
                center_y < 0 or center_y >= depth_image.shape[0]):
            self.get_logger().warn(f"障碍物中心点超出图像范围: ({center_x}, {center_y})")
            return

        # 获取深度值（单位：毫米）
        depth_value = depth_image[center_y, center_x]

        # 过滤无效深度值
        if depth_value < self.min_valid_depth or depth_value > self.max_valid_depth:
            self.get_logger().debug(f"无效深度值: {depth_value} mm (位置: {center_x}, {center_y})")
            return

        # 发布障碍物位置信息
        self.obstacle_pub.publish(obstacle_pos)

        # 发布距离信息
        distance_msg = Float64()
        distance_msg.data = float(depth_value)
        self.distance_pub.publish(distance_msg)

        # 打印日志
        self.get_logger().info(
            f"障碍物位置: ({center_x}, {center_y}), "
            f"距离: {depth_value} mm, "
            f"面积: {obstacle_pos.area} px²"
        )


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleDistancePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("用户终止程序")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()