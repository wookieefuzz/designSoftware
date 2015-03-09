import socket
import re

host = ''
port = 5903
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

while True:
    csock,caddr = sock.accept()
    print "connection from: " + 'caddr'
    req = csock.recv(1024)
    print req
    fo = open("agUAVlog.txt","a")
    fo.write(req)
    fo.write("\n")
    fo.close()
    csock.close()
    
import socket
import re

host = ''
port = XXXX # your open port here
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

while True:
    csock,caddr = sock.accept()
    print "incoming connection" 
    req = csock.recv(1024)
    print req
    fo = open("log.txt","a")
    fo.write(req)
    fo.write("\n")
    fo.close()
    csock.close()
    
    