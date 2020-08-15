from tkinter import *

root= Tk()
root.title("Simple Calculator")

e = Entry(root,borderwidth = 10,width=40)
e.grid(row=0, column=0,columnspan =3, padx=10, pady=10)

def button_click(number):
   # e.delete(0,END)
   current= e.get()
   e.delete(0,END)
   e.insert(0,str(current) + str(number))

def clear_button():
    e.delete(0,END)
def button_add():
    first_number = e.get()
    global f_num
    global math
    math= "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "substraction":
        e.insert(0, f_num - int(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_mutiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_divides():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#Defining the buttons
btn1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
btn2 = Button(root,text="2",padx=40,pady=20,command=lambda :button_click(2))
btn3 = Button(root,text="3",padx=40,pady=20,command=lambda :button_click(3))
btn4 = Button(root,text="4",padx=40,pady=20,command=lambda :button_click(4))
btn5 = Button(root,text="5",padx=40,pady=20,command=lambda :button_click(5),)
btn6 = Button(root,text="6",padx=40,pady=20,command=lambda :button_click(6))
btn7 = Button(root,text="7",padx=40,pady=20,command=lambda :button_click(7))
btn8 = Button(root,text="8",padx=40,pady=20,command=lambda :button_click(8))
btn9 = Button(root,text="9",padx=40,pady=20,command=lambda :button_click(9))
btn0 = Button(root,text="0",padx=40,pady=20,command=lambda :button_click(0))
btn_add = Button(root,text="+",padx=39,pady=20,command=button_add)

btn_sub = Button(root,text="-",padx=40,pady=20,command=button_sub)
btn_mutiply = Button(root,text="X",padx=41,pady=20,command=button_mutiply)
btn_division = Button(root,text="/",padx=41,pady=20,command=button_divides)

btn_clear = Button(root,text="Clear",padx=78,pady=20,command=clear_button)
btn_equal= Button(root,text="=",padx=87,pady=20,command=button_equal)


#displaying the buttons
btn1.grid(row =3 ,column=0)
btn2.grid(row =3,column=1)
btn3.grid(row =3 ,column=2)

btn4.grid(row =2 ,column=0)
btn5.grid(row =2 ,column=1)
btn6.grid(row =2 ,column=2)

btn7.grid(row =1 ,column=0)
btn8.grid(row =1 ,column=1)
btn9.grid(row =1 ,column=2)

btn0.grid(row =4 ,column=0)
btn_add.grid(row =5 ,column=0)
btn_clear.grid(row =6 ,column=1,columnspan=2)
btn_equal.grid(row =4 ,column=1,columnspan=2)

btn_sub.grid(row =6 ,column=0)
btn_mutiply.grid(row =5 ,column=1)
btn_division.grid(row=5 ,column=2)

root.mainloop()