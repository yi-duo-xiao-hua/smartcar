"""解析 code_test 工作空间根目录与包内配置路径（不依赖机器上的 /home/...）。"""
from __future__ import annotations

import os
from pathlib import Path


def get_code_test_root() -> Path:
    """优先读环境变量 CODE_TEST_ROOT（由 start_race.sh 设置），否则向上查找 code_test 根目录。"""
    env = os.environ.get("CODE_TEST_ROOT", "").strip()
    if env:
        return Path(env).resolve()
    here = Path(__file__).resolve()
    for ancestor in here.parents:
        marker = ancestor / "src" / "test_carcontrol" / "config" / "config_new_resnet.yaml"
        if marker.is_file():
            return ancestor
    raise RuntimeError(
        "未找到 code_test 根目录。请用 code_test/start_race.sh 启动，或先执行：\n"
        "  export CODE_TEST_ROOT=/path/to/origincar/code_test"
    )


def test_carcontrol_config_dir() -> Path:
    """所有 YAML / OpenCV dnn 描述文件统一放在源码树：src/test_carcontrol/config/"""
    return get_code_test_root() / "src" / "test_carcontrol" / "config"


def config_path(name: str) -> Path:
    """配置文件名，例如 config_new_resnet.yaml、detect.prototxt。"""
    return test_carcontrol_config_dir() / name


def output_dir(*parts: str) -> Path:
    """code_test 下的输出目录（自动创建），例如 output_dir('depth')。"""
    p = get_code_test_root().joinpath("output", *parts)
    p.mkdir(parents=True, exist_ok=True)
    return p


def default_resnet_nv12_model() -> Path:
    """与 new_pidctrl / test_car_pid 中历史默认名一致，相对 code_test 根。"""
    return get_code_test_root() / "src" / "test_carcontrol" / "model" / "resnet18_224x224_nv12.bin"
