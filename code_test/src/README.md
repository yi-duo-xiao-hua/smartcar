# code_test 工作空间说明

本目录是 **独立的 ROS 2 colcon 工作空间**，根路径为 **`/userdata/code_test`**，包含比赛/算法实验包：`test_carcontrol`、`test_interface`、`test_node`。

## 目录约定

| 路径 | 用途 |
|------|------|
| `src/test_carcontrol/config/` | 所有 YAML 与 OpenCV dnn 描述文件 |
| `src/test_carcontrol/model/` | `.bin` 等模型文件（需自备） |
| `log/`、`output/` | 运行日志与录像/抓图输出（运行时自动创建） |

环境变量 **`CODE_TEST_ROOT`** 指向本工作空间根目录（即 `code_test/`）；仓库根目录下的 **`start_race.sh`** 会自动设置。

## 与 `origincar`、主工作空间的关系

- **`/userdata/dev_ws/`**（或其它路径）：可选的主 colcon 工作空间，编译 `origincar_*`、`origincar_msg` 等。
- **`start_race.sh`** 默认会尝试 **`source ${DEV_WS_ROOT:-/userdata/dev_ws}/install/setup.bash`**，再 **`source` 本目录的 `install/setup.bash`**，这样节点可使用 **`origincar_msg`** 等主仓包。可通过环境变量 **`DEV_WS_ROOT`** 指定主工作空间根目录。

一键启动：在 **`code_test/`** 下执行 **`./start_race.sh`**。

## 日常使用 ROS 2 命令

在本工作空间编译后，新开终端需先加载环境：

```bash
source /userdata/code_test/install/setup.bash
```

然后再执行 `ros2 run`、`ros2 launch` 等。
