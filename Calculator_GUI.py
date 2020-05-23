from tkinter import *
import math
root = Tk()
root.title("Simple Calculator")
e = Entry(root,width = 35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0, END)
def button_add():
    first_num = e.get()
    global f_num
    global math1
    math1 = "addition"
    #f_num = int(first_num)
    f_num = first_num
    e.delete(0, END)
def button_sub():
    first_num = e.get()
    global f_num
    global math1
    math1 = "subtraction"
    #f_num = int(first_num)
    f_num = first_num
    e.delete(0, END)
def button_mul():
    first_num = e.get()
    global f_num
    global math1
    math1 = "multiplication"
    #f_num = int(first_num)
    f_num = first_num
    e.delete(0, END)
def button_div():
    first_num = e.get()
    global f_num
    global math1
    math1 = "division"
    #f_num = int(first_num)
    f_num = first_num
    e.delete(0, END)
def button_sqrt():
    first_num = e.get()
    global f_num
    global math1
    math1 = "sqrt"
    f_num = first_num
    e.delete(0, END)
def button_pow():
    first_num = e.get()
    global f_num
    global math1
    math1 = "pow"
    f_num = first_num
    e.delete(0, END)
def button_fact():
    first_num = e.get()
    global f_num
    global math1
    math1 = "fact"
    f_num = first_num
    e.delete(0, END)
def button_loge():
    first_num = e.get()
    global f_num
    global math1
    math1 = "loge"
    f_num = first_num
    e.delete(0, END)
def button_log():
    first_num = e.get()
    global f_num
    global math1
    math1 = "log"
    f_num = first_num
    e.delete(0, END)
def button_sin():
    first_num = e.get()
    global f_num
    global math1
    math1 = "sin"
    f_num = first_num
    e.delete(0, END)
def button_cos():
    first_num = e.get()
    global f_num
    global math1
    math1 = "cos"
    f_num = first_num
    e.delete(0, END)
def button_tan():
    first_num = e.get()
    global f_num
    global math1
    math1 = "tan"
    f_num = first_num
    e.delete(0, END)
def button_exp():
    first_num = e.get()
    global f_num
    global math1
    math1 = "exp"
    f_num = first_num
    e.delete(0, END)
def button_inv():
    first_num = e.get()
    global f_num
    global math1
    math1 = "inv"
    f_num = first_num
    e.delete(0, END)
def button_point():
    first_num = e.get()
    e.delete(0, END)
    e.insert(0,str(first_num)+".")


def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math1 == "addition":
        e.insert(0,float(f_num)+float(second_num))
    elif math1 == "subtraction":
        e.insert(0, float(f_num) - float(second_num))
    elif math1 == "multiplication":
        e.insert(0, float(f_num) * float(second_num))
    elif math1 == "division":
        e.insert(0, float(f_num) / float(second_num))
    elif math1 == "sqrt":
        e.insert(0, math.sqrt(float(f_num)))
    elif math1 == "pow":
        e.insert(0, float(f_num)**float(second_num))
    elif math1 == "fact":
        e.insert(0, math.factorial(int(f_num)))
    elif math1 == "loge":
        e.insert(0, math.log(float(f_num)))
    elif math1 == "log":
        e.insert(0, math.log(float(f_num),10))
    elif math1 == "sin":
        e.insert(0, math.sin(float(f_num)))
    elif math1 == "cos":
        e.insert(0, math.cos(float(f_num)))
    elif math1 == "tan":
        e.insert(0, math.tan(float(f_num)))
    elif math1 == "exp":
        e.insert(0, math.exp(float(f_num)))
    elif math1 == "inv":
        e.insert(0, 1/float(f_num))

button_0 = Button(root,text="0",padx=40,pady=20, command=lambda:button_click(0))
button_1 = Button(root,text="1",padx=40,pady=20, command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20, command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20, command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20, command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20, command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20, command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20, command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20, command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20, command=lambda:button_click(9))
button_equal = Button(root,text="=",padx=39,pady=20, command=button_equal)
button_add = Button(root,text="+",padx=40,pady=20, command=button_add)
button_clear = Button(root,text="Clear",padx=30,pady=20, command=button_clear)
button_subtract = Button(root,text="-",padx=40,pady=20, command=button_sub)
button_multiply = Button(root,text="*",padx=40,pady=20, command=button_mul)
button_divison = Button(root,text="/",padx=40,pady=20, command=button_div)
button_sqrt = Button(root,text="-\/",padx=36,pady=20, command=button_sqrt)
button_power = Button(root,text="^",padx=40,pady=20, command=button_pow)
button_factorial = Button(root,text="!",padx=40,pady=20, command=button_fact)
button_loge = Button(root,text="ln",padx=36,pady=20, command=button_loge)
button_log10 = Button(root,text="log",padx=34,pady=20, command=button_log)
button_sine = Button(root,text="sin",padx=35,pady=20, command=button_sin)
button_cosine = Button(root,text="cos",padx=34,pady=20, command=button_cos)
button_tan = Button(root,text="tan",padx=34,pady=20, command=button_tan)
button_exp = Button(root,text="exp",padx=34,pady=20, command=button_exp)
button_inv = Button(root,text="1/x",padx=34,pady=20, command=button_inv)
button_point = Button(root,text=".",padx=40,pady=20, command=button_point)
button_1.grid(row=3, column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)
button_add.grid(row=1 ,column=3)
button_divison.grid(row=4 ,column=3)
button_multiply.grid(row=3 ,column=3)
button_subtract.grid(row=2 ,column=3 )
button_power.grid(row=1,column=4)
button_sqrt.grid(row=2 ,column=4)
button_factorial.grid(row=3, column=4)
button_loge.grid(row=4 ,column=4)
button_log10.grid(row=4 ,column=1)
button_sine.grid(row=4 ,column=2)
button_cosine.grid(row=5 ,column=0)
button_tan.grid(row=5 ,column=1)
button_exp.grid(row=5 ,column=2)
button_inv.grid(row=5 ,column=3)
button_point.grid(row=5 ,column=4)
button_0.grid(row=4 ,column=0)
button_equal.grid(row=6 ,column=0)
button_clear.grid(row=6 ,column=1)
root.mainloop()