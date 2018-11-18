from  concurrent import futures

from flags import save_flag,get_flag,show_txt,main

MAX_WORKS=20

def download_one(cc):
    flag= get_flag(cc)
    save_flag(flag,cc.lower()+'.gif')
    return cc

def download_many(cc_list):
    works=min(MAX_WORKS,len(cc_list))

    with futures.ThreadPoolExecutor(works) as excutor:

        res=excutor.map(download_one,sorted(cc_list))
        return len(list(res))

if __name__ == '__main__':
    main(download_many)