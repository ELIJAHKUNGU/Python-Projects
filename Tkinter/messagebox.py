from tkinter import *
from  tkinter import messagebox


root= Tk()

#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
def clicked():
    #messagebox.showinfo("Message Box","Delete")
    #messagebox.showwarning("Message Box","Delete")
    response=messagebox.askyesno("Message Box","Exit the message box")

    #Label(root,text=response).pack()
    if response ==1:
        #Label(root,text="You clicked Yes!!")
        root.quit()
    else:
        messagebox.askyesno("Message Box", "Exit the message box")


btn = Button(root,text="Message", command=clicked).pack()





root.mainloop()