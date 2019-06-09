import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('PyTalk')
# window.iconbitmap('image/logo.ico')
window.geometry('400x300')
window.resizable(0, 0)

# welcome image
canvas = tk.Canvas(window, width=400, height=300, bg='lightblue')
image_file = tk.PhotoImage(file='image/welcome.gif')
image = canvas.create_image(200, 20, anchor='n', image=image_file)
canvas.pack(side=tk.TOP)

# user information
tk.Label(window, text='User name:').place(x=50, y=130)
tk.Label(window, text='Password:').place(x=50, y=170)

var_usr_name = tk.StringVar()
var_usr_name.set('example@pytalk.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=130)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=170)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    try:
        with open('usrs_info.pickle', 'rb') as usrs_file:
            usrs_info = pickle.load(usrs_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usrs_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usrs_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome to PyTalk', message='How are you?\t' + usr_name)
        else:
            tk.messagebox.showerror(message='Wrong password! Try agian')
    else:
        is_sing_up = tk.messagebox.askyesno(title='Welcome', message='You have not sign up yet. Sign up now?')
        if is_sing_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_pytalk():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 检查用户名是否存在
        with open('usrs_info.pickle', 'rb') as usrs_file:
            exist_usr_info = pickle.load(usrs_file)

        if np != npf:
            tk.messagebox.showerror(title='Error', message='Password is different from confirm password!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror(title='Error', message='The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usrs_file:
                pickle.dump(exist_usr_info, usrs_file)
            tk.messagebox.showinfo(title='Welcome', message='You have signed up!')

    window_sign_up = tk.Toplevel(window)  # 创建子窗口
    window_sign_up.title('Sign up PyTalk')
    window_sign_up.geometry('350x200')
    window_sign_up.resizable(0, 0)
    window_sign_up.iconbitmap('image/logo.ico')

    new_name = tk.StringVar()
    new_name.set('example@pytalk.com')
    tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password:').place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_new_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_pytalk)
    btn_confirm_sign_up.place(x=150, y=130)


# login and sign up button
btn_quit = tk.Button(window, text='Cancel', command=window.quit)
btn_quit.place(x=50, y=220)
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=160, y=220)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=250, y=220)

window.mainloop()
