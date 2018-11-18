# 是一个生成器类型的对象
def countdown(n):
    print("countdown form n", n)
    while n > 0:
        # 将的值保存起来，返回一个生成器对象
        yield n
        n -= 1
    print("down")


if __name__ == "__main__":
    s = countdown(10)
    print(type(s))
    # print(countdown(10))

    # for i in countdown(10):
    #     print(i)
