from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login System')
        self.root.resizable(False, False)
        self.root.geometry("1199x600+100+50")
        #Background image
        # file = 'images/bg.jpg'
        # image = file
        main_frame = Frame(bg="red")
        main_frame.place(x= 0 , y=0, relwidth=1 ,relheight=1)
        # self.bg=ImageTk.PhotoImage(image)
        # self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)

        #LOgin frame
        frame_login = Frame(self.root, bg='blue')
        frame_login.place(x=300,y =150, width=500, height=400)



root = Tk()
obj = Login(root)
root.mainloop()
        
