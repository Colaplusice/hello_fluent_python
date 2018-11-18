from collections import namedtuple

Result = namedtuple("count", "average")


def cal_speed_finally():
    total = 0.0
    count = 0
    average = 0
    while True:
        receive = yield
        if not receive:
            break
        count += 1
        total += receive
        average = total / count
    return Result(count, average)
