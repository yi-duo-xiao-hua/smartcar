#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一键启动 README 中列出的比赛用节点（test_carcontrol）。"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                'use_image_compress',
                default_value='true',
                description='若为 false 则不启动图像压缩节点 image_com',
            ),
            Node(
                package='test_carcontrol',
                executable='new_resnet',
                name='new_resnet',
                output='screen',
            ),
            Node(
                package='test_carcontrol',
                executable='new_yolo',
                name='new_yolo',
                output='screen',
            ),
            Node(
                package='test_carcontrol',
                executable='test_qrcode',
                name='test_qrcode',
                output='screen',
            ),
            Node(
                package='test_carcontrol',
                executable='test_llm_local',
                name='test_llm_local',
                output='screen',
            ),
            Node(
                package='test_carcontrol',
                executable='new_ctrlpub',
                name='new_ctrlpub',
                output='screen',
            ),
            Node(
                package='test_carcontrol',
                executable='image_com',
                name='image_com',
                output='screen',
                condition=IfCondition(LaunchConfiguration('use_image_compress')),
            ),
        ]
    )
