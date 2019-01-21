# asyncio

为什么异步的任务比同步的要快，运行到第一个yield from的时候，cpu马上去做其他的事情了。

相当于所有的yield都是同时发出去的，所有并发性上很好
运行到download_one,马上去做get_flag(),然后yield asyncio.http