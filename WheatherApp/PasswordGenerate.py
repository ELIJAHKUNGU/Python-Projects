from tkinter import *
import random


root = Tk()
root.title('Password Generate')
root.geometry("400x50")



def passwordGenerate():


    lower_chars = ["a","b","c","d","e"]
    upper_chars = ["A","B","C","D","E"]
    special_chars = ["@","#","$","%","&"]
    numerical_chars = [1,2,3,4,5,6]

    password = random.choice(lower_chars)+random.choice(upper_chars)+random.choice(special_chars)+str(random.choice(numerical_chars))
    password = password + password

    label = Label(root, text=str(password.get()))
    label.grid(row=1, column=0, columnspan=2)


password_entry = Entry(root)
password_entry.grid(row=0,column=0,padx=20)

#Button to generate the password
btn = Button(root,text="Generate the password",command=passwordGenerate)
btn.grid(row=0,column=1)



root.mainloop()