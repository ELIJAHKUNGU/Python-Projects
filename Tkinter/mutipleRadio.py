from tkinter import *

root = Tk()

MODES = [
    ("Pepperoni","Perpperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza = StringVar()
#pizza.set("Pepperoni")


for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    mylabel=Label(root,text=value)
    mylabel.pack(anchor=W)



mylabel=Label(root,text=pizza.get()).pack(anchor=W)

myButton=Button(root,text="Order", command=lambda :clicked(pizza.get())).pack(anchor=W)
root.mainloop()