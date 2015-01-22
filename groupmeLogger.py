import socket
import re

host = ''
port = 5902
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

while True:
    csock,caddr = sock.accept()
    print "connection from: " + 'caddr'
    req = csock.recv(1024)
    print req
    csock.close()
    
    