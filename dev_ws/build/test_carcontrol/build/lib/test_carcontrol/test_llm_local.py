# 导入 requests 库，用于发送 HTTP 请求
import requests 
import base64
import os
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String
from std_msgs.msg import Int32
import cv2
import numpy as np
# 不再需要火山方舟的SDK，可以注释或删除
# from volcenginesdkarkruntime import Ark


class LLMNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.llm_pub = self.create_publisher(String, "/llm_output", 10)
        self.img_sub = self.create_subscription(CompressedImage, "/image", self.image_callback, 10)
        self.sign_sub = self.create_subscription(Int32, "/sign4return", self.sign_callback, 10)
        
        # --- [主要修改 1: Ollama 配置] ---
        # 设置Ollama API的地址
        self.ollama_api_url = "http://192.168.0.200:11434/api/generate" # 使用 /api/generate 端点
        # 设置你希望在Ollama中使用的模型名称, 例如 llava
        # 确保这个模型已经通过 `ollama run llava` 或 `ollama pull llava` 下载到本地
        self.model = "qwen2.5vl:7b" 
        # --- [修改结束] ---

        self.isoutput = 0

        # --- [主要修改 2: 移除云端SDK客户端] ---
        # self.client = Ark(...) 这部分代码不再需要，已删除
        # --- [修改结束] ---
        
        
    def sign_callback(self,msg):
        if msg.data == -1:
            self.isoutput = 1
    
    def image_callback(self,msg):
        if self.isoutput == 1:
            np_arr = np.frombuffer(msg.data, np.uint8)
            image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            
            # 将解码后的图像直接编码为PNG格式的二进制数据
            # 这样可以避免写入和读取磁盘文件，效率更高
            _, buffer = cv2.imencode('.png', image_np)
            self.base64_image = base64.b64encode(buffer).decode('utf-8')
            
            self.isoutput = 0

            # --- [主要修改 3: 构建并发送Ollama API请求] ---
            try:
                # 准备发送给Ollama API的JSON数据
                payload = {
                    "model": self.model,
                    "prompt": "图片中有一张立牌，请描述立牌上的人物特征和环境特征，要求简洁清晰",
                    "stream": False,  # 设置为 False 以便一次性接收完整响应
                    "images": [self.base64_image]
                }

                # 使用 requests 发送 POST 请求
                # 注意：Ollama API 的图片数据是直接放在 "images" 列表里的，不需要 "data:image/png;base64," 前缀
                print("正在向本地Ollama模型发送请求...")
                response = requests.post(self.ollama_api_url, json=payload, timeout=60) # 设置60秒超时
                
                # 检查HTTP响应状态
                response.raise_for_status()

                # 解析JSON响应并提取内容
                response_json = response.json()
                content = response_json.get("response", "未能获取到有效回复。")

                llm_msg = String()
                llm_msg.data = content.strip() # .strip() 用于移除可能存在的前后空白
                self.llm_pub.publish(llm_msg)
                print("Ollama模型的回复:")
                print(content)

            except requests.exceptions.RequestException as e:
                self.get_logger().error(f"请求Ollama API时发生网络错误: {e}")
            except Exception as e:
                self.get_logger().error(f"处理Ollama响应时发生未知错误: {e}")
            # --- [修改结束] ---


def main(args=None):
    rclpy.init(args=args)
    node = LLMNode("llmNode_ollama") # 建议给节点换个新名字以区分
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()