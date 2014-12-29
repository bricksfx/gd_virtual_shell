17行中'/home/fanxu'改为所要连接到主机的home文件夹 34行作同样改动
maintmp_ver3.py
更改第26行 为所要连接的ssh主机地址
27行为所要登录的用户名
28行 self.s.login(self.hostn, self.username, 'fx')
后边'fx' 改为所要登录的用户名的密码


tsTclnt.py 测试用
