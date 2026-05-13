import base64
import os
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from std_msgs.msg import String
from std_msgs.msg import Int32
import cv2
import numpy as np
import time
from cv_bridge import CvBridge
# 通过 pip install volcengine-python-sdk[ark] 安装方舟SDK
from volcenginesdkarkruntime import Ark

from test_carcontrol.code_test_paths import output_dir
from test_carcontrol.ros_qos import SIGN4RETURN_QOS


class LLMNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.bridge = CvBridge()
        self.llm_pub = self.create_publisher(String, "/llm_output", 10)
        self.img_sub = self.create_subscription(Image, "/aurora/rgb/image_raw", self.image_callback, 10)
        # self.img_sub = self.create_subscription(CompressedImage, "/image", self.image_callback, 10)
        self.sign_sub = self.create_subscription(
            Int32, "/sign4return", self.sign_callback, SIGN4RETURN_QOS
        )
        self.model = "doubao-1.5-vision-pro-32k-250115"
        self.isoutput = 0
        # self.output_done = 0
        # 初始化一个Client对象，从环境变量中获取API Key
        self.client = Ark(
            api_key='68a87054-8182-4e8c-acb2-9056e4c85c20',# os.getenv('ARK_API_KEY'),
            )
        
        
    def sign_callback(self,msg):
        if msg.data == -1:
            self.isoutput = 1
    
    def image_callback(self,msg):
        if self.isoutput == 1:
            image_np = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # np_arr = np.frombuffer(msg.data, np.uint8)
            # 使用OpenCV解码MJPG数据
            # image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            # _, buffer = cv2.imencode('.png', image_np)
            # self.base64_image = base64.b64encode(buffer).decode('utf-8')
            str = time.strftime("%m%d_%H%M%S", time.localtime())
            image_path = str(output_dir("llm_snap") / f"{str}.png")
            cv2.imwrite(image_path,image_np)
            self.isoutput = 0
            with open(image_path, "rb") as image_file:
                self.base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            #base64_image = base64.b64encode(image_np).decode('utf-8')
            # 定义方法将指定路径图片转为Base64编码
            #def encode_image(image_path):
            #  with open(image_path, "rb") as image_file:
            #    return base64.b64encode(image_file.read()).decode('utf-8')
            
            # 需要传给大模型的图片
            #image_path = "/root/PictureToText/doubaoTest/1.png"
            
            # 将图片转为Base64编码
            #base64_image = encode_image(image_path)
            
            self.response = self.client.chat.completions.create(
              # 替换 <Model> 为模型的Model ID
              model = self.model,
              messages=[
                {
                  "role": "user",
                  "content": [
                    {
                      "type": "text",
                      "text": "图片中有一张立牌，请描述立牌上图片的内容，要求简洁清晰",
                    },
                    {
                      "type": "image_url",
                      "image_url": {
                      # 需要注意：传入Base64编码前需要增加前缀 data:image/{图片格式};base64,{Base64编码}：
                      # PNG图片："url":  f"data:image/png;base64,{base64_image}"
                      # JPEG图片："url":  f"data:image/jpeg;base64,{base64_image}"
                      # WEBP图片："url":  f"data:image/webp;base64,{base64_image}"
                        "url":  f"data:image/png;base64,{self.base64_image}"
                      },
                    },
                  ],
                }
              ],
            )
            llm_msg = String()
            llm_msg.data = self.response.choices[0].message.content
            self.llm_pub.publish(llm_msg)
            print(self.response.choices[0].message.content)

def main(args=None):
    rclpy.init(args=args)
    node = LLMNode("llmNode")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

