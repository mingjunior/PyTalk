"""
客户端 视图层

为用户提供图形界面,将用户指令发给逻辑处理层
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from bll import Client

class App:
	def __init__(self, master=None):
		self.client = Client()  # 生成客户端逻辑处理对象
		self.master = master
		self.frame = tk.Frame(self.master)
		self.frame.title("PyTalk")
		# self.frame.geometry('400x200')
		self.frame.resizable(0,0)
		self.init_widget()
	
	def init_widget(self):  # 生成登录界面
		tk.Label(self.frame, text='Welcome to PyTalk', font=('微软雅黑', 16)).grid(row=0,column=0,columnspan=3)
		tk.Label(self.frame, text="用户名：").grid(row=1,column=0,padx=10, pady=10)
		tk.Label(self.frame, text="密  码：").grid(row=2,column=0,padx=10, pady=10)
		
		self.name = tk.StringVar()  # 创建tk字符串用于绑定输入的用户名
		self.entry_name = tk.Entry(self.frame, textvariable=self.name)
		self.entry_name.grid(row=1,column=1,columnspan=2, padx=10, pady=10)
		self.pwd = tk.StringVar()  # 创建tk字符串用于绑定输入的密码
		self.entry_pwd = tk.Entry(self.frame, textvariable=self.pwd, show="*")
		self.entry_pwd.grid(row=2,column=1,columnspan=2, padx=10, pady=10)

		self.btn_register = tk.Button(self.frame,text='Register', command=self.register)
		self.btn_register.grid(row=3,column=0,padx=10,pady=10)
		self.btn_login = tk.Button(self.frame,text='Login', command=self.login)
		self.btn_login.grid(row=3,column=1,padx=10,pady=10)
		btn_quit = tk.Button(self.frame,text='Cancel', command=self.frame.quit, fg='red')
		btn_quit.grid(row=3,column=2,padx=10,pady=10)
	

	def login(self):
		name = self.name.get()
		pwd = self.pwd.get()
		re = self.client.do_login(name, pwd)
		if re == 'OK':  # 登录成功跳到聊天界面
			self.chat()
		else:
			tk.messagebox.showerror(message=re)


	def register(self):  # 创建注册子窗口
		reg_window = tk.Toplevel(self.frame)
		reg_window.title('Register PyTalk')
		reg_window.resizable(0,0)

		tk.Label(reg_window, text='用户名:').grid(row=0,column=0,padx=10,pady=10)
		tk.Label(reg_window, text='密码:').grid(row=1,column=0,padx=10,pady=10)
		tk.Label(reg_window, text='确认密码:').grid(row=2,column=0,padx=10,pady=10)
		self.reg_name = tk.StringVar()
		entry_name = tk.Entry(reg_window, textvariable=self.reg_name)
		entry_name.grid(row=0,column=1,padx=10,pady=10)
		self.reg_pwd = tk.StringVar()
		entry_pwd = tk.Entry(reg_window, textvariable=self.reg_pwd, show='*')
		entry_pwd.grid(row=1,column=1,padx=10,pady=10)
		self.reg_pwd2 = tk.StringVar()
		entry_pwd2 = tk.Entry(reg_window, textvariable=self.reg_pwd2, show='*')
		entry_pwd2.grid(row=2,column=1,padx=10,pady=10)
		btn_register = tk.Button(reg_window, text='Register', command=self.do_register)
		btn_register.grid(row=3,column=0,padx=10,pady=10)
		btn_quit = tk.Button(reg_window, text='Cancel', command=reg_window.quit)
		btn_quit.grid(row=3,column=1,padx=10,pady=10)

	def do_register(self):
		name = self.reg_name.get()
		pwd = self.reg_pwd.get()
		pwd2 = self.reg_pwd2.get()
		if pwd == pwd2:
			re = self.client.do_register(name, pwd)
			if re == "OK":
				tk.messagebox.showinfo(message="注册成功")
			else:
				tk.messagebox.showerror(message=re)
		else:
			tk.messagebox.showerror(message="两次密码不同")
	
	def chat(self):
		self.frame.quit  # 销毁登录界面
		self.master.geometry('1000x800')
		self.window = tk.Frame(self.master)  # 创建聊天窗口
		self.list_friends = self.client.get_friends_list(self.name)
		self.menubar = tk.Menu(self.window)
		self.window['menubar'] = self.menubar







if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.mainloop()