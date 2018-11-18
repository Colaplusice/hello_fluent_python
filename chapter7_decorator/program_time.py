import time

def clock(func):
    def clocked(*args):
        t_1=time.perf_counter()
            # 运行实体函数
        result=func(*args)
        t_2=time.perf_counter()
        name=func.__name__
        arg_str=','.join(repr(arg) for arg in args)
        print('spend time is {},arg is{}'.format(t_2-t_1,arg_str))
        return result
    return clocked

@clock
def generate_100():
    a_list=[]
    for i in range(10):
        a=[2]*10
        a_list.append(a)
    return a_list

@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)


if __name__ == '__main__':
    factorial(130)

# print(generate_100())