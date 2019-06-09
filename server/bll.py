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
		print("handle")


if __name__ == '__main__':
	server = PyTalkServer()
	server.start_server()