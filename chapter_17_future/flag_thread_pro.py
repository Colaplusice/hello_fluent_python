from concurrent import futures
from flag_threadpool import download_one
from flags import POP20_CC, main


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            # 返回一个future 对象表示待执行的操作
            future = executor.submit(download_one, cc)
            print(type(future))
            to_do.append(future)
            msg = "scheduled for {}:{}"
            print(msg.format(cc, future))

        results = []
        # 在函数运行结束后产出期物
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = "{}result:{!r}"

            # 结果全部产生
            print(msg.format(future, res))

            results.append(res)
    return results


if __name__ == "__main__":
    main(download_many)
