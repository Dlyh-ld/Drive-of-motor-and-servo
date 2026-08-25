# -*- coding: utf-8 -*-
"""
test_decide.py —— 练习：用"假 dets"测试 decide() 逻辑（不用摄像头）
"""

# 第 1 部分：造一个假的 dets，模拟 YOLO 检测结果
# dets 是列表，每个元素是一个字典，描述一个目标
dets = [
    {"cls": "green_cube", "cx": 480.0, "cy": 240.0, "conf": 0.93},
]


def decide(dets):
    """输入 dets（YOLO 结果），返回 (左轮速度, 右轮速度)"""
    # 没看到任何目标 -> 停下
    if not dets:
        return 0, 0

    # 从列表里挑出"置信度最高"的那个目标
    target = max(dets, key=lambda d: d["conf"])
    cx = target["cx"]          # 目标中心的横坐标

    # 画面宽 640，正中心是 320
    error = cx - 320           # 目标偏右 -> 正数；偏左 -> 负数
    Kp = 0.2                   # 比例系数（转向的"力度"）
    diff = Kp * error          # 差速

    base = 30                  # 基础前进速度
    left = base + diff         # 左轮速度
    right = base - diff        # 右轮速度
    return left, right


# 第 2 部分：测试
left, right = decide(dets)
print(f"目标 cx={dets[0]['cx']}  ->  左轮 {left}, 右轮 {right}")
