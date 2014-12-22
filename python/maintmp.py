#coding=utf8
import execute
import hostname
import os

class operation():
    def __init__(self):
        self.host = hostname.hostname()
        self.username = os.getlogin()
        self.path = os.getcwd()
        self.start = self.username + '@' + \
        self.host + ':'+ self.path + '$' + ' '

    def display(self):
        while True:
            input = raw_input(self.start)
            if input == 'exit':
                break
            execute.command_return(input)

test1 = operation()
test1.display()
