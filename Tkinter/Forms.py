from  tkinter import *
root = Tk()

e = Entry(root,width=40,borderwidth=10)
e.insert(0,"Enter your Name")
e.pack()
def click():
    #hello  = "Hello Mr:"+e.get()
    #mylabel = Label(root,text=hello)
    mylabel = Label(root,text="Hello Mr."+e.get())
    mylabel.pack()

btn = Button(root,text="Enter Your Name",command=click)
btn.pack()

root.mainloop()