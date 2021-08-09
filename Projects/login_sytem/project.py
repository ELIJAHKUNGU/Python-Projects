from tkinter import *

root = Tk()
root.geometry("500x300")
#root.resizable(False , False)

#get values function
def getvals():
    return


label_title = Label(root, text="Python Registration Form", font="ar 15 bold")
label_title.grid(row=0,column=3)
#declaring the variables
label_name = Label(root, text="Name")
label_phone = Label(root, text="Phone")
label_gender = Label(root, text="Gender")
label_emergency = Label(root, text="Emergency")
label_paymentmode = Label(root, text="Payment Mod")
#Packing the variables
label_name.grid(row=1,column=2)
label_phone.grid(row=2,column=2)
label_gender.grid(row=3,column=2)
label_emergency.grid(row=4,column=2)
label_paymentmode.grid(row=5,column=2)

#Declaring Variables
namevalue = StringVar
gendervar = StringVar
phonevalue = StringVar
emergencyvalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

#Entry box
nameentry = Entry (root, textvariable=namevalue)
phoneentry = Entry (root, textvariable=phonevalue)
genderentry = Entry (root, textvariable=gendervar)
paymententry = Entry (root, textvariable=paymentvalue)
emergencyentry = Entry (root, textvariable=emergencyvalue)
#packing
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymententry.grid(row=4, column=3)
emergencyentry.grid(row=5, column=3)
#single checkbox remember me
checkbtn = Checkbutton(root, text="Remember me" ,variable=checkvalue)
checkbtn.grid(row=6, column=3)
#submit button
submit_btn = Button(root, text="Sumit", command=getvals)

root.mainloop()