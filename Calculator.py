from tkinter import *
from tkinter.font import Font
import math
from tkinter import messagebox

root= Tk()
root.title("Calculator")
root.iconbitmap(r"C:\DaTa(F)\Practice\Start_Pyton\tkinter\calculator.ico")
root.configure(background="grey15")
#Create Entry Widget
font_ = Font(size=25)
e = Entry(root,width=12,borderwidth=3,font=font_,bg="gray15",fg="ghost white")
e.grid(row=0,column=0,columnspan=4,pady=5)
e.focus()       #Auto focus the entry widget cursor

def button_click(number):
    e.insert(len(e.get())+1,number)

def button_equal():
    if len(e.get()) == 0:
        messagebox.showerror("ValueError","No value found!") 
    else:
        s = e.get()
        s = s.replace("^","**")
        try:
            res = eval(s)   
        except:
            res = "Error"
        e.delete(0,END)
        e.insert(0,res)

def string_handel(string):
    rs = string[::-1]
    val = []
    for i in rs:
        if i in ["+","-","*","/"]:
            break
        else:
            val.insert(0,i)
    return "".join(val)
    
def int_float(st):
    if "." in st:
        st = float(st)
    else:
        st = int(st)
    return st

def clear():
    e.delete(0,END)

def operator(op):
    e.insert(len(e.get())+1,op)

#Square Function
def square(z):
    n = e.get()
    if n == "":
        e.insert(0,0)
    else:
        total_len =  len(e.get())
        s = string_handel(e.get())          #string_handle returns a string
        length = total_len-len(s)
        num = int_float(s)
        if z==1:
            e.delete(length,END)
            e.insert(length+1,num**2)           #sqr
        elif z==2:
            e.delete(length,END)
            e.insert(length+1,math.sqrt(num))   #sqrt
        elif z==3:
            e.insert(len(n)+1,"^")              #Power
        elif z==4:
            e.insert(len(e.get())+1,"%")         #Modulo

    
#Pi Function
def button_pii():
    e.insert(len(e.get())+1,3.14)

#factorial Function
def factorial():
    n = e.get()
    if n == "":
        e.insert(0,0)
    else:
        total_len =  len(e.get())
        s = string_handel(e.get())          
        length = total_len-len(s)
        if "." in s:
            messagebox.showerror("ValueError","Factorial() only accepts integral values")
        else:
            s = int(s)
            e.delete(length,END)
            e.insert(length+1,math.factorial(s))

def log_(n):
    num = e.get()
    if len(num) == 0:
        e.insert(0,"Invalid Input")
    else:
        total_len =  len(e.get())
        s = string_handel(e.get())          
        length = total_len-len(s)
        num = int_float(s)
        e.delete(length,END)
        if n=="1":
            e.insert(length+1,math.log10(num))      #log base 10
        else:
            e.insert(length+1,math.log(num))    #Natural log

def back():
    s = e.get()
    e.delete(0,END)
    e.insert(0,s[:-1])
    
btn_font = Font(size=12)
#Creating Buttons 
button_clear = Button(root,text="CLR",font=btn_font,command=clear,height=2,width=5,bg="gray15",fg="ghost white",bd=0)
button_1 = Button(root,text="1",font=btn_font,command=lambda : button_click(1),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_2 = Button(root,text="2",font=btn_font,command=lambda : button_click(2),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_3 = Button(root,text="3",font=btn_font,command=lambda : button_click(3),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_4 = Button(root,text="4",font=btn_font,command=lambda : button_click(4),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_5 = Button(root,text="5",font=btn_font,command=lambda : button_click(5),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_6 = Button(root,text="6",font=btn_font,command=lambda : button_click(6),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_7 = Button(root,text="7",font=btn_font,command=lambda : button_click(7),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_8 = Button(root,text="8",font=btn_font,command=lambda : button_click(8),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_9 = Button(root,text="9",font=btn_font,command=lambda : button_click(9),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_0 = Button(root,text="0",font=btn_font,command=lambda : button_click(0),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_div = Button(root,text="/",font=btn_font,command=lambda:operator("/"),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_mul = Button(root,text="*",font=btn_font,command=lambda:operator("*"),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_min = Button(root,text="-",font=btn_font,command=lambda:operator("-"),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_plus = Button(root,text="+",font=btn_font,command=lambda:operator("+"),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_eq = Button(root,text="=",font=btn_font,command=button_equal,height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_dot = Button(root,text=".",font=btn_font,command=lambda:operator("."),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_mod = Button(root,text="%",font=btn_font,command=lambda:square(4),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_pi = Button(root,text="π",font=btn_font,command=button_pii,height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_sqr = Button(root,text="x²",font=btn_font,command=lambda:square(1),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_sqrt = Button(root,text="√x",font=btn_font,command=lambda:square(2),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_pow = Button(root,text="pow",font=btn_font,command=lambda:square(3),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_fact = Button(root,text="n!",font=btn_font,command=factorial,height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_back = Button(root,text="←",font=btn_font,command=back,height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_log = Button(root,text="log",font=btn_font,command=lambda:log_(1),height=3,width=5,bg="gray15",fg="ghost white",bd=0)
button_ln = Button(root,text="ln",font=btn_font,command=lambda:log_(2),height=3,width=5,bg="gray15",fg="ghost white",bd=0)

#Placing buttons in grid
button_clear.grid(row=0,column=4)
button_sqrt.grid(row=1,column=0)
button_sqr.grid(row=1,column=1)
button_pow.grid(row=1,column=2)
button_fact.grid(row=1,column=3)
button_back.grid(row=1,column=4)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_div.grid(row=2,column=3)
button_mod.grid(row=2,column=4)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_plus.grid(row=3,column=3)
button_mul.grid(row=3,column=4)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_min.grid(row=4,column=3)
button_ln.grid(row=4,column=4)
button_dot.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_pi.grid(row=5,column=2)
button_log.grid(row=5,column=3)
button_eq.grid(row=5,column=4)

root.mainloop()