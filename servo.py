#需要函数
"""
pi.set_PWM_frequency(pin, 1000)	    设 PWM 频率
pi.set_mode(pin, pigpio.OUTPUT)	    把引脚设为输出
pi.set_servo_pulsewidth(pin, us)   # 控制角度(单位：微秒us)
pulse = confing.SERVO_MIN_PULSE_WIDTH + (angle / 180) * (confing.SERVO_MAX_PULSE_WIDTH - confing.SERVO_MIN_PULSE_WIDTH)
"""


import pigpio
import confing



class Servo:
    def __init__(self, pi):
        self.pi = pi
        self.pi.set_mode(confing.SERVO_PWM, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(confing.SERVO_PWM, confing.SERVO_FREQUENCY)
        self.pi.set_servo_pulsewidth(confing.SERVO_PWM, 0)  # 初始化舵机为0度

    def set_angle(self, angle):
        angle = max(0, min(90, angle)) # 限制角度在0-90度之间
        #角度转换成脉宽
        pulse = confing.SERVO_MIN_PULSE_WIDTH + (angle / 180) * (confing.SERVO_MAX_PULSE_WIDTH - confing.SERVO_MIN_PULSE_WIDTH)
        #设置舵机角度
        self.pi.set_servo_pulsewidth(confing.SERVO_PWM, pulse)

    def off(self):
        #关闭舵机
        self.pi.set_servo_pulsewidth(confing.SERVO_PWM, 0)

