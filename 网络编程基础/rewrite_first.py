# encoding=utf-8
import socket
import sys


host=sys.argv[1]
port=70
filename=sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host,port))


except socket.gaierror,e:
    print("连接错误%s"%e)

    # makefile 构建一个文件类对象
fd=s.makefile('rw',0)

fd.write(filename+'\r\n')

for line in fd.readlines():
    sys.stdout.write(line)