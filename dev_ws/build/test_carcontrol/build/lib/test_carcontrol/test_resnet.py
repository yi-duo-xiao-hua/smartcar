import cv2
import numpy as np
from hobot_dnn import pyeasy_dnn as dnn

def convert_bgr_to_nv12(cv_image):
    yuv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2YUV)
    y_channel = yuv_image[:, :, 0]
    u_channel = yuv_image[::2, ::2, 1]
    v_channel = yuv_image[::2, ::2, 2]
    uv_channel = np.empty((u_channel.shape[0], u_channel.shape[1] * 2), dtype=u_channel.dtype)
    uv_channel[:, ::2] = u_channel
    uv_channel[:, 1::2] = v_channel
    nv12_image = np.concatenate((y_channel.flatten(), uv_channel.flatten()))
    return nv12_image

def process_frame(cv_image, models, original_width, original_height):
    # 将图像缩放到模型期望的尺寸
    cv_image_resized = cv2.resize(cv_image, (224, 224), interpolation=cv2.INTER_LINEAR)
    nv12_image = convert_bgr_to_nv12(cv_image_resized)
    
    # 使用模型进行推理
    outputs = models[0].forward(np.frombuffer(nv12_image, dtype=np.uint8))
    outputs = outputs[0].buffer
    
    # 假设模型输出是在224x224图像上的比例坐标
    x_ratio, y_ratio = outputs[0][0][0][0], outputs[0][1][0][0]
    
    # 将比例坐标转换为原始视频帧的像素坐标
    x_pixel = int(x_ratio * original_width)
    y_pixel = int(y_ratio * original_height)
    
    return x_pixel, y_pixel

def main():
    models = dnn.load('/root/resnet18_224x224_nv12.bin')
    cap = cv2.VideoCapture("/root/test.avi")

    # 确定视频编解码器和创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('test_output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        x, y = process_frame(frame, models,640,480)
        cv2.circle(frame, (x, y), radius=5, color=(0, 0, 255), thickness=-1)

        # 写入帧到输出文件
        out.write(frame)

        # cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()  # 释放VideoWriter对象
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()