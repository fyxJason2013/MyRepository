from tkinter import *
import random as r



win = Tk()
win.title('抢答')
win.geometry('300x200')
win.resizable(False, False)


def show_t():
    string = int(lb2.cget('text')) + 1
    lb2.config(text=string)
    lb2.after(1000, show_t)


def clicked1():
    from tkinter import messagebox
    if int(entry1.get()) == eval(f'{a} {what} {b}'):
        messagebox.showinfo('提示', '恭喜您计算正确，您赢了。用时：%01d秒' % lb2.cget('text'))
        win.destroy()
    else:
        messagebox.showinfo('提示', '很遗憾，您计算错误，请继续作答。')


r.seed(r.randint(1, 1000000000))
a = r.randint(1, 100)
b = r.randint(1, 100)
ran = r.randint(1, 2)
c = a + b if ran == 1 else a - b
what = "+" if ran == 1 else '-'

lb1 = Label(win, fg="blue", text=str(a) + what + str(b) + '=')
lb1.grid(column=1, row=0)
lb2 = Label(win, fg='red', font=('微软雅黑', 10, 'bold'),
            text='0')
lb2.grid(column=0, row=0)

entry1 = Entry(win)
entry1.grid(column=0, row=2)
entry1.focus()


button1 = Button(win, text='抢答', bg='red', command=clicked1, width=10, height=9)
button1.grid(column=0, row=3)


show_t()
mainloop()
