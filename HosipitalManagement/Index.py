from tkinter import *
from  tkinter import messagebox


root = Tk()
root.title("Pharmacy Management System")

# Creating a frame
frame = LabelFrame(root, padx=40, pady=10)
frame.grid(row=0, column=1, padx=10, pady=10, columnspan=20)


title = Label(frame, text="Pharmacy Management System", font="Bold  50")
title.grid(row=0, column=2, columnspan=20)


# To create a space btwn  the title  and entry


def clear_button():
    e.delete(0, END)
    password.delete(0,END)
def button_exit():
    #messagebox.showinfo("Message Box","Delete")
    #messagebox.showwarning("Message Box","Delete")
    response=messagebox.askyesno("Exit System","Are sure you want Exit From System")

    #Label(root,text=response).pack()
    if response ==1:
        #Label(root,text="You clicked Yes!!")
        root.quit()
    else:
        messagebox.askyesno("Confirmation Message", "Press Yes to Continue")







frame1 = LabelFrame(root, padx=10, pady=10, borderwidth=10)
frame1.grid(row=2, column=5, padx=10, pady=10, columnspan=20)

e = Entry(frame1, width=100, borderwidth=10)
e.insert(0, "Enter your Username" )
mylabel = Label(frame1, text="Username:", font="Bold 20")

password = Entry(frame1, width=100, borderwidth=10, )
password.insert(0, "Enter your Password")
mypass = Label(frame1, text="Password:", font="Bold 20")

mylabel.grid(row=3, column=2)
e.grid(row=3, column=3, columnspan=3)
mypass.grid(row=4, column=2)
password.grid(row=4, column=3, columnspan=3)

frame2 = LabelFrame(frame1, padx=10, pady=10, )
frame2.grid(row=5, column=3, padx=10, pady=10, columnspan=2)

btnlogin = Button(frame2, text="Login", width=28)
btnregister = Button(frame2, text="Reset", width=25, command=clear_button)
button_quit = Button(frame2, text="Exit program", command=button_exit)

btnlogin.grid(row=6, column=3)
btnregister.grid(row=6, column=4)
button_quit.grid(row=6, column=5)

frame3 = LabelFrame(frame1, padx=10, pady=10, )
frame3.grid(row=7, column=3, padx=10, pady=10, columnspan=2)

frame4 = LabelFrame(frame3, padx=10, pady=10, )
frame4.grid(row=8, column=3, padx=10, pady=10, columnspan=2)


#New window
def new_window():
    top = Toplevel()
    top.title("Pharmacy Management System")
    label =Label(top,text="A New Window").pack()
    btn = Button(top,text="Close Window",command=top.destroy).pack()




btnHospital1 = Button(frame4, text="Pharmacy  Management", width=25,command=new_window)
btnHospital1.grid(row=9, column=4, columnspan=2)

frame5 = LabelFrame(frame3, padx=10, pady=10, )
frame5.grid(row=8, column=5, padx=10, pady=10, columnspan=2)

btnHospital = Button(frame5, text="Hospital  Management", width=25,command=new_window)
btnHospital.grid(row=9, column=5, columnspan=2)

root.mainloop()
