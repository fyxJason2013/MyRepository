from tkinter import *


win = Tk()
win.title('批量生成文件夹')
win.geometry('500x100')
win.resizable(False, False)

def create():
    import os
    try:
        for i in range(1, int(spinbox.get())+1):
            os.mkdir(f'.//{i}')
    except FileExistsError:
        from tkinter import messagebox
        messagebox.showerror('错误', '文件夹已存在！')


label = Label(win, text='请输入要创建文件夹的个数：', font=('', 10, ''),
           fg='red')
label.grid(column=1, row=1, columnspan=2)
spinbox = Spinbox(win, from_=1, to=50)
spinbox.grid(column=4, row=1)
button = Button(win, text='创建', command=create,
                height=5, width=5)
button.grid(column=5, row=1)


mainloop()
