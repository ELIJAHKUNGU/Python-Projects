from tkinter import *
from tkinter import  filedialog
from PIL import ImageTk,Image
root= Tk()





def open():
    global my_imagr
    root.filename = filedialog.asksaveasfilename(initialdir="/C:Users/hp2\PycharmProjects/Tkinter/images",
                                                 title="Select A File",
                                                 filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()

    my_imagr = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_imagr).pack()


btn_open = Button(root,text="Open File",command=open).pack()






root.mainloop()