"""
服务端 逻辑处理层

1. 建立套接字链接
2. 逻辑处理: 处理客户端请求和调用模型层
"""

import sys

from socket import *
from multiprocessing import Process

# 服务端地址
HOST = '0.0.0.0'
POST = 10000
ADDR = (HOST, POST)

class PyTalkServer:
	def __init__(self):
		self.address = ADDR
		self.user = [] # 在线用户列表[(username, connfd)]
		self.create_socket()

	def create_socket(self):
		"""创建套接字,绑定地址,并监听"""
		self.sockfd = socket(AF_INET, SOCK_STREAM)
		self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
		self.sockfd.bind(self.address)
		self.ip = self.address[0]
		self.port = self.address[1]

	def start_server(self):
		"""启动服务"""
		self.sockfd.listen(5)
		print("Listen the port %d ..." % self.port)

		# 如何处理僵尸进程

		while True:
			try:
				connfd, addr = self.sockfd.accept()
			except KeyboardInterrupt:
				self.sockfd.close()
				sys.exit("服务器退出")
			except Exception:
				continue

			print("Connect from", addr)
			client = Process(target=self.handle, args=(connfd,))
			client.Daemon = True
			client.start()

	def handle(self, connfd):
		while True:
			data = connfd.recv(1024).decode()
			if not data or data[0] == 'Q': # 退出
				connfd.close()
				return
			elif data[0] == 'R': # 注册
				self.do_register(connfd, data)
			elif data[0] == 'L': # 登录
				self.do_login(connfd, data)
			elif data[0] == 'M': # 发送消息
				self.do_message(connfd, data)
			elif data[0] == 'A': # 添加好友
				self.do_addfriend(connfd, data)
	
	def do_register(self, connfd, data):
		print(data)
		# 判断用户名是否已存在
		if False:
			connfd.send("OK".encode())
		else:
			connfd.send("用户名已存在".encode())
	
	def do_login(self, connfd, data):
		print(data)
		# 判断用户名密码是否正确
		if False:
			connfd.send("OK".encode())
		else:
			connfd.send("密码错误/用户不存在".encode())

	def do_message(self, connfd, data):
		print(data)
	
	def do_addfriend(self, connfd, data):
		print(data)
		# 判断用户是否在线
		if True:
			connfd.send("OK".encode())
		else:
			connfd.send("用户不在线".encode())


if __name__ == '__main__':
	server = PyTalkServer()
	server.start_server()