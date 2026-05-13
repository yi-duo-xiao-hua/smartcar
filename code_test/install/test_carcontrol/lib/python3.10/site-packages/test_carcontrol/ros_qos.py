"""本栈内话题的统一 QoS，避免与其它节点在 DURABILITY 等策略上不一致而产生告警。"""
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy

# /sign4return：若发布端为 VOLATILE，而订阅端（含其它包）请求 TRANSIENT_LOCAL，会触发 DURABILITY 不兼容告警。
# 发布端使用 TRANSIENT_LOCAL 可与 VOLATILE 订阅端兼容，也可满足需要“读到最近一条”的订阅端。
SIGN4RETURN_QOS = QoSProfile(
    depth=10,
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
)

# /cmd_vel：部分底盘、Foxglove、桥接节点以 TRANSIENT_LOCAL 订阅；默认 VOLATILE 发布会触发 DURABILITY 不兼容。
CMD_VEL_QOS = QoSProfile(
    depth=10,
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
)
