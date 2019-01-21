from concurrent.futures import ThreadPoolExecutor


def wait_on_future():
    print('here')
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())


executor = ThreadPoolExecutor(max_workers=10)
executor.submit(wait_on_future)
