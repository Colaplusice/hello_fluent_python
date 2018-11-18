# encoding=utf-8
import socket,sys

port=2401
host = sys.argv[1]
filename = sys.argv[2]
# af address famliy 用于互联网技术
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host,port))
except socket.gaierror,e:
    print('连接出现错误%s'%e)

    s.sendall(filename+"\r\n")
    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)
        sys.exit(1)

