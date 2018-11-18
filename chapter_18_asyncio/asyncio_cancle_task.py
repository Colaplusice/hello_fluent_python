import asyncio


async def task_func():
    print("in task")

    return "result"


async def main(loop):
    print("create task")

    task = loop.create_task(task_func())

    print("cancel task")
    task.cancel()
    print("cancel task{!r}".format(task))

    try:
        await task
    except asyncio.CancelledError:
        print("caught error from canceled task")
    else:
        print("task result:{!r}".format(task.result()))


event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(main(event_loop))

finally:
    event_loop.close()
