from tkinter import  *


root = Tk()
frame = LabelFrame(root , text = "This a frame", padx =100 ,pady=100)
frame.pack(padx=100,pady =100)

btn = Button(frame , text = "Button")
btn.pack()




root.mainloop()