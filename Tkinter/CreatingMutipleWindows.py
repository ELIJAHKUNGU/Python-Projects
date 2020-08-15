from tkinter import *

#* All the librabraries
root = Tk()
root.title('Pharmacy Management System')



def New_Window():
    top = Toplevel()
    label = Label(top, text="New System").pack()

btn = Button(root,text="Open a new Window",command=New_Window)
btn.pack()









root.mainloop()