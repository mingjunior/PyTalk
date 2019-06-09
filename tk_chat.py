import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import time

class App:
	def __init__(self, master=None):
		self.master = master
		self.master.title('pytalk')
		self.master.geometry('1000x800')
		self.list_friends = [
						    'Alan',
						    'Will',
						    'Bran',
						    'Bob',
						    'Kevin',
						    'Daisy',
						    'Mary',
						    'Carl',
						    'Lily',
						    'Kate',
						    'Jeo',
						    '张三',
						    '李四',
						    '王五',
						    '赵六',
						    '陈七',
						    '唐八',
						    '沈九'
						]
		self.initWidgets()

	def initWidgets(self):
		self.frm_btn = tk.Frame(self.master,bg='#eee')
		self.frm_btn.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.05)
		self.create_top_btn()
		self.nb = ttk.Notebook(self.master)
		self.nb.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)
		self.create_friends_tag()
		self.text_input = tk.Entry(self.master,bg='#EEE', font=('宋体', 16, 'normal'))
		self.text_input.place(relx=0.1, rely=0.9, relwidth=0.7, relheight=0.05)
		self.btn_send_msg = tk.Button(self.master, 
			text='发送消息', cursor='hand2', font=('Arial', 16, 'bold'), activeforeground='red', command=self.send)
		self.btn_send_msg.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.05)
		
	def create_friends_tag(self):
		self.tab_font_style = ttk.Style().configure('.',font=('微软雅黑', 12))
		self.list_nb_tab = []
		# 循环创建标签
		for frd in self.list_friends:
			text_frd = tk.Text(self.nb, 
								bg='#eee',
								font=('微软雅黑', 16, 'normal'),
								state='disable') # 将文本框设置成不可编辑状态
			self.nb.add(text_frd, text=frd)
			self.list_nb_tab.append(text_frd)

	def create_top_btn(self):
		self.btn_setting = tk.Button(self.frm_btn,
									text='设置',
									cursor='hand2',
									width=10,
									font=('Arial', 16, 'bold'),

									activeforeground='red',
									command=self.set)
		self.btn_setting.pack(side='left', fill='y')
		self.btn_add_friend = tk.Button(self.frm_btn,
									text='添加好友',
									cursor='hand2',
									width=10,
									font=('Arial', 16, 'bold'),
									activeforeground='red',
									command=self.add_friend)
		self.btn_add_friend.pack(side='left', fill='y')

	def set(self):
		pass

	def add_friend(self):
		pass

	def send(self):
		msg_string = self.text_input.get()
		if not msg_string or msg_string == '\n':
			messagebox.showwarning('warning', '消息为空,发送失败')
		else:
			msg_pre = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
			# 选择当前的子窗口部件，即消息显示框
			current_window = self.list_nb_tab[self.nb.index(self.nb.select())]
			current_window.config(state='normal') # 修改文本框为可编辑状态
			# 配置名为time_style的样式
			current_window.tag_configure('time_style', font=('Arial', 10, 'normal'),foreground='green',justify='right')
			current_window.tag_configure('text_style', font=('微软雅黑', 16, 'normal'),justify='right')
			current_window.insert(tk.END, msg_pre, 'time_style')# 插入文本内容，设置使用time_style样式
			current_window.insert(tk.END, msg_string + '\n', 'text_style')
			current_window.config(state='disable')
			self.text_input.delete(0, len(msg_string))

if __name__ == '__main__':
	root = tk.Tk()
	app = App(root)
	root.mainloop()
