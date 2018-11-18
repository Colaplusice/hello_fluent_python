def xiecheng_2(a):
    print("start a", a)
    b = yield a
    print("received b", b)
    c = yield a + b
    print("received c", c)
