#需要用到的函数
"""
pi.set_mode(pin, pigpio.OUTPUT)	    把引脚设为输出
pi.write(pin, 1) / pi.write(pin, 0)	输出高/低电平
pi.set_PWM_range(pin, 100)	        把占空比范围设成 0~100
pi.set_PWM_frequency(pin, 1000)	    设 PWM 频率
pi.set_PWM_dutycycle(pin, 50)	    设占空比（0~100） #决定速度快慢
"""

import pigpio
import confing



class Motor:
    def __init__(self, pi, pwm_pin, ain1_pin, ain2_pin):
        self.pi = pi
        self.pwm_pin = pwm_pin
        self.ain1_pin = ain1_pin
        self.ain2_pin = ain2_pin

        # 设置引脚模式为输出
        self.pi.set_mode(self.pwm_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.ain1_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.ain2_pin, pigpio.OUTPUT)

        # 设置PWM频率和占空比范围
        self.pi.set_PWM_frequency(self.pwm_pin, confing.MOTOR_FREQUENCY)
        self.pi.set_PWM_range(self.pwm_pin, confing.MOTOR_MAX_DUTY)

    def set_speed(self, speed):
        if speed > 0:
            # 前进
            self.pi.write(self.ain1_pin, 1)
            self.pi.write(self.ain2_pin, 0)
        elif speed < 0:
            # 后退
            self.pi.write(self.ain1_pin, 0)
            self.pi.write(self.ain2_pin, 1)
        else:
            self.coast()
            return

        # 设置占空比
        duty_cycle = int(min(abs(speed), confing.MOTOR_MAX_DUTY))
        self.pi.set_PWM_dutycycle(self.pwm_pin, duty_cycle)

    def brake(self):
        # 刹车
        self.pi.write(self.ain1_pin, 1)
        self.pi.write(self.ain2_pin, 1)
        self.pi.set_PWM_dutycycle(self.pwm_pin, 0)

    def coast(self):
        # 停止
        self.pi.write(self.ain1_pin, 0)
        self.pi.write(self.ain2_pin, 0)
        self.pi.set_PWM_dutycycle(self.pwm_pin, 0)

    

