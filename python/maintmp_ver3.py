#coding=utf8
import subprocess
import sys
import execute
import hostname
import os
import time
from socket import *
import pxssh

HOST = 'localhost'
PORT = 10086
BUFSIZE = 8192
ADDR = (HOST, PORT)

class operation():
    def __init__(self):
        os.chdir('/home/fangxu')
        self.host = hostname.hostname()
        self.username = os.getlogin()
        self.path = os.getcwd()
        self.start = self.username + '@' + \
        self.host + ':'+ self.path + '$' + ' '
        try:
            self.s = pxssh.pxssh()
            self.hostn = '127.0.0.1'
            self.username = 'fangxu'
            self.s.login(self.hostn, self.username, 'fx')
            print 'ssh 登录成功'
        except pxssh.ExceptionPxssh, e:
            print 'pxssh failed to login.'
            print str(e)
        
    def dirchange(self, dirn):
        os.chdir(dirn) 
        self.host = hostname.hostname()
        self.username = os.getlogin()
        self.path = os.getcwd()
        self.start = self.username + '@' + \
        self.host + ':'+ self.path + '$' + ' '

    def command_return(self, command_from_client, cli):
        comm = command_from_client.split()
        if comm[0] == 'cd':
            print "yes it's cd"
            print comm[1]
            self.dirchange(comm[1])
        try:
            self.s.sendline(command_from_client)
            self.s.prompt()
            cli.send(self.s.before)
            time.sleep(0.1)
            cli.send('#')
            time.sleep(0.1)
        except KeyboardInterrupt, e:
            cli.send('ERROR')

    def conn_ser(self):
        self.tcpser = socket(AF_INET, SOCK_STREAM)
        self.tcpser.bind(ADDR)
        self.tcpser.listen(5)

        while True:
            print 'waiting for connect'
            self.tcpcli , self.addr = self.tcpser.accept()
            while True:
                try:
                    head = self.tcpcli.send(self.start)
                    command_from_cli = self.tcpcli.recv(BUFSIZE)
                    self.command_return(command_from_cli, self.tcpcli)
                except Exception, ex:
                    print ex
                    break

    def display(self):
        while True:
            input = raw_input(self.start)
            if input == 'exit':
                break
            execute.command_return(input)

test1 = operation()
test1.conn_ser()
