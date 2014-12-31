#coding=utf8
import paramiko
import interactive
from socket import *

#记录日志
paramiko.util.log_to_file('/tmp/test')

class ssh_conn:
    def conn(self):
        self.ssh=paramiko.SSHClient()
	self.ssh.load_system_host_keys()
	self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	self.ssh.connect('127.0.0.1',port=22,username='fangxu',password='fx',compress=True)

    def interactive_shell(self, ser):
        self.channel = self.ssh.invoke_shell()
        interactive.interactive_shell(self.channel, ser)

    def close(self):
        self.channel.close()
        self.ssh.close()

class socket_ser:
    HOST = '10.16.1.219'
    PORT = 10086
    ADDR = (HOST, PORT)
    BUFSIZE = 1024
    def start_soc(self):
        self.TcpSer = socket(AF_INET, SOCK_STREAM)
        self.TcpSer.bind(self.ADDR)
        self.TcpSer.listen(5)

    def conn(self):
        self.start_soc()
        while True:
            print 'waiting for conect'
            try:
                self.tcpcli, self.addr = self.TcpSer.accept()
                begin_tag_from_cli = self.tcpcli.recv(self.BUFSIZE)
                if begin_tag_from_cli == 'start':
                   print 'succeed' 
                   self.tcpcli.send('youcanstart')
                   ssh = ssh_conn()
                   try:
                       ssh.conn()
                       ssh.interactive_shell(self.tcpcli)
                   except Exception, ex:
                       print ex
                   finally:
                       ssh.close()
            except Exception, ex:
                print ex
            finally:
                self.tcpcli.close()

def main():
    sock = socket_ser()
    sock.conn()

if __name__ == '__main__':
     main()
        
 

