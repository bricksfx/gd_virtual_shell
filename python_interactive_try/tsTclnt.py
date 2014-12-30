#!/usr/bin/env python
#coding=utf8
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
        if data.find('in#') >= 0:
            data = data.replace('in#\n', '')
            print data,
            command_input = raw_input()
            command_input += '\n'
            tcpCliSock.send(command_input)
        else:
            print data,
            time.sleep(0.1)
tcpCliSock.close()

