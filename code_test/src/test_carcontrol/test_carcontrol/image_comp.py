#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import CompressedImage

import yaml

from test_carcontrol.code_test_paths import config_path

class ImageCompressor(Node):
    def __init__(self):
        super().__init__('image_compressor')
        
        # 声明可调参数（可在运行时通过ros2 param set修改）
        
        with open(config_path("config_image_compress.yaml"), "r", encoding="utf-8") as config_file:
            self.params = yaml.safe_load(config_file)
        print(f"Image compress config: {self.params}.")
        
        # 创建订阅和发布
        self.subscription = self.create_subscription(
            CompressedImage,
            '/image',
            self.image_callback,
            10)
        self.publisher = self.create_publisher(
            CompressedImage,
            '/topic_myimage',
            10)
        
        self.get_logger().info("图像压缩节点已启动，等待输入图像...")

    def image_callback(self, msg):
        # 获取当前参数值
        # scale_factor = self.get_parameter('scale_factor').value
        # jpeg_quality = self.get_parameter('jpeg_quality').value
        # enable_compression = self.get_parameter('enable_compression').value

        scale_factor = self.params["scale_factor"]
        jpeg_quality = self.params["jpeg_quality"]
        enable_compression = self.params["enable_compression"]
        
        # 将ROS消息转换为OpenCV图像
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        if cv_image is None:
            self.get_logger().error("图像解码失败！")
            return
        
        # 应用缩放
        if scale_factor != 1.0:
            new_width = int(cv_image.shape[1] * scale_factor)
            new_height = int(cv_image.shape[0] * scale_factor)
            cv_image = cv2.resize(cv_image, (new_width, new_height))
        
        # 压缩图像
        compression_params = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality] if enable_compression else []
        success, compressed_data = cv2.imencode('.jpg', cv_image, compression_params)
        
        if not success:
            self.get_logger().error("图像压缩失败！")
            return
        
        # 创建并发布新消息
        compressed_msg = CompressedImage()
        compressed_msg.header = msg.header
        compressed_msg.format = "jpeg"
        compressed_msg.data = compressed_data.tobytes()
        self.publisher.publish(compressed_msg)
        
        # 记录调试信息（频率限制避免日志过多）
        if hasattr(self, '_count'):
            self._count += 1
            if self._count % 30 == 0:
                self.get_logger().info(
                    f"已处理图像 | 缩放: {scale_factor:.1f}x | 质量: {jpeg_quality} | "
                    f"大小: {len(msg.data)//1024}KB -> {len(compressed_data)//1024}KB"
                )
        else:
            self._count = 1

def main(args=None):
    rclpy.init(args=args)
    node = ImageCompressor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()