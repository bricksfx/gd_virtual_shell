#coding=utf8
import socket
import sys
from socket import *
import time
 
# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False
 
 
def interactive_shell(chan,ser):
    if has_termios:
        posix_shell(chan, ser)
    else:
        windows_shell(chan)
 
def judge(strin):
    if (strin.find('@') >=0):
        strout = strin +'in#' +'\n'
        return strout
    elif (strin.find('[sudo] password for') >= 0):
        strout = strin + 'in#' + '\n'
        return strout
    return strin

def posix_shell(chan, ser):
    import select
     
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        ch = 0
        std = 0
        while True:
            r, w, e = select.select([chan,ser], [], [])
            if chan in r:
                try:
                    x = chan.recv(1024)
                    if len(x) == 0:
                        print '\r\n*** EOF\r\n',
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                    ser.send(judge(x))
                except timeout:
                    pass

            if ser in r:
                try:
                    x = ser.recv(1024)
                    if len(x) != 0:
                        chan.send(x)
                    elif len(x) == 0:
                        break
                except timeout:
                        pass

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
 
     
# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading
 
    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
         
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()
         
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
         
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
