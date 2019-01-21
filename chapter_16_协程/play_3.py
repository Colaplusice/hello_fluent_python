import time


def yields():
    yield sd()


def sd():
    print('sd')
    time.sleep(3)
    yield 1


ssd = yields()
aasd = next(ssd)
# print(next(aasd))
# print(next(aasd))
