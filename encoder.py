#需要的函数
"""
pi.read(pin)	                                  #读引脚当前电平，返回 0 或 1
pi.set_mode(pin_a, pigpio.INPUT)                  # A、B 都设为输入
pi.set_pull_up_down(pin_a, pigpio.PUD_UP)         # 上拉，防止悬空乱跳
pi.callback(pin_a, pigpio.EITHER_EDGE, 回调函数)   # A 上升/下降沿都触发
"""



import pigpio


class Encoder:
    def __init__(self, pi, pin_a, pin_b):
        self.pi = pi
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.count = 0  # 初始化计数器

        # 设置引脚模式和上拉电阻
        self.pi.set_mode(pin_a, pigpio.INPUT)
        self.pi.set_mode(pin_b, pigpio.INPUT)
        self.pi.set_pull_up_down(pin_a, pigpio.PUD_UP)
        self.pi.set_pull_up_down(pin_b, pigpio.PUD_UP)
        self._cb = self.pi.callback(self.pin_a, pigpio.EITHER_EDGE, self.callback)

    def callback(self, gpio, level, tick):
        # 读取 A、B 引脚的电平状态
        a = self.pi.read(self.pin_a)
        b = self.pi.read(self.pin_b)

        # 根据 A、B 的状态判断旋转方向并更新计数
        if a == b:
            self.count += 1  # 顺时针旋转
        else:
            self.count -= 1  # 逆时针旋转

    def reset_count(self):
        self.count = 0  # 重置计数器


