#coding=utf8
import subprocess
import sys
 
class FlushFile(object):
    """Write-only flushing wrapper for file-type objects."""
    def __init__(self, f):
        self.f = f
    def write(self, x):
        self.f.write(x)
        self.f.flush()
 
sys.stdout = FlushFile(sys.__stdout__)
 
    
def command_return(command_from_client):

    popen = subprocess.Popen([command_from_client], shell = True, stdout = subprocess.PIPE)
    output = ''
    while True:
        next_line = popen.stdout.readline()
        if next_line == '' and popen.poll() != None:
            break
        return next_line
        #print next_line,
        #output += next_line
    #return output


if __name__ == '__main__':
    while True:
        input = raw_input("请输入指令：")
        print command_return(input)

