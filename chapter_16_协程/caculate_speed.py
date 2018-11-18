from functools import wraps
import time


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def cal_speed():
    total = 0.0
    count = 0
    yield_value = None
    while True:
        now = yield yield_value
        total += now
        count += 1
        print("now the average is :", float(total / count))


cal_speed()
