from concurrent import futures
import time

worker_num = 10

result = []


def get_one(name):
    print(name)
    result.append(name)
    time.sleep(2)
    return 123


to_do = []

with futures.ThreadPoolExecutor(worker_num) as executor:
    for _ in range(10):
        future = executor.submit(get_one, "name")
        # print(future.result())
        to_do.append(future)

print(result)

