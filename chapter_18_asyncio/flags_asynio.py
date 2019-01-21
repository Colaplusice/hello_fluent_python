import asyncio
import aiohttp
from chapter_17_future.download_flag import BASE_URL, save_flag, show, main


@asyncio.coroutine
def get_flags(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    # 阻塞的操作，通过协程实现
    resp = yield from aiohttp.request("GET", url)
    image = yield from resp.read()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flags(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]

    # 等待所有协程运行完毕结束
    wait_coro = asyncio.wait(to_do)
    # 执行事件循环，直到wait_coro运行结束
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == "__main__":
    main(download_many)
