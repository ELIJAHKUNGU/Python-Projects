from tkinter import *

#* All the librabraries
root = Tk()
root.title('Pharmacy Management System')
#Height And Width
#root.geometry(800*700)
mylabel= Label(root, text = 'Admin Panel',font=('Arial Bold',50))
mylabel.pack()

btn1= Button(root, text = 'Patient System',fg='white',bg='green',height=3,width=20)

btn2= Button(root, text = 'Hospital  System',fg='white',bg='purple',height=3,width=20)
btn1.pack()
btn2.pack()



root.mainloop()