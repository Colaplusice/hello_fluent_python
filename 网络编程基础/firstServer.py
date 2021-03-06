import socket

host = ""
port = 2401

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print("server is running on port %d press control-c to terminate" % port)

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile("rw", 0)
    clientfile.write("welcome" + str(clientaddr) + "\n")
    clientfile.write("please enter a String:")
    line = clientfile.readline().strip()
    clientfile.write("you entered %d charaters.\n" % len(line))
    clientfile.close()
    clientsock.close()
