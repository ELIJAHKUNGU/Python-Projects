from tkinter import *


root = Tk()
def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

checkbox = Checkbutton(root,text="Check me",variable=var,onvalue="ON",offvalue="OFF")
checkbox.deselect()
checkbox.pack()
btn = Button(root,text="See the Selection",command=show).pack()

root.mainloop()