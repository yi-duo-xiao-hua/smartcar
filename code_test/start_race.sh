#!/usr/bin/env bash
# =============================================================================
# code_test 一键启动（比赛用 race_bringup）
# 独立工作空间根目录：/userdata/code_test（可选叠加主仓 dev_ws 的 install）
# =============================================================================
# 用法：
#   cd /userdata/code_test
#   chmod +x start_race.sh   # 仅需一次
#   ./start_race.sh
# 可选参数传给 launch，例如关闭图像压缩节点：
#   ./start_race.sh use_image_compress:=false
#
# 同时启动 origincar 底盘（origincar_bringup）+ 比赛节点（勿与已运行的底盘重复）：
#   WITH_ORIGINCAR=1 ./start_race.sh
#
# 首次建议在主工作空间已编译 origincar 后，安装本包声明的依赖：
#   cd /userdata/code_test && rosdep install --from-paths src/test_carcontrol -y
#   （另需系统包 libzbar0：sudo apt install -y libzbar0）
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Python 节点：配置在 src/test_carcontrol/config/，日志 log/，产出 output/
export CODE_TEST_ROOT="$SCRIPT_DIR"

# 主工作空间 install（origincar_msg 等）；独立部署时默认 /userdata/dev_ws，可用 DEV_WS_ROOT 覆盖
: "${DEV_WS_ROOT:=/userdata/dev_ws}"
UNDERLAY_SETUP="${DEV_WS_ROOT}/install/setup.bash"

# ----- ROS 2 发行版 -----
if [[ -z "${ROS_DISTRO:-}" ]]; then
  if [[ -f /opt/ros/humble/setup.bash ]]; then
    set +u
    # shellcheck source=/dev/null
    source /opt/ros/humble/setup.bash
    set -u
  elif [[ -f /opt/ros/jazzy/setup.bash ]]; then
    set +u
    # shellcheck source=/dev/null
    source /opt/ros/jazzy/setup.bash
    set -u
  elif [[ -f /opt/ros/foxy/setup.bash ]]; then
    set +u
    # shellcheck source=/dev/null
    source /opt/ros/foxy/setup.bash
    set -u
  else
    echo "未检测到 ROS_DISTRO，且未找到 /opt/ros/humble、jazzy 或 foxy。" >&2
    echo "请先: source /opt/ros/<发行版>/setup.bash" >&2
    exit 1
  fi
fi

# ----- 主工作空间 underlay（可选）-----
if [[ -f "$UNDERLAY_SETUP" ]]; then
  echo "[start_race] 加载 underlay: $UNDERLAY_SETUP"
  set +u
  # shellcheck source=/dev/null
  source "$UNDERLAY_SETUP"
  set -u
else
  echo "[start_race] 未找到 $UNDERLAY_SETUP（若无 origincar_msg 等依赖可忽略）" >&2
fi

# ----- 编译本工作空间（若尚未 install）-----
if [[ ! -f install/setup.bash ]]; then
  echo "[start_race] 未找到 install/setup.bash，正在 colcon build ..."
  colcon build --symlink-install
fi

# ament/colcon 的 setup 在 set -u 下会触发未定义变量，source 时临时关闭 nounset
set +u
# shellcheck source=/dev/null
source install/setup.bash
set -u

echo "[start_race] CODE_TEST_ROOT=$CODE_TEST_ROOT"

LAUNCH_FILE="race_bringup.launch.py"
if [[ "${WITH_ORIGINCAR:-0}" == "1" ]]; then
  if [[ ! -f "$UNDERLAY_SETUP" ]]; then
    echo "[start_race] 错误: WITH_ORIGINCAR=1 需要已编译的主工作空间 underlay：" >&2
    echo "  $UNDERLAY_SETUP" >&2
    echo "请先在 ${DEV_WS_ROOT:-/userdata/dev_ws} 执行 colcon build，再运行本脚本。" >&2
    exit 1
  fi
  LAUNCH_FILE="race_with_origincar.launch.py"
  echo "[start_race] WITH_ORIGINCAR=1 → 启动 origincar_bringup + race_bringup"
fi

exec ros2 launch test_carcontrol "$LAUNCH_FILE" "$@"
