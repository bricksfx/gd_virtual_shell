#!/usr/bin/env python
from socket import *
import time
import sys

Host = 'localhost'
Port = 10086
Bufsiz = 1204
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
        time.sleep(0.1) 
        if data.find('in#') >= 0:
            data1 = data.replace('\n', '')
            data2 = data1.replace('in#', '')
            sys.stdout.flush()
            print data2, 
            command_input = raw_input()
            tcpCliSock.send(command_input)
        else:
            print data,
tcpCliSock.close()

