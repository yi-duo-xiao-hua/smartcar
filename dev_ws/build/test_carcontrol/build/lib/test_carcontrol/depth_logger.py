import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os
import time

from test_carcontrol.code_test_paths import output_dir

class DepthImageRecorder(Node):
    """ROS2节点，订阅深度图像话题，将深度图像保存为视频文件"""

    def __init__(self):
        super().__init__('depth_image_recorder')

        # 1. 初始化CvBridge
        self.bridge = CvBridge()
        
        # 2. 创建视频保存目录（位于 code_test/output/depth_logger）
        self.save_dir = str(output_dir("depth_logger"))
        
        # 3. 生成带时间戳的视频文件名
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.video_path = os.path.join(self.save_dir, f"depth_video_{timestamp}.avi")
        self.video_writer = None
        
        # 4. 视频参数
        self.frame_rate = 15  # 帧率（根据实际频率调整）
        self.frame_count = 0
        
        # 5. 订阅深度图像话题
        self.depth_sub = self.create_subscription(
            Image,
            '/aurora/depth/image_raw',
            self.image_callback,
            10
        )
        self.get_logger().info(f"已订阅话题：/aurora/depth/image_raw")
        self.get_logger().info(f"深度视频将保存至：{self.video_path}")

    def initialize_video_writer(self, width, height):
        """初始化视频写入器"""
        # 使用XVID编码器保存AVI视频
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter(
            self.video_path,
            fourcc,
            self.frame_rate,
            (width, height),
            isColor=False  # 单通道灰度图像
        )
        if not self.video_writer.isOpened():
            self.get_logger().error("无法创建视频文件！")
            return False
        return True

    def image_callback(self, msg: Image):
        """深度图像回调函数：处理图像并写入视频"""
        try:
            # 1. 将ROS Image转换为16位OpenCV数组
            depth_cv = self.bridge.imgmsg_to_cv2(msg, desired_encoding='mono16')
        except Exception as e:
            self.get_logger().error(f"图像转换失败：{e}")
            return

        # 2. 打印基本信息（每30帧打印一次）
        if self.frame_count % 30 == 0:
            self.get_logger().info(
                f"录制中... 帧数：{self.frame_count} | 尺寸：{msg.width}x{msg.height} | "
                f"深度范围：{np.min(depth_cv)}-{np.max(depth_cv)} mm"
            )

        # 3. 初始化视频写入器（如果是第一帧）
        if self.video_writer is None:
            if not self.initialize_video_writer(msg.width, msg.height):
                return

        # 4. 将16位深度图转换为8位（0~255）
        if depth_cv.dtype == np.uint16:
            scaled_depth = cv2.normalize(
                depth_cv, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U
            )
        else:
            scaled_depth = depth_cv.astype(np.uint8)

        # 5. 增强对比度（可选）
        scaled_depth = cv2.equalizeHist(scaled_depth)

        # 6. 写入视频帧
        self.video_writer.write(scaled_depth)
        self.frame_count += 1

    def destroy_node(self):
        """节点销毁时释放资源"""
        if self.video_writer is not None:
            self.video_writer.release()
            self.get_logger().info(f"视频保存完成！共保存 {self.frame_count} 帧")
            self.get_logger().info(f"视频路径：{self.video_path}")
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = DepthImageRecorder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("用户终止程序")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()