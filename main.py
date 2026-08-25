import pigpio
import confing
import encoder
import motor
import pid
import servo
import time




pi = pigpio.pi()  # 初始化 pigpio

pi.set_mode(confing.MOTOR_STBY, pigpio.OUTPUT)  # 设置电机使能引脚为输出
pi.write(confing.MOTOR_STBY, 1)  # 使能电机驱动器

motor_left = motor.Motor(pi, confing.WHEEL_LEFT_PWM, confing.WHEEL_LEFT_AIN1, confing.WHEEL_LEFT_AIN2)
motor_right = motor.Motor(pi, confing.WHEEL_RIGHT_PWM, confing.WHEEL_RIGHT_AIN1, confing.WHEEL_RIGHT_AIN2)
encoder_left = encoder.Encoder(pi, confing.ENCODER_LEFT_A, confing.ENCODER_LEFT_B)
encoder_right = encoder.Encoder(pi, confing.ENCODER_RIGHT_A, confing.ENCODER_RIGHT_B)
pid_left = pid.PID(confing.SPEED_KP, confing.SPEED_KI, confing.SPEED_KD)
pid_right = pid.PID(confing.SPEED_KP, confing.SPEED_KI, confing.SPEED_KD) 
heading_pid = pid.PID(confing.HEADING_KP, confing.HEADING_KI, confing.HEADING_KD)  

TARGET = confing.TARGET_SPEED   # 目标速度 (单位：脉冲数/秒)
dt = 1.0 / confing.CONTROL_LOOP_HZ  # 控制周期，单位秒
prev_l = encoder_left.count  # 上一时刻左轮编码器计数
prev_r = encoder_right.count  # 上一时刻右轮编码器计数
heading = 0  # 未偏航角度



while True:
    current_l = encoder_left.count  # 当前左轮编码器计数
    current_r = encoder_right.count  # 当前右轮编码器计数

    delta_l = current_l - prev_l  # 左轮编码器计数变化
    delta_r = current_r - prev_r  # 右轮编码器计数变化

    prev_l = current_l  # 更新左轮编码器计数
    prev_r = current_r  # 更新右轮编码器计数

    speed_l = (delta_l) /dt  # 左轮速度，单位：脉冲数/秒
    speed_r = (delta_r) / dt  # 右轮速度，单位：脉冲数/秒

    heading += delta_l - delta_r  # 偏航角度变化
    heading = heading % 360  # 限制偏航角度在0-360度之间
    diff = heading_pid.update(heading, dt) # 计算偏航角度的 PID 输出，用于调整左右轮速度差
    error_l = TARGET - speed_l + diff  # 左轮速度误差
    error_r = TARGET - speed_r - diff  # 右轮速度误差

    pid_output_l = pid_left.update(error_l, dt)  # 左轮 PID 输出
    pid_output_r = pid_right.update(error_r, dt)  # 右轮 PID 输出

    motor_left.set_speed(pid_output_l)  # 设置左轮电机速度
    motor_right.set_speed(pid_output_r)  # 设置右轮电机速度
    
    time.sleep(dt)  # 等待下一个控制周期








