import tkinter as tk 
from tkinter import messagebox
import random

root = tk.Tk()
root.title("PyTalk")
root.iconbitmap('image/logo.ico')
root.geometry("1000x800")
# root.resizable(False, False)

top_frm = tk.Frame(root, background='dodgerblue')
top_frm.place(x=0, y=0, relwidth=1, relheight=0.1)

# 左侧图标
image_home = tk.PhotoImage(file='image/home.gif')
top_label = tk.Button(top_frm,
					image=image_home, 
					font=('Arial', 20, 'bold'),
					foreground='white',
					background='dodgerblue',
					compound=tk.LEFT) # 图片在文字左边
top_label.bm = image_home # 手动为top_label添加属性bm，绑定图片变量，防止图片被回收
top_label.place(relx=0.02, rely=0.5,anchor='w')

# 主框架
frm = tk.Frame(root, background='#EEE')
frm.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
# frm.pack(fill=tk.BOTH, expand=True)
# 左右次框架
frm_left = tk.Frame(frm, background='#EEE')
frm_left.place(relx=0, rely=0, relwidth=0.2, relheight=1)
# frm_left.pack(side='left', fill=tk.Y, expand=True)
frm_right = tk.Frame(frm,background='lightgreen')
frm_right.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
# frm_right.pack(side='right', fill=tk.Y, expand=True)

# 左侧添加listbox，显示好友列表
listbox_friends = tk.Listbox(frm_left)
listbox_friends.pack(fill=tk.BOTH, expand=True)

# 右侧分为聊天窗和文本输入窗

# 左右两侧添加滑块
# 创建Scrollbar组件，设置组件与左侧框的纵向滚动关联
scroll_left = tk.Scrollbar(listbox_friends, command=listbox_friends.yview)
scroll_left.pack(side='right',fill=tk.Y)
# 设置左侧框的纵向滚动影响scroll_left滚动条
listbox_friends.configure(yscrollcommand=scroll_left.set)


# 左侧添加好友列表，从服务器获取
list_friends = [
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
	'王五'
]
list_friends.sort()
# 循环创建好友标签按钮
for i, name in enumerate(list_friends):
	# 生成3个随机数，并将其格式化成16进制，转成颜色格式
	color_number = [random.randrange(0, 256) for i in range(3)]
	grayness = int(round(0.299*color_number[0]+0.587*color_number[1]+0.114*color_number[2]))
	bg_color = "#%02x%02x%02x" % tuple(color_number)
	fg_color = 'white' if grayness < 128 else 'black'

	# # 创建并放置标签
	# btn_friend = tk.Button(listbox_friends, text=name, fg=fg_color, bg=bg_color, font=('Arial', 20, 'bold'))
	# btn_friend.place(relx=0, rely=0.11*i, relwidth=1, relheight=0.1)
	# print(name)
	label_friend = tk.Label(listbox_friends, text=name, fg=fg_color, bg=bg_color, font=('Arial', 20, 'bold'))
	label_friend.pack()
	listbox_friends.insert(tk.END, label_friend)


root.mainloop()