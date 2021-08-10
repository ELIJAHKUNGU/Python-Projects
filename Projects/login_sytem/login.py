from tkinter import *


main_screen = Tk()   # create a GUI window 
main_screen.geometry("300x250") # set the configuration of GUI window 
main_screen.title("Account Login") # set the title of GUI window

def login():
    login = Toplevel()
    login.geometry("300x250")
    label_title = Label(login, text="Login User")
    label_title.grid(row=0, column=3)


 
def register():
    register_screen = Toplevel() 
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    # Set text variables
    username = StringVar()
    password = StringVar()
    
    # Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
        
    # Set username label
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    
    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
        
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    # Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
    # Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen ,text="Register", height="2", width="30", command=register_user).pack()


    
    

def register_user():


    # get username and password
    username_info = username.get()
    password_info = password.get()

    # Open file in write mode
    file = open(username_info, "w")

    # write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    # set a label for showing success information on screen 

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    # Set register button






btn_login = Button(main_screen, text='Login',command=login).pack()
buttn_register = Button(main_screen, text='Register', command=register).pack()

main_screen.mainloop()

