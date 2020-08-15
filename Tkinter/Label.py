from tkinter import *

root = Tk()
root.title("Hello Tkinter")

#intialiaze
myLbel = Label(root ,text="Hello wold!")
myLabel = Label(root ,text="rising Cock!").grid(row =10 , column= 8)
#display on the screen
#myLbel.pack()
myLbel.grid(row =0 , column= 0)


root.mainloop()

