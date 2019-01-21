import asyncio
import time


@asyncio.coroutine
def get_flags(cc):
    print('this is get flag cc'.format(cc))
    time.sleep(1)
    resp = yield from cc
    return resp


@asyncio.coroutine
def download_one(cc):
    print('this is cc '.format(cc))
    time.sleep(1)
    cc = yield from get_flags(cc)
    return cc


def download_many(num):
    loop = asyncio.get_event_loop()
    to_do = [download_one(i) for i in range(num)]

    # 等待所有协程运行完毕结束
    wait_coro = asyncio.wait(to_do)
    # 执行事件循环，直到wait_coro运行结束
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


download_many(15)
