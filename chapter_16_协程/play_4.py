import time
import random


def follow(thefile):
    print(thefile.readlines())
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        print('line')
        print(line)
        if not line:
            time.sleep(0.1)
            continue
        yield line

def countdown(n):
    print('counting from',n)
    while n>0:
        newvalue=(yield n)
        print(newvalue)
        if newvalue is not None:
            n=newvalue
        else:
            n-=1


def start(func):
    def star(*args, **kwargs):
        sd = func(*args, **kwargs)
        next(sd)
        return sd

    return star


@start
def grep(key):
    print('开始在句子里找单词')
    try:
        while True:
            sentence = yield
            if key in sentence:
                print('find it')
    except GeneratorExit:
        print('byebye')
    pass

@start
def accept_number():
    while True:
        result=yield
        print('accept value:',result)


def prdouce_an_item():
    s = random.randint(0, 10)
    print('produce a new item')
    return s


def source(target):
    while True:
        item = prdouce_an_item()
        time.sleep(2)
        target.send(item)


source(accept_number())