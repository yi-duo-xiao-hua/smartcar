# Origincar 使用说明

## 编译

```bash
# 默认工作空间 /userdata/dev_ws/
cd /userdata/dev_ws/
colcon build --symlink-install
```

## 底盘和控制

启动底盘
```bash
ros2 launch origincar_base origincar_bringup.launch.py
```

启动键盘控制
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
以下按键进行控制
```
   u    i    o
   j    k    l
   m    ,    .
```
键盘节点会发布 速度消息 到 /cmd_vel 话题，底盘节点订阅速度消息实现键盘控制

## USB 相机驱动与图像可视化
```bash
ros2 launch origincar_bringup usb_websocket_display.launch.py
```
运行成功后，在同一网络的PC端，打开浏览器，输入 http://IP:8000，选择“web展示端”，即可查看图像和算法效果，IP为OriginBot的IP地址。

## 深度相机驱动与图像可视化
启动相机

```bash
ros2 launch deptrum-ros-driver-aurora930 aurora930_launch.py

```
启动rqt_image_view
```
ros2 run rqt_image_view rqt_image_view
```

## 比赛示例代码一键启动（`code_test`）

参考目录：**`src/code_test`**（与 `origincar` 同级，位于 `dev_ws/src/` 下）。其中的 `start_race.sh` 会在 **`code_test` 作为独立 colcon 工作空间** 下：加载 ROS 2、**加载上一级 `dev_ws/install`（underlay，提供 `origincar_msg`、`origincar_base` 等）**、若尚无 `install/setup.bash` 则 `colcon build --symlink-install`，再启动比赛 launch。

- **仅比赛节点**：`./start_race.sh` → `race_bringup.launch.py`（需自行先起底盘/相机时可按下文操作）。
- **底盘 + 比赛一并起**（勿与已在运行的 `origincar_bringup` 重复）：`WITH_ORIGINCAR=1 ./start_race.sh` → `race_with_origincar.launch.py`（内含 `origincar_base` 的 `origincar_bringup`）。

### 一键命令（推荐）

在已安装 ROS 2 的小车或开发机上执行：

```bash
cd /userdata/dev_ws/src/code_test
./start_race.sh
```

若脚本尚无执行权限，可先执行一次 `chmod +x start_race.sh`，或直接用：

```bash
bash /userdata/dev_ws/src/code_test/start_race.sh
```

### 与本文前面章节的关系

- **底盘**：若控制类节点依赖 `/cmd_vel` 等，请先按上文 **「启动底盘」** 运行 `origincar_bringup`（或你实际使用的底盘 bringup）。
- **相机 / 图像**：若 ResNet、YOLO、图像压缩等依赖相机话题，请先按 **USB 相机** 或 **深度相机** 章节启动对应驱动与可视化（按需选用）。

### 本脚本实际拉起的节点（`race_bringup.launch.py`）

会并行启动：`new_resnet`、`new_yolo`、`test_qrcode`、`test_llm_local`、`new_ctrlpub`，以及默认开启的图像压缩节点 `image_com`（可通过参数关闭）。

### 可选启动参数

例如关闭图像压缩节点：

```bash
./start_race.sh use_image_compress:=false
```

其余 `ros2 launch` 支持的参数写法均可追加在 `./start_race.sh` 之后。

### 依赖说明（避免 ModuleNotFoundError）

`test_carcontrol` 的 **`package.xml`** 已声明 `python3-requests`、`python3-shapely`、`python3-pyzbar` 及 **`origincar_msg` / `origincar_base`** 等；在主工作空间根执行一次 **rosdep** 即可拉齐大部分依赖：

```bash
cd /userdata/dev_ws
rosdep install --from-paths src/code_test/src/test_carcontrol -y
sudo apt install -y libzbar0
```

亦可手动：`sudo apt install -y python3-requests python3-shapely python3-pyzbar libzbar0`，或 `pip3 install -r /userdata/dev_ws/src/code_test/requirements-race.txt`。

另：`new_resnet` 使用 **`hobot_dnn`** 与 **`.bin` 模型文件**（见 `code_test/src/test_carcontrol/model/`），仅在对应 RDK/地平线环境且模型存在时才能完整跑通。算法相关 **YAML 配置** 位于 **`code_test/src/test_carcontrol/config/`**。
