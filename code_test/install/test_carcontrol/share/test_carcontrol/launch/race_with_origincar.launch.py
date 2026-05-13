#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""先启动 origincar 底盘 bringup，再启动 race_bringup（比赛算法节点）。

需在主工作空间已编译 origincar_base，且已 source 主仓 install（默认 /userdata/dev_ws/install，见 start_race.sh 的 DEV_WS_ROOT underlay）。
若底盘已在别处启动，请使用 race_bringup.launch.py，勿重复启动本文件。
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    origincar_share = get_package_share_directory('origincar_base')
    origincar_bringup = PythonLaunchDescriptionSource(
        os.path.join(origincar_share, 'launch', 'origincar_bringup.launch.py')
    )

    test_share = get_package_share_directory('test_carcontrol')
    race_bringup = PythonLaunchDescriptionSource(
        os.path.join(test_share, 'launch', 'race_bringup.launch.py')
    )

    return LaunchDescription(
        [
            IncludeLaunchDescription(origincar_bringup),
            IncludeLaunchDescription(race_bringup),
        ]
    )
