# encoding =utf-8
import sys, urllib

# 输出html信息
# python gopher.py http://gopher.quux.org:70/

f = urllib.urlopen(sys.argv[1])
while 1:
    buf = f.read(2048)
    if not len(buf):
        break

    sys.stdout.write(buf)
