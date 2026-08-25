#需要函数
"""
pi.set_mode(pin, pigpio.OUTPUT)        把引脚设为输出
pi.set_servo_pulsewidth(pin, us)       控制角度(单位：微秒us)
pulse = 500 + (angle / 180) * (2500 - 500)
"""

import pigpio
import confing


class Servo:
    def __init__(self, pi):
        self.pi = pi                                    # 把连接对象存到实例上
        self.pi.set_mode(confing.SERVO_PWM, pigpio.OUTPUT)
        # 上电先把脉宽置 0，避免舵机猛地跳到某个角度
        self.pi.set_servo_pulsewidth(confing.SERVO_PWM, 0)

    def set_angle(self, angle):
        angle = max(0, min(90, angle))  # 限制角度在 0~90 度之间
        # 角度 -> 脉宽（0°=500us, 90°=1500us, 180°=2500us）
        pulse = confing.SERVO_MIN_PULSE_WIDTH + (angle / 180) * (confing.SERVO_MAX_PULSE_WIDTH - confing.SERVO_MIN_PULSE_WIDTH)
        self.pi.set_servo_pulsewidth(confing.SERVO_PWM, int(pulse))

    def off(self):
        self.pi.set_servo_pulsewidth(confing.SERVO_PWM, 0)
