#!/usr/bin/env python
#coding=utf8
from socket import *
import time
import sys
import termios
import tty

Host = '202.199.100.61'
Port = 10086
Bufsiz = 1204
addr = (Host, Port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(addr)
print 'connect succeed'
def posix_shell(chan):
    import select
     
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
 
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = chan.recv(1024)
                    if len(x) == 0:
                        print '\r\n*** EOF\r\n',
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                chan.send(x)
 
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
 
while True:
    tcpCliSock.send('start')
    print 'start successful'
    headout = tcpCliSock.recv(Bufsiz)
    if headout == 'youcanstart':
        print 'start successful'
    '''
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
    '''
    posix_shell(tcpCliSock)
    tcpCliSock.close()

