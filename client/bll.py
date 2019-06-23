"""
客户端 逻辑处理层

1. 建立套接字与服务端连接
2. 接收界面层指令和逻辑处理
"""


from socket import *
from multiprocessing import Process
import sys

# 服务端地址
HOST = '127.0.0.1'
POST = 10000
ADDR = (HOST, POST)


class Client:
	def __init__(self):
		self.create_socket()

	def create_socket(self):
		self.sockfd = socket(AF_INET, SOCK_STREAM)
		print("haha")
		try:
			self.sockfd.connect(ADDR)
		except Exception as e:
			# sys.exit()
			print(e)
	
	def do_register(self, name, passwd): # 已经在ui.py中判断两次密码是否相同了
		msg = "R " + name + " " + passwd
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(128).decode()
		if data == "OK":
			print("register success")
			return data
			# 跳转到 do_chat
			# 返回ok, 图形界面进入登录界面
		else:
			print(data)
			return data

	def do_login(self, name, passwd):
		msg = "L " + name + " " + passwd
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(128).decode()
		if data == 'OK':
			print("login success")
			return 'OK'
			# 跳转到 do_chat
			# 返回ok, 图形界面进入聊天界面
		else:
			print(data)
			return data
	
	def do_chat(self, name_send, name_recv, data):
		# 创建分支进程接收消息
		p = Process(target=self.recv_msg, args=(self.sockfd,))
		p.daemon = True
		p.start()
		# 主进程发送消息或请求

	def do_addfriend(self, name_send, name_recv):
		msg = "A " + name_send + " " + name_recv
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(128).decode()
		if data == "OK":
			print("Add friend success")
		else:
			print(data)
	
	def send_msg(self, name_send, name_recv, data):
		while True:
			msg = "M " + name_send + " " + name_recv + " " + data
			self.sockfd.send(msg.encode())
	
	def recv_msg(self, name_send, name_recv, data):
		while True:
			data = self.sockfd.recv(1024).decode()
			print(data)
	
	def get_friends_list(self, name):
		msg = 'G ' + name
		self.sockfd.send(msg.encode())
		data = self.sockfd.recv(1024)
		return data





if __name__ == '__main__':
	client = Client()
	client.do_register('cm', '123456')
	client.do_login('cm', '123456')
	client.do_addfriend('cm', 'alan')