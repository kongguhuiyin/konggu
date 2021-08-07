# _*_ coding : UTF-8 _*_
#    开发人员 : wangyueke
#    开发时间 : 2021/8/1 21:26
#    文件名称 : Tkinter.py
#    开发工具 : PyCharm

import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('my window')
window.geometry('450x300')
on_hit = False


# def hit_me():
#     global on_hit
#     if on_hit is False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False+
#         var.set('')
# var = tk.StringVar()
# I = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
# I.pack()
# b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
# b.pack()


# ------------------------文本框控件----------------------------------------
# e = tk.Entry(window, show='1')
# e.pack()

# def insert_point():
#     var = e.get()
#     t.insert('insert', var)
#
#
# def insert_end():
#     var = e.get()
#     t.insert('end', var)
#
#
# b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
# b1.pack()
# b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
# b2.pack()
# t = tk.Text(window, height=2)
# t.pack()


# --------------------------列表控件-----------------------------
# var1 = tk.StringVar()
# I = tk.Label(window, bg='yellow', width=20, height=2, textvariable=var1)
# I.pack()
#
#
# def print_selection():
#     value = Ib.get(Ib.curselection())   # 获取选中的文本
#     var1.set(value)
#
#
# b1 = tk.Button(window, text='print selection', width=20, height=2, command=print_selection)
# b1.pack()
#
# var2 = tk.StringVar()
# var2.set((11, 22, 33, 44))
# Ib = tk.Listbox(window, listvariable=var2)
# list_items = [1, 2, 3, 4]
# for item in list_items:
#     Ib.insert('end', item)
#
# Ib.insert(1, 'first')
# Ib.insert(2, 'second')
# Ib.delete(2)
# Ib.pack()


# --------------------------Scale尺度-----------------------------
# I = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
# I.pack()
#
#
# def print_selection(v):
#     I.config(text='you have selection: ' + v)
#
#
# s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=0, variable=0, tickinterval=2, resolution=0.1, command=print_selection)
# s.pack()


# --------------------------CheckButton-----------------------------
# I = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
# I.pack()
#
#
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 1):
#         I.config(text='I love both')
#     elif (var1.get() == 1) & (var2.get() == 0):
#         I.config(text='I only love Python')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         I.config(text='I only lova C++')
#     else:
#         I.config(text='I do not love either')
#
#
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, command=print_selection)
# c2 = tk.Checkbutton(window, text=' C++  ', variable=var2, onvalue=1, command=print_selection)
# c1.pack()
# c2.pack()


# --------------------------Canvas 画布-----------------------------
# canvs = tk.Canvas(window, bg='gray', height=300, width=500)
# image_file = tk.PhotoImage(file='C:\\Users\\wangyueke\\Desktop\\1.gif')
# image = canvs.create_image(100, 100, anchor='center', image=image_file)  # anchor为锚定点,锚定gif图的中间点
#
# x0, y0, x1, y1 = 200, 200, 240, 240
# line = canvs.create_line(x0, y0, x1, y1)   # 画直线
# oval = canvs.create_oval(x0, y0, x1, y1, fill='red')   # 四点确定一个矩形，在矩形中画圆
# arc = canvs.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=120, fill='red')   # 扇形，从0度开始，收到120度
# rect = canvs.create_rectangle(280, 120, 280+30, 120+30, fill='red')
# canvs.pack()
#
#
# def moveit():
#     canvs.move(rect, 0, 20)   # 移动
#
#
# b = tk.Button(window, text='move', bg='yellow', font=('宋体', 20), height=2, width=20, command=moveit).pack()


# --------------------------MenuBar 菜单-----------------------------
# I = tk.Label(window, text='', height=4, width=30, bg='yellow')
# I.pack()
# counter = 0
#
#
# def do_job():
#     global counter
#     I.config(text='do ' + str(counter))
#
#
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New', command=do_job)
# filemenu.add_command(label='Open', command=do_job)
# filemenu.add_command(label='Save', command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
# window.config(menu=menubar)


# --------------------------Frame 框架-----------------------------
# tk.Label(window, text='on the window').pack()
#
# frm = tk.Frame(window)
# frm.pack()
#
# frm_1 = tk.Frame(frm, )
# frm_1.pack(side='left')
# frm_2 = tk.Frame(frm)
# frm_2.pack(side='right')
#
# tk.Label(frm_1, text='on the frm_1').pack()
# tk.Label(frm_1, text='on the frm_1_').pack()
# tk.Label(frm_2, text='on the frm_2').pack()


# --------------------------Messagebox 窗口-----------------------------
# def hit_me():
#     # tk.messagebox.showinfo(title='Hi', message='hhhhh')   # 生成窗口
#     # tk.messagebox.showwarning(title='Hi', message='hhhhh')
#     # tk.messagebox.showerror(title='Hi', message='hhhhh')
#     # tk.messagebox.askquestion(title='Hi', message='hhhhh')   # return 'yes','no'
#     # tk.messagebox.askyesno(title='Hi', message='hhhhh')   # return True, False
#     tk.messagebox.askretrycancel(title='Hi', message='hhhhh')   # return True, False
#
#
# tk.Button(window, text='hit me', command=hit_me).pack()   # 做一个按钮


# -------------------------- pack grid place放置方式 -----------------------------
# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

# for i in range(4):   # 按格子的方式放置
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, ipady=10)   # padx设置空间周围水平方向空白区域保留大小，ipadx内部扩展

# tk.Label(window, text=1).place(x=10, y=100, anchor='nw')




# -------------------------- 实例：登录窗口emp_1 -----------------------------

# welcome image
canvs = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='C:\\Users\\wangyueke\\Desktop\\1.gif')
image = canvs.create_image(0, 0, anchor= 'nw', image=image_file)
canvs.pack(side='top')


# user information
tk.Label(window, text='User name:').place(x=50, y=150)
tk.Label(window, text='Password: ').place(x=50, y=190)

var_user_name = tk.StringVar()
var_user_name.set('emp@python.com')
var_user_pwd = tk.StringVar()
entry_user_name = tk.Entry(window, textvariable=var_user_name)   # 输入的内容保存在var_user_name
entry_user_name.place(x=160, y=150)
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, show='*')
entry_user_pwd.place(x=160, y=190)


# login and sign button
def user_login():
    global is_sign_up
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()
    try:
        with open('user_info.pickle', 'rb') as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle', 'wb') as user_file:
            user_info = {'admin': 'admin'}
            pickle.dump(user_info, user_file)
    if user_name in user_info:
        if user_pwd == user_info[user_name]:
            tk.messagebox.showinfo(title='Welcome', message=user_name + ' How are you? ')
        else:
            tk.messagebox.showerror(message='Error, your password is wrong')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome')

    if is_sign_up is True:
        user_sign_up()


def user_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')
    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)


btn_login = tk.Button(window, text='Login', command=user_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=user_sign_up)
btn_sign_up.place(x=270, y=230)


window.mainloop()











