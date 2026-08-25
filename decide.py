import confing

DANGER = "blue_danger"


def decide(dets):
    #当未检测到目标是左轮正转右轮反转顺时针搜索目标
    if not dets:
        return 20, -20

    #过滤危险目标
    safe = [det for det in dets if det["cls"] != DANGER]

    #过滤完未找到目标，躲开危险目标
    if not safe:
        target = max(dets, key=lambda d: d["conf"])
        error = target["cx"] - 320
        diff = 0.2 * error
        return confing.TARGET_SPEED - diff, confing.TARGET_SPEED + diff

    #找到目标，向目标移动
    target = max(safe, key=lambda d: d["conf"])
    error = target["cx"] - 320
    diff = 0.2 * error
    return confing.TARGET_SPEED + diff, confing.TARGET_SPEED - diff



