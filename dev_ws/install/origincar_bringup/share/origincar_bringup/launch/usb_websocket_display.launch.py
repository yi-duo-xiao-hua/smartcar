import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.conditions import IfCondition
from launch.substitutions import TextSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory, get_package_prefix

def generate_launch_description():
    # Copy config files
    dnn_node_example_path = os.path.join(get_package_prefix('dnn_node_example'), "lib/dnn_node_example")
    os.system(f"cp -r {dnn_node_example_path}/config .")

    # Declare launch arguments
    launch_args = [
        # 默认：车载 YOLOv5x（见 yolov5x_car_workconfig.json）；可 dnn_example_config_file:=... 覆盖为 v8 等。
        DeclareLaunchArgument(
            "dnn_example_config_file",
            default_value=TextSubstitution(text="/userdata/dev_ws/config/yolov5x_car_workconfig.json"),
        ),
        DeclareLaunchArgument("dnn_example_dump_render_img", default_value=TextSubstitution(text="0")),
        # USB 出图 640x480；模型若为 640 输入由 DNN 内预处理对齐（若 bin 为 672 请改为 672）
        DeclareLaunchArgument("dnn_example_image_width", default_value=TextSubstitution(text="640")),
        DeclareLaunchArgument("dnn_example_image_height", default_value=TextSubstitution(text="640")),
        DeclareLaunchArgument("dnn_example_msg_pub_topic_name", default_value=TextSubstitution(text="hobot_dnn_detection")),
        DeclareLaunchArgument('device', default_value='/dev/video0', description='usb camera device'),
        # 与 DNN 同时订 /hbmem_img 时，零拷贝 loan 易触发 SIGSEGV；默认关 loan，仍异常时可 false 关掉 Nv122BGR
        DeclareLaunchArgument(
            'enable_nv122_view',
            default_value='true',
            description='若 true 启动 Nv122BGR（订 /hbmem_img）；仅调 DNN 时可设为 false',
        ),
    ]

    # Include launch descriptions
    usb_node = IncludeLaunchDescription(PythonLaunchDescriptionSource(get_package_share_directory('hobot_usb_cam') + '/launch/hobot_usb_cam.launch.py'),
                                       launch_arguments={'usb_image_width': '640', 'usb_image_height': '480',
                                                         'usb_video_device': LaunchConfiguration('device')}.items())

    nv12_codec_node = IncludeLaunchDescription(PythonLaunchDescriptionSource(get_package_share_directory('hobot_codec') + '/launch/hobot_codec_decode.launch.py'),
                                               launch_arguments={'codec_in_mode': 'ros', 'codec_out_mode': 'shared_mem',
                                                                 'codec_sub_topic': '/image', 'codec_pub_topic': '/hbmem_img'}.items())

    jpeg_codec_node = IncludeLaunchDescription(PythonLaunchDescriptionSource(get_package_share_directory('hobot_codec') + '/launch/hobot_codec_encode.launch.py'),
                                               launch_arguments={'codec_in_mode': 'shared_mem', 'codec_out_mode': 'ros',
                                                                 'codec_sub_topic': '/hbmem_img', 'codec_pub_topic': '/image'}.items())

    # 调试 YOLO/编解码时可暂时关闭 websocket，减轻反压与缓存（确认无问题后再恢复）。
    # web_node = IncludeLaunchDescription(PythonLaunchDescriptionSource(get_package_share_directory('websocket') + '/launch/websocket.launch.py'),
    #                                     launch_arguments={'websocket_image_topic': '/image', 'websocket_image_type': 'mjpeg',
    #                                                       'websocket_smart_topic': LaunchConfiguration("dnn_example_msg_pub_topic_name")}.items())

    # Algorithm node
    dnn_node_example_node = Node(
        package='dnn_node_example',
        executable='example',
        output='screen',
        parameters=[
            {"config_file": LaunchConfiguration('dnn_example_config_file')},
            {"dump_render_img": LaunchConfiguration('dnn_example_dump_render_img')},
            {"feed_type": 1},
            # 0：DNN 订阅 /image（JPEG）；1：订阅 /hbmem_img（NV12）。当前按需求用 /image。
            {"is_shared_mem_sub": 0},
            {"msg_pub_topic_name": LaunchConfiguration("dnn_example_msg_pub_topic_name")}
        ],
        arguments=['--ros-args', '--log-level', 'warn']
    )
    image_transport_node = Node(
        package='utils',
        executable='image_transport_node',
        output='screen',
        arguments=['--ros-args', '--log-level', 'info'],
        condition=IfCondition(LaunchConfiguration('enable_nv122_view')),
    )
    return LaunchDescription([
        # 避免 hbmem 多订阅 + loan 回调导致段错误（日志曾出现 Loaned messages 警告后 codec/DNN -11）
        SetEnvironmentVariable('ROS_DISABLE_LOANED_MESSAGES', '1'),
    ] + launch_args + [
        usb_node,
        nv12_codec_node,
        dnn_node_example_node,
        # web_node,
        image_transport_node,
    ])
