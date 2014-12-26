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
    headout = tcpCliSock.recv(Bufsiz)
    print headout,
    command_in = raw_input("")

    tcpCliSock.send(command_in)
    while True:
        data = tcpCliSock.recv(Bufsiz)
        if data == '#':
            break
        print data
tcpCliSock.close()

