#!/usr/bin/env python
from socket import *
Host = 'localhost'
Port = 10086
Bufsiz = 8192
addr = (Host, Port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(addr)
print 'connect succeed'

while True:
    tcpCliSock.send('start')
    print 'start successful'
    headout = tcpCliSock.recv(Bufsiz)
    if headout == 'youcanstart':
        print 'start successful'
    while True:
        data = tcpCliSock.recv(Bufsiz)
        if data == '#':
            break
        print data,
tcpCliSock.close()

