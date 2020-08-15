from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image View App")

img1 = ImageTk.PhotoImage(Image.open("images/image.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("images/hoho.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("images/mt.jpeg"))
img4 = ImageTk.PhotoImage(Image.open("images/comp.jpeg"))
img5 = ImageTk.PhotoImage(Image.open("images/SC.jpeg"))
img6 = ImageTk.PhotoImage(Image.open("images/Ocean.jpeg"))
img7 = ImageTk.PhotoImage(Image.open("images/SiliconValley.png"))


image_list = [img1,img2,img3,img4,img5,img6,img7]
status = Label(root,text="Image 1 0ut of  " +str(len(image_list)),bd=2,relief=SUNKEN,anchor =E)
my_label =Label(image = img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global btn_back
    global btn_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[-1])


    btn_forward = Button (root,text = ">>",command = lambda :forward(image_number +1))
    btn_back = Button(root, text="<<", command=lambda :back(image_number-1))
    status = Label(root, text="Image "+str(image_number)+" 0ut of  " + str(len(image_list)), bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    if image_number == 7:
        btn_forward = Button(root,text = ">>",state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_forward.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)


def back(image_number):
    global my_label
    global btn_back
    global btn_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[-1])


    btn_forward = Button (root,text = ">>",command = lambda :forward(image_number +1))
    btn_back = Button(root, text="<<", command=lambda :back(image_number-1))


    if image_number == 1:
        btn_forward = Button(root,text = ">>",state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    btn_forward.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)


btn_back = Button(root,text="<<",command=back ,state=DISABLED)
btn_quit = Button(root,text="Exit Program" ,command=root.quit)
btn_forward = Button(root,text=">>",command=lambda :forward(2))

btn_back.grid(row=1,column=0)
btn_quit.grid(row=1,column=1)
btn_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)




root.mainloop()