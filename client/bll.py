"""
客户端 逻辑处理层

1. 建立套接字与服务端连接
2. 接收界面层指令和逻辑处理
"""


from socket import *

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


if __name__ == '__main__':
	client = Client()