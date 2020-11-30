
import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title('Calculator')
win.geometry('310x160')
win.resizable(0,0)
win.configure(background='grey')


scvalue = tk.StringVar()
scvalue.set('')
screen = ttk.Entry(win , textvariable=scvalue)
screen.grid(row=0,columnspan=5,sticky='nsew')


# text = tk.StringVar()
exp = ''
num = ''
def cancel(event=None):
    global exp
    exp = ''
    scvalue.set(exp)


def press(num):
    global exp
    exp += str(num)
    scvalue.set(exp)

def equal(event=None):
    global exp
    try:
        t = str(eval(exp))
        scvalue.set(t)
    except SyntaxError:
        scvalue.set('Error')


c_btn = ttk.Button(win,text='C',command=cancel)
c_btn.grid(row=1,column=0)


plus_btn = ttk.Button(win , text='+',command=lambda:press('+'))
plus_btn.grid(row=1,column=1)


minus_btn = ttk.Button(win , text='-',command=lambda:press('-'))
minus_btn.grid(row=1,column=2)

div_btn = ttk.Button(win , text='/',command=lambda:press('/'))
div_btn.grid(row=1,column=3)

X_btn = ttk.Button(win,text='X',command=lambda:press('*'))
X_btn.grid(row=3,column=3)

per_btn = ttk.Button(win,text='%',command=lambda:press('%'))
per_btn.grid(row=2,column=3)



seven_btn = ttk.Button(win,text='7',command=lambda:press('7'))
seven_btn.grid(row=2,column=0)

four_btn = ttk.Button(win,text='4',command=lambda:press('4'))
four_btn.grid(row=3,column=0)




one_btn = ttk.Button(win,text='1',command=lambda:press('1'))
one_btn.grid(row=4,column=0)


# column 2

eight_btn = ttk.Button(win,text='8',command=lambda:press('8'))
eight_btn.grid(row=2,column=1)


five_btn = ttk.Button(win,text='5',command=lambda:press('5'))
five_btn.grid(row=3,column=1)


two_btn = ttk.Button(win,text='2',command=lambda:press('2'))
two_btn.grid(row=4,column=1)





nine_btn = ttk.Button(win,text='9',command=lambda:press('9'))
nine_btn.grid(row=2,column=2)

six_btn = ttk.Button(win,text='6',command=lambda:press('6'))
six_btn.grid(row=3,column=2)

three_btn = ttk.Button(win,text='3',command=lambda:press('3'))
three_btn.grid(row=4,column=2)

zero_btn = ttk.Button(win,text='0',command=lambda:press('0'))
zero_btn.grid(row=4,column=3)

equal_btn = ttk.Button(win,text='=',command=equal)
equal_btn.grid(row=5,columnspan=3,sticky='nsew')

dec_btn = ttk.Button(win,text='.',command=lambda:press('.'))
dec_btn.grid(row=5,column=3)




win.mainloop()


