import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os
import time

from test_carcontrol.code_test_paths import output_dir

class DepthObstacleDetector(Node):
    """ROS2节点：订阅深度图像，识别障碍物轮廓（红线绘制），并保存为视频"""

    def __init__(self):
        super().__init__('depth_obstacle_detector')
        
        # 1. 初始化核心组件
        self.bridge = CvBridge()  # ROS与OpenCV图像转换工具
        self.frame_count = 0      # 帧计数器（用于日志）
        
        # 2. 视频保存配置（code_test/output/depth_yolo）
        self.save_dir = str(output_dir("depth_yolo"))
        timestamp = time.strftime("%Y%m%d_%H%M%S")    # 时间戳（避免文件名重复）
        self.video_path = os.path.join(self.save_dir, f"depth_obstacle_{timestamp}.avi")
        self.video_writer = None                      # 视频写入器（后续初始化）
        self.frame_rate = 15                          # 视频帧率（需与图像发布频率匹配）
        
        # 3. 订阅深度图像话题（与相机驱动保持一致）
        self.depth_sub = self.create_subscription(
            Image,
            '/aurora/depth/image_raw',
            self.image_callback,
            10  # QoS深度（队列大小）
        )
        
        # 4. 日志输出（确认节点启动）
        self.get_logger().info(f"✅ 节点启动成功！")
        self.get_logger().info(f"📡 已订阅话题：/aurora/depth/image_raw")
        self.get_logger().info(f"🎥 视频将保存至：{self.video_path}")

    def image_callback(self, msg: Image):
        """深度图像回调函数：处理每帧图像，识别轮廓并保存视频"""
        try:
            # Step 1: 将ROS Image转换为16位深度图像（保留原始深度值）
            depth_16bit = self.bridge.imgmsg_to_cv2(msg, desired_encoding='mono16')
        except Exception as e:
            self.get_logger().error(f"❌ 图像转换失败：{e}")
            return
        
        # Step 2: 预处理（16位→8位灰度图，去噪，增强对比度）
        # 16位深度图归一化到0-255（8位），便于处理
        depth_8bit = cv2.normalize(depth_16bit, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        # 高斯模糊（去噪，保留边缘）
        blurred = cv2.GaussianBlur(depth_8bit, (5, 5), 0)
        # 直方图均衡化（增强对比度，使障碍物轮廓更清晰）
        equalized = cv2.equalizeHist(blurred)
        
        # Step 3: 阈值分割（分离障碍物与背景）
        # 使用Otsu自动阈值（适用于双峰灰度分布，如障碍物亮、背景暗的场景）
        _, thresh = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 可选：自适应阈值（适用于光照不均的场景，替换上述行）
        # thresh = cv2.adaptiveThreshold(equalized, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        
        # Step 4: 形态学操作（优化二值图像，填充孔洞/去除噪声）
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构核（调整大小优化效果）
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)  # 闭操作（膨胀→腐蚀，填充小孔）
        opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)   # 开操作（腐蚀→膨胀，去除小噪声）
        
        # Step 5: 轮廓检测（提取所有前景轮廓）
        # cv2.RETR_EXTERNAL：仅保留外轮廓；cv2.CHAIN_APPROX_SIMPLE：压缩轮廓点（节省内存）
        contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Step 6: 轮廓筛选（保留符合障碍物特征的轮廓）
        # 筛选条件：面积>200像素（排除小噪声）、高宽比>1.5（锥形/直立障碍物）、顶点数3-4（三角形/梯形）
        filtered_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 200:  # 排除小噪声（根据实际场景调整阈值）
                continue
            x, y, w, h = cv2.boundingRect(cnt)  # 获取轮廓边界框
            aspect_ratio = h / w  # 高宽比（直立障碍物的高远大于宽）
            if aspect_ratio < 1.5:  # 根据实际障碍物形状调整（如锥形的高宽比通常>1.5）
                continue
            # 多边形近似（减少轮廓点，保留主要形状）
            perimeter = cv2.arcLength(cnt, True)  # 轮廓周长（闭合）
            epsilon = 0.03 * perimeter  # 近似精度（周长的3%，调整可控制形状简化程度）
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            if len(approx) not in [3, 4]:  # 保留三角形（3顶点）或梯形（4顶点）的轮廓（锥形投影）
                continue
            filtered_contours.append(cnt)  # 符合条件的轮廓加入列表
        
        # Step 7: 绘制轮廓（红线标注障碍物）
        # 将8位灰度图转换为3通道BGR（便于绘制彩色轮廓）
        contour_img = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
        # 绘制筛选后的轮廓（红线，线宽2）
        cv2.drawContours(contour_img, filtered_contours, -1, (0, 0, 255), 2)
        
        # Step 8: 初始化视频写入器（仅第一帧执行）
        if self.video_writer is None:
            height, width = contour_img.shape[:2]  # 获取图像尺寸（H×W）
            fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频编码器（XVID=AVI格式，兼容性好）
            # 初始化视频写入器（路径、编码器、帧率、尺寸）
            self.video_writer = cv2.VideoWriter(self.video_path, fourcc, self.frame_rate, (width, height))
            if not self.video_writer.isOpened():
                self.get_logger().error("❌ 无法创建视频文件！请检查路径权限或编码器设置。")
                return
        
        # Step 9: 写入视频帧
        self.video_writer.write(contour_img)
        self.frame_count += 1
        
        # Step 10: 日志输出（每30帧打印一次，避免刷屏）
        if self.frame_count % 30 == 0:
            self.get_logger().info(f"📊 录制进度：已保存 {self.frame_count} 帧 | 检测到 {len(filtered_contours)} 个障碍物")

    def destroy_node(self):
        """节点销毁时释放资源（必须执行，否则视频文件会损坏）"""
        if self.video_writer is not None:
            self.video_writer.release()  # 释放视频写入器
            self.get_logger().info(f"✅ 视频保存完成！共保存 {self.frame_count} 帧")
            self.get_logger().info(f"📂 视频路径：{self.video_path}")
        super().destroy_node()  # 调用父类销毁方法

def main(args=None):
    """节点主函数"""
    rclpy.init(args=args)  # 初始化ROS2
    node = DepthObstacleDetector()  # 创建节点实例
    try:
        rclpy.spin(node)  # 循环等待回调（阻塞直到节点停止）
    except KeyboardInterrupt:
        node.get_logger().info("⏹️ 用户终止程序")
    finally:
        node.destroy_node()  # 销毁节点（释放资源）
        rclpy.shutdown()     # 关闭ROS2

if __name__ == '__main__':
    main()