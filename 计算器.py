from tkinter import *
from math import *


def close_question_show():
    from tkinter import messagebox
    if messagebox.askyesno('退出', '您想要退出吗?'):
        win.quit()


win = Tk()
win.title('计算器')
win.geometry('700x200')
win.resizable(False, False)
win.protocol("WM_DELETE_WINDOW", close_question_show)


def fill(text):
    entry.insert(INSERT, f'{text}')


def cal():
    if len(var_2.get()) != 0:
        entry_2.delete(0, END)
    else:
        pass
    val = eval(var.get())
    entry_2.insert(INSERT, '='+str(val))


def delete():
    entry.delete(len(var.get())-1, END)


def ac():
    entry.delete(0, END)
    entry_2.delete(0, END)


def science_mode():
    win.geometry('900x200')
    button_21 = Button(win, text='sin', command=lambda: fill('sin('), width=15)
    button_21.grid(column=5, row=1)
    button_22 = Button(win, text='cos', command=lambda: fill('cos('), width=15)
    button_22.grid(column=6, row=1)
    button_23 = Button(win, text='tan', command=lambda: fill('tan('), width=15)
    button_23.grid(column=5, row=2)
    button_24 = Button(win, text='阶乘', command=lambda: fill('factorial('), width=15)
    button_24.grid(column=6, row=2)
    button_25 = Button(win, text='π', command=lambda: fill('pi'), width=15)
    button_25.grid(column=5, row=3)
    button_26 = Button(win, text='e', command=lambda: fill('e'), width=15)
    button_26.grid(column=6, row=3)


var = StringVar()
var_2 = StringVar()
entry = Entry(win, textvariable=var)
entry.grid(column=1, row=0)
entry_2 = Entry(win, textvariable=var_2)
entry_2.grid(column=3, row=0)
lb = Label(win, text='算式:')
lb.grid(column=0, row=0)
lb2 = Label(win, text='结果:')
lb2.grid(column=2, row=0)
button = Button(win, text='1', command=lambda: fill('1'), width=15)
button.grid(column=0, row=2)
button_2 = Button(win, text='2', command=lambda: fill('2'), width=15)
button_2.grid(column=1, row=2)
button_3 = Button(win, text='3', command=lambda: fill('3'), width=15)
button_3.grid(column=2, row=2)
button_4 = Button(win, text='4', command=lambda: fill('4'), width=15)
button_4.grid(column=3, row=2)
button_5 = Button(win, text='5', command=lambda: fill('5'), width=15)
button_5.grid(column=4, row=2)
button_6 = Button(win, text='6', command=lambda: fill('6'), width=15)
button_6.grid(column=0, row=3)
button_7 = Button(win, text='7', command=lambda: fill('7'), width=15)
button_7.grid(column=1, row=3)
button_8 = Button(win, text='8', command=lambda: fill('8'), width=15)
button_8.grid(column=2, row=3)
button_9 = Button(win, text='9', command=lambda: fill('9'), width=15)
button_9.grid(column=3, row=3)
button_10 = Button(win, text='0', command=lambda: fill('0'), width=15)
button_10.grid(column=4, row=3)
button_11 = Button(win, text='+', command=lambda: fill('+'), width=15)
button_11.grid(column=0, row=1)
button_12 = Button(win, text='-', command=lambda: fill('-'), width=15)
button_12.grid(column=1, row=1)
button_13 = Button(win, text='*', command=lambda: fill('*'), width=15)
button_13.grid(column=2, row=1)
button_14 = Button(win, text='/', command=lambda: fill('/'), width=15)
button_14.grid(column=3, row=1)
button_15 = Button(win, text='=', command=cal, width=15)
button_15.grid(column=4, row=1)
button_16 = Button(win, text='退格', command=delete, width=15)
button_16.grid(column=0, row=4)
button_17 = Button(win, text='AC', command=ac, width=15)
button_17.grid(column=1, row=4)
button_18 = Button(win, text='(', command=lambda: fill('('), width=15)
button_18.grid(column=2, row=4)
button_19 = Button(win, text=')', command=lambda: fill(')'), width=15)
button_19.grid(column=3, row=4)
button_20 = Button(win, text='退出', command=close_question_show, width=15)
button_20.grid(column=4, row=4)
main_menu = Menu(win)
menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='选项', menu=menu)
menu.add_command(label='科学计算器', command=science_mode)
menu.add_command(label='退出', command=close_question_show)
win.configure(menu=main_menu)
mainloop()
