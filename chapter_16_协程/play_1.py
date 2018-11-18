def simple_1(a):
    print('start a >',a)
    b= yield a
    print('receive b',b)
    c=yield a+b
    print('c is ',c)
my_simple_1=simple_1()

from inspect import getgeneratorstate
getgeneratorstate(my_simple_1)
