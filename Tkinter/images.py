from tkinter import *
from PIL import ImageTk,Image


root = Tk()
my_img = ImageTk.PhotoImage(Image.open("images/image.jpeg"))
my_label =Label(image = my_img)
my_label.pack()


button_quit =Button(root,text="Exit program",command=root.quit)
button_quit.pack()



root.mainloop()