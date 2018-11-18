import asyncio
import threading

import time


# @asyncio.coroutine
def hello(name):
    for i in range(4):
        time.sleep(i)
        print("hello {} : {}".format(name, i))
        world()
    # yield world()


def world():
    for i in range(4):
        print("come {}".format(i))
        time.sleep(i)


# 执行协程
start = time.time()
for i in range(4):
    threading.Thread(target=hello, args=("sd",)).start()
# 获取一个event_loop
# loop=asyncio.get_event_loop()
# a_list=[hello('sad') for i in range(4)]
# loop.run_until_complete(asyncio.wait(a_list))
# loop.close()
end = time.time()
print("spend time {}".format(end - start))
