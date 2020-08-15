from tkinter import *
root = Tk()


def show():
    myLabel = Label(root, text=Clicked.get()).pack()


#Dropdown menu
options = [
     "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"

       ]

Clicked = StringVar()
Clicked.set(options[0])
dropdown_menu= OptionMenu(root,Clicked,*options)
dropdown_menu.pack()
btn = Button(root,text="See the Selection",command=show).pack()

root.mainloop()