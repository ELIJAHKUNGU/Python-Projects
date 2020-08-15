from tkinter import *
root = Tk()

def myclick():
    myLabel = Label(root,text="I clicked the button")
    myLabel.pack()

def Name():
    myLabel1 = Label(root,text="Print the Name:Elijah",fg="purple",font=("Arial",50))
    myLabel1.pack()


mybutton = Button(root,text="Click the Button",command=myclick,)
btn1 = Button(root,text="Name",padx=50,pady=40,command=Name,bg="purple")
btn2 = Button(root , text="Click me" ,state = DISABLED,padx =50)

btn1.pack()
btn2.pack()
mybutton.pack()

root.mainloop()



