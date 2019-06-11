"""
客户端 逻辑处理层

1. 建立套接字与服务端连接
2. 接收界面层指令和逻辑处理
"""


from socket import *
from select import select
import os

# 服务端地址
HOST = '0.0.0.0'
POST = 10000
ADDR = (HOST, POST)


class Client:
	def __init__(self):
		self.create_socket()

	def create_socket(self):
		self.sockfd = socket(AF_INET, SOCK_STREAM)
		try:
			self.sockfd.connect(ADDR)
		except:
			sys.exit()
	
	def do_register(self, name, passwd): # 已经在ui.py中判断两次密码是否相同了
		msg = "R " + name + " " + passwd
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(128).decode()
		if data == "OK":
			print("register success")
			# 跳转到 do_chat
			# 返回ok, 图形界面进入登录界面
		else:
			print(data)

	def do_login(self, name, passwd):
		msg = "L " + name + " " + passwd
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(128).decode()
		if data == 'OK':
			print("login success")
			# 跳转到 do_chat
			# 返回ok, 图形界面进入聊天界面
		else:
			print(data)
	
	def do_chat(self, name_send, name_recv, data):
		# 添加IO多路复用, 接收和发消息
		# rlist = [self.sockfd]
		# wlist = []
		# xlist = []
		# while True:
		# 	rs, ws, xs = select(rlist, wlist, xlist)
		# 	for r in rs:
		# 		if r is self.sockfd:
		# 			connfd, addr = r.accept()
		# 			rlist.append(connfd)
		# 		else:
		# 			self.send_msg()
		# 			rlist.remove(r)

		pid = os.fork()
		if pid == 0:
			self.send_msg()

	def do_addfriend(self, name_send, name_recv):
		msg = "A " + name_send + " " + name_recv
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(128).decode()
		if data == "OK":
			print("Add friend success")
		else:
			print(data)
	
	def send_msg(self, name_send, name_recv, data):
		msg = "M " + name_send + " " + name_recv + " " + data
		pass
	
	def recv_msg(self, name_send, name_recv, data):
		pass




if __name__ == '__main__':
	client = Client()
	client.do_register('cm', '123456')
	client.do_login('cm', '123456')
	client.do_addfriend('cm', 'alan')