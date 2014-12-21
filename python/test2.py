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
 
popen = subprocess.Popen(['ping -c 4 www.baidu.com'], shell = True, stdout = subprocess.PIPE)

print "step1"
 
 
while True:
    next_line = popen.stdout.readline()
    if next_line == '' and popen.poll() != None:
        break
    sys.stdout.write(next_line)
