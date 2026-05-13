"""解析 code_test 工作空间、安装前缀下的 share 目录及可写运行时目录。"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def _package_share() -> Path | None:
    """已安装包时的 share/test_carcontrol（含 config、可选 model）。"""
    try:
        from ament_index_python.packages import get_package_share_directory

        return Path(get_package_share_directory("test_carcontrol"))
    except Exception:
        return None


def _walk_dev_code_test_root(start: Path) -> Path | None:
    """从源码或 symlink-install 的 __file__ 向上查找 code_test 根目录。"""
    for ancestor in start.parents:
        marker = ancestor / "src" / "test_carcontrol" / "config" / "config_new_resnet.yaml"
        if marker.is_file():
            return ancestor
    return None


def get_code_test_root() -> Path:
    """可写根目录：日志、output；也可拼接源码里的相对模型路径。

    优先级：CODE_TEST_ROOT → 源码树探测 → ~/.code_test（仅运行时已安装包且无源码时）。
    """
    env = os.environ.get("CODE_TEST_ROOT", "").strip()
    if env:
        return Path(env).resolve()

    here = Path(__file__).resolve()
    dev = _walk_dev_code_test_root(here)
    if dev is not None:
        return dev

    # 仅安装了 deb/site-packages、未设置环境变量：使用用户目录，避免找不到路径
    fallback = Path.home() / ".code_test"
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback


def test_carcontrol_config_dir() -> Path:
    """YAML / dnn 描述文件目录：优先源码树，否则 install/share 下的 config。"""
    here = Path(__file__).resolve()
    dev = _walk_dev_code_test_root(here)
    if dev is not None:
        p = dev / "src" / "test_carcontrol" / "config"
        if p.is_dir():
            return p

    share = _package_share()
    if share is not None:
        cfg = share / "config"
        if cfg.is_dir():
            return cfg

    raise RuntimeError(
        "未找到配置文件目录。请任选其一：\n"
        "  export CODE_TEST_ROOT=/userdata/code_test\n"
        "或在对应工作空间重新编译 test_carcontrol（确保 setup.py 安装了 config/）：\n"
        "  cd /userdata/code_test && colcon build --symlink-install --packages-select test_carcontrol"
    )


def config_path(name: str) -> Path:
    """配置文件名，例如 config_new_resnet.yaml、detect.prototxt。"""
    return test_carcontrol_config_dir() / name


def output_dir(*parts: str) -> Path:
    """可写输出目录：位于 get_code_test_root()/output/..."""
    p = get_code_test_root().joinpath("output", *parts)
    p.mkdir(parents=True, exist_ok=True)
    return p


def resolve_model_file(param_rel: str) -> Path:
    """解析 YAML 中的 model 路径：绝对路径、工作空间相对路径，或 install/share/.../model/ 下同名文件。"""
    mp = Path(param_rel)
    if mp.is_file():
        return mp.resolve()

    root = get_code_test_root()
    cand = root / param_rel
    if cand.is_file():
        return cand.resolve()

    share = _package_share()
    if share is not None:
        alt = share / "model" / mp.name
        if alt.is_file():
            return alt.resolve()

    # 常见布局：模型与源码并列 model/
    dev = _walk_dev_code_test_root(Path(__file__).resolve())
    if dev is not None:
        alt2 = dev / "src" / "test_carcontrol" / "model" / mp.name
        if alt2.is_file():
            return alt2.resolve()

    return cand


def default_resnet_nv12_model() -> Path:
    """new_pidctrl / test_car_pid 默认 ResNet bin。"""
    share = _package_share()
    if share is not None:
        p = share / "model" / "resnet18_224x224_nv12.bin"
        if p.is_file():
            return p
    return get_code_test_root() / "src" / "test_carcontrol" / "model" / "resnet18_224x224_nv12.bin"
