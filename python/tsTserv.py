#!/usr/bin/env python
#coding=utf8

from socket import *

HOST = 'localhost'
PORT = 8001
BUFSIZE = 1204
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


def connect():
    while True:
        print 'waiting for connecting...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connect from :', addr
        while True:
            headout = tcpCliSock.recv(BUFSIZE)
            print headout,
            command_in = raw_input("")
            tcpCliSock.send(command_in)
            while True:
                data = tcpCliSock.recv(BUFSIZE)
                if data == '#':
                    break
                print data
            print "next"
        tcpCliSock.close()
    tcpSerSock.close()

if __name__ == '__main__':
    connect()
