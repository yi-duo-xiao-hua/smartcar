#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""仅订阅 dnn_node 发布的 YOLO 检测结果（默认 hobot_dnn_detection），在终端打印类别与框。"""

import time

import rclpy
from rclpy.node import Node
from ai_msgs.msg import PerceptionTargets


class YoloDetectionEcho(Node):
    def __init__(self):
        super().__init__('yolo_detection_echo')
        self.declare_parameter('topic', 'hobot_dnn_detection')
        self.declare_parameter('echo_hz', 4.0)

        topic = self.get_parameter('topic').get_parameter_value().string_value
        hz = float(self.get_parameter('echo_hz').get_parameter_value().double_value)
        self._min_interval = 1.0 / max(0.5, hz)
        self._last_echo = 0.0
        self._last_summary = None

        self.create_subscription(PerceptionTargets, topic, self._cb, 10)
        self.get_logger().info(
            f'已订阅 YOLO: topic={topic!r}, 类型=ai_msgs/PerceptionTargets, '
            f'节流≈{hz:.1f} Hz（摘要变化时立即打印）'
        )

    def _cb(self, msg: PerceptionTargets):
        parts = []
        for t in msg.targets:
            if not t.rois:
                parts.append(f'{t.type}(无框)')
                continue
            r = t.rois[0].rect
            parts.append(
                f'{t.type}[xywh=({r.x_offset},{r.y_offset},{r.width},{r.height})]'
            )
        summary = f'n={len(msg.targets)} ' + (' | '.join(parts) if parts else '(画面中无检测框)')

        now = time.time()
        changed = summary != self._last_summary
        if not changed and (now - self._last_echo) < self._min_interval:
            return
        self._last_summary = summary
        self._last_echo = now
        self.get_logger().info(summary)


def main(args=None):
    rclpy.init(args=args)
    node = YoloDetectionEcho()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
