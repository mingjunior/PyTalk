import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("PyTalk")
root.iconbitmap('image/logo.ico')
root.geometry("1000x800")
# root.resizable(False, False)

# 左侧框架
frm_left = tk.Frame(root, background='lightblue')
frm_left.place(relx=0,rely=0,relwidth=0.2,relheight=1)
# 右侧框架
frm_right = tk.Frame(root, background='lightgreen')
frm_right.place(relx=0.2,rely=0,relwidth=0.8,relheight=1)

# 左侧框架，主页标签
label_home = tk.Label(text='User Name', foregound=)

root.mainloop()