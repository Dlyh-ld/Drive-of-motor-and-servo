class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0        # 累积误差
        self.previous_error = 0  # 前次误差
        self.has_prev = False    # 有没有"上次误差"（第一次还没有）

    def update(self, error, dt):
        p = self.Kp * error
        self.integral += error * dt
        i = self.Ki * self.integral

        # 第一次调用时还没有"上次误差"，变化率算 0，避免尖峰
        if self.has_prev:
            d = self.Kd * (error - self.previous_error) / dt
        else:
            d = 0.0

        self.previous_error = error
        self.has_prev = True     # 从下一次起，就有"上次误差"了
        return p + i + d

