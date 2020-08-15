from tkinter import *

root = Tk()
root.geometry("400x400")
vertical_slider = Scale(root,from_=0,to=1000,bg="Blue")
vertical_slider.pack()


def slide(var):
    my_label = Label(root,text=horizontal_slider.get()).pack()
    root.geometry(str(horizontal_slider.get()+"x400"))

horizontal_slider = Scale(root,from_=0,to=1000,bg="Blue",orient=HORIZONTAL,command=slide)
horizontal_slider.pack()
my_label = Label(root,text=horizontal_slider.get()).pack()


#def slide():
   # my_label = Label(root,text=horizontal_slider.get()).pack()
    #root.geometry(str(horizontal_slider.get())+"x400")


btn = Button(root,text="Click Me!",command=slide).pack()

root.mainloop()