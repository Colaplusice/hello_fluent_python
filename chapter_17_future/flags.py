import os
import sys
import requests
import time
POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()


BASE_URL='http://flupy.org/data/flags'

DEST_DIR='/Users/fanjialiang2401/Desktop/flags'

def get_flag(cc):
    url='{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
    print(url)
    resp=requests.get(url)
    return resp.content

def save_flag(img,filename):
    print(filename)
    path=os.path.join(DEST_DIR,filename)
    with open(path,'wb')as fp:
        fp.write(img)


def get_many(flag_list):
    for i in flag_list:
        flag=get_flag(i)
        show_txt(flag)
        save_flag(flag,i.lower()+'.gif')
    return len(flag_list)


def show_txt(text):
    print(text,end=' ')
    sys.stdout.flush()

def main(get_many):
    t0 = time.time()
    count = get_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{}flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(get_many)

