# encoding=utf-8
from redis import Redis

import rq

# 这个One为工人的名称
queue = rq.Queue("two", connection=Redis.from_url("redis://"))

# 第一个参数为想执行任务的名称
job = queue.enqueue("one.example", 23)

sd = job.get_id()
print(sd)
