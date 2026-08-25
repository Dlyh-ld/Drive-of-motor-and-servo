"""
该文件定义了小车的硬件接口配置
命名都以大写加下划线的形式定义
"""



#车轮信息
WHEEL_DIAMETER = None    #车轮直径mm
WHEEL_BASE = None    #车轮间距mm

#电机型号和参数
MOTOR_DRIVER = "TB6612"
MOTOR_FREQUENCY = 1000    #电机频率
MOTOR_MAX_DUTY = 100  #电机最大占空比
MOTOR_STBY = 25    #电机使能引脚

#定义左轮的PWM和AIN1、AIN2的GPIO口
WHEEL_LEFT_PWM = 12
WHEEL_LEFT_AIN1 = 5
WHEEL_LEFT_AIN2 = 6

#定义右轮的PWM和AIN1、AIN2的GPIO口
WHEEL_RIGHT_PWM = 18
WHEEL_RIGHT_AIN1 = 23
WHEEL_RIGHT_AIN2 = 24

#左编码器A、B相
ENCODER_LEFT_A = 16
ENCODER_LEFT_B = 20
#右编码器A、B相
ENCODER_RIGHT_A = 26
ENCODER_RIGHT_B = 21



#定义小车舵机驱动的GPIO口
SERVO_PWM = 17
SERVO_FREQUENCY = 50    #舵机频率
SERVO_MAX_PULSE_WIDTH = 2500    #舵机最大脉宽
SERVO_MIN_PULSE_WIDTH = 500     #舵机最小脉宽


#------------------------------------------------------------------------------------
# 编码器机械参数（航向计算用）
ENCODER_PPR = 13          # TODO: 编码器盘每转脉冲数(线数)，查型号或标定
ENCODER_GEAR_RATIO = 30   # TODO: 减速比 = 电机转数 / 轮子转数

# 舵机角度范围
SERVO_MIN_ANGLE = 0
SERVO_MAX_ANGLE = 90

# 控制参数
CONTROL_LOOP_HZ = 50      # 每秒执行几次 PID（50 = 20ms 一次）
TARGET_SPEED = 2000        # 目标速度 (单位：脉冲数/秒)，先慢一点

# PID 参数（占位，后面实测再调）
SPEED_KP = 1.0
SPEED_KI = 0.05
SPEED_KD = 0.0
HEADING_KP = 2.0
HEADING_KI = 0.0
HEADING_KD = 0.0

