import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os
import time

from test_carcontrol.code_test_paths import output_dir

class ConeDetector(Node):
    """ROS2节点：订阅RGB图像，识别深蓝色锥桶（红线绘制），保存视频"""

    def __init__(self):
        super().__init__('cone_detector')
        
        # 1. 核心组件初始化
        self.bridge = CvBridge()  # ROS与OpenCV图像转换
        self.frame_count = 0      # 帧计数器（日志用）
        
        # 2. 视频保存配置（code_test/output/cone_detector）
        self.save_dir = str(output_dir("cone_detector"))
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # 时间戳（避免文件名重复）
        self.video_path = os.path.join(self.save_dir, f"cone_detector_{timestamp}.avi")
        self.video_writer = None  # 视频写入器（后续初始化）
        self.frame_rate = 15      # 视频帧率（需与RGB相机发布频率匹配）
        
        # 3. 订阅RGB图像话题（与相机驱动一致）
        self.rgb_sub = self.create_subscription(
            Image,
            '/aurora/rgb/image_raw',
            self.image_callback,
            10  # QoS深度（队列大小）
        )
        
        # 4. 关键参数配置（基于实拍图校准）
        # （1）颜色阈值（HSV空间，适配深蓝色主体）
        self.lower_blue = np.array([110, 120, 80])     # 深蓝色：H=110-130°，S=120-200，V=80-120
        self.upper_blue = np.array([130, 200, 120])    # 深蓝色：H=110-130°，S=120-200，V=80-120
        # （2）预处理参数（减少噪声+提升亮度）
        self.blur_ksize = (3, 3)  # 3x3高斯模糊核（保留颜色边界）
        # （3）形态学操作参数（优化掩码）
        self.morph_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 5x5矩形核（填充孔洞）
        # （4）轮廓筛选条件（适配锥桶形状）
        self.min_contour_area = 200  # 最小轮廓面积（像素，排除小噪声）
        self.min_aspect_ratio = 1.5  # 最小高宽比（锥桶高>宽，需>1.5）
        self.epsilon_ratio = 0.03    # 多边形近似精度（周长的3%，保留锥形轮廓）
        
        # 5. 日志输出（确认节点启动）
        self.get_logger().info("✅ 锥桶检测节点启动成功！")
        self.get_logger().info(f"📡 已订阅话题：/aurora/rgb/image_raw")
        self.get_logger().info(f"🎥 视频将保存至：{self.video_path}")

    def image_callback(self, msg: Image):
        """RGB图像回调函数：处理每帧图像，识别深蓝色锥桶轮廓并保存视频"""
        try:
            # Step 1: 将ROS Image转换为OpenCV BGR图像（编码为`bgr8`）
            rgb_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"❌ 图像转换失败：{e}")
            return
        
        # Step 2: 预处理（高斯模糊+转HSV+V通道均衡化+转回RGB）
        blurred = cv2.GaussianBlur(rgb_img, self.blur_ksize, 0)  # 3x3高斯模糊（减少噪声）
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  # 转HSV空间（保留颜色特征）
        h, s, v = cv2.split(hsv)                        # 分离HSV通道
        v_eq = cv2.equalizeHist(v)                       # 对V通道做直方图均衡化（提升亮度对比度）
        hsv_eq = cv2.merge([h, s, v_eq])                 # 合并通道（不改变H和S）
        rgb_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR) # 转回RGB空间（用于后续处理）
        
        # Step 3: 颜色分割（提取深蓝色主体）
        mask_blue = cv2.inRange(hsv_eq, self.lower_blue, self.upper_blue)  # 使用均衡化后的HSV图像
        mask = mask_blue  # 仅保留深蓝色掩码（不处理白色条纹）
        
        # Step 4: 形态学操作（优化掩码，保留轮廓）
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.morph_kernel, iterations=1)  # 闭操作（填充孔洞）
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.morph_kernel, iterations=1)   # 开操作（去除小噪声）
        
        # Step 5: 轮廓检测（提取掩码中的外轮廓）
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Step 6: 轮廓筛选（保留符合锥桶特征的轮廓）
        filtered_contours = []
        for cnt in contours:
            # 条件1：排除小噪声轮廓（面积<最小阈值）
            area = cv2.contourArea(cnt)
            if area < self.min_contour_area:
                continue
            # 条件2：排除宽大于高的轮廓（非锥桶形状）
            x, y, w, h = cv2.boundingRect(cnt)  # 边界框（x:左, y:上, w:宽, h:高）
            aspect_ratio = h / w  # 高宽比（锥桶高应远大于宽）
            if aspect_ratio < self.min_aspect_ratio:
                continue
            # 条件3：保留锥形轮廓（多边形近似为3-4顶点）
            perimeter = cv2.arcLength(cnt, True)  # 轮廓周长（闭合）
            epsilon = self.epsilon_ratio * perimeter  # 近似精度（周长的3%）
            approx = cv2.approxPolyDP(cnt, epsilon, True)  # 多边形近似
            if len(approx) not in [3, 4]:  # 三角形（3顶点）或梯形（4顶点，锥桶投影）
                continue
            # 符合条件的轮廓加入列表
            filtered_contours.append(cnt)
        
        # Step 7: 绘制轮廓（用红线标注锥桶，线宽2）
        cv2.drawContours(rgb_img, filtered_contours, -1, (0, 0, 255), 2)
        
        # Step 8: 初始化视频写入器（仅第一帧执行）
        if self.video_writer is None:
            height, width = rgb_img.shape[:2]  # 图像尺寸（H×W）
            fourcc = cv2.VideoWriter_fourcc(*'XVID')  # AVI编码器（兼容性好）
            self.video_writer = cv2.VideoWriter(self.video_path, fourcc, self.frame_rate, (width, height))
            if not self.video_writer.isOpened():
                self.get_logger().error("❌ 无法创建视频文件！请检查路径权限或编码器设置。")
                return
        
        # Step 9: 写入视频帧
        self.video_writer.write(rgb_img)
        self.frame_count += 1
        
        # Step 10: 日志输出（每30帧打印一次）
        if self.frame_count % 30 == 0:
            self.get_logger().info(f"📊 录制进度：已保存 {self.frame_count} 帧 | 检测到 {len(filtered_contours)} 个锥桶")

    def destroy_node(self):
        """节点销毁时释放资源"""
        if self.video_writer is not None:
            self.video_writer.release()
            self.get_logger().info(f"✅ 视频保存完成！共保存 {self.frame_count} 帧")
            self.get_logger().info(f"📂 视频路径：{self.video_path}")
        super().destroy_node()

def main(args=None):
    """节点主函数"""
    rclpy.init(args=args)
    node = ConeDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("⏹️ 用户终止程序")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()