import time


def clock(func):
    def clocked(*args):
        begin_time = time.perf_counter()
        b = func(*args)
        print(b)
        end_time = time.perf_counter()
        print("spend time is {}".format(end_time - begin_time))

    return clocked
