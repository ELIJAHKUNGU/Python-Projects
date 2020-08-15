from tkinter import *
import sqlite3
from  tkinter import messagebox


root =Tk()
root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
root.configure(background="yellow")
root.geometry("1350x700")



Mainframe = LabelFrame(root,bg="red")
Mainframe.grid()

title_frame = LabelFrame(Mainframe, bd=1,padx=50, pady=10,background="white",relief=RIDGE)
title_frame.pack(side=TOP)

label_title = Label(title_frame,text="Warehouse Inventory Sales Purchase ",font=("Arial Bold",50),fg="red")
label_title.grid()

#Database
#Creating a database
connect = sqlite3.connect('invetory_book.db')
#create a cursor
cursor = connect.cursor()

#Creating a table
#cursor.execute("""CREATE TABLE products(
             #p_id integer ,
             #name_item text,
             #price_item integer ,
             #quality text,
             #manufacturer text,
            # contacts integer)""")


def Close():
    #messagebox.showinfo("Message Box","Delete")
    #messagebox.showwarning("Message Box","Delete")
    response=messagebox.askyesno("Warehouse Inventory Sales Purchase","Are You sure want Close the Program")

    #Label(root,text=response).pack()
    if response ==1:
        #Label(root,text="You clicked Yes!!")
        root.quit()
    else:
        messagebox.askyesno("Warehouse Inventory Sales Purchase", "Click Yes to continue")



    #messagebox.showinfo("Message Box","Delete")
    #messagebox.showwarning("Message Box","Delete")
    response=messagebox.askyesno("Warehouse Inventory Sales Purchase","Are You sure want Close the Program")

    #Label(root,text=response).pack()
    if response ==1:
        #Label(root,text="You clicked Yes!!")
        root.quit()
    else:
        messagebox.askyesno("Warehouse Inventory Sales Purchase", "Click Yes to continue")


def Submit():
    # Connecting to the database
    connect = sqlite3.connect('invetory_book.db')
    # create a cursor
    cursor = connect.cursor()

    # if(len(entry_pid.get() !=0) and len(entry_name.get()) and len(entry_qty.get()) and len(entry_price.get())
    # and len(entry_company.get()) and len(entry_contact.get())):
    # Insert into Table
    cursor.execute("INSERT INTO products VALUES"
                   " (:entry_pid,:entry_name,:entry_price,:entry_qty,:entry_company,:entry_contact)",
                   {
                       'entry_pid': entry_pid.get(),
                       'entry_name': entry_name.get(),
                       'entry_price': entry_price.get(),
                       'entry_qty': entry_qty.get(),
                       'entry_company': entry_company.get(),
                       'entry_contact': entry_contact.get()
                   })

    messagebox.showinfo("Warehouse Inventory Sales Purchase", "Data Added Successfully")

    entry_pid.delete(0, END)
    entry_name.delete(0, END)
    entry_price.delete(0, END)
    entry_qty.delete(0, END)
    entry_company.delete(0, END)
    entry_contact.delete(0, END)
    # commit changes
    connect.commit()

    # Close connection
    connect.close()

def show():
            # Connecting to the  database
            connect = sqlite3.connect('invetory_book.db')

            # create a cursor
            cursor = connect.cursor()

            # Query the database
            cursor.execute("SELECT *,oid FROM products")
            records = cursor.fetchall()
            # print(records)

            # Loop thru results
            print_records = ''
            for record in records:
                print_records += str(record) +"\t"+"\n"
            show_label = Label(product_list, text=print_records, font=('Arial Bold', 10))
            show_label.grid(row=0, column=0)

            # commit changes
            connect.commit()

            # Close connection
            connect.close()

Operational_frame = LabelFrame(Mainframe,bd=2,width=1300,height=60,padx=50,pady=20,bg="white",relief=RIDGE)
Operational_frame.pack(side=BOTTOM)


Body_frame = LabelFrame(Mainframe,bd=2,width=1290,height=400,padx=30,pady=20,bg="white",relief=RIDGE)
Body_frame.pack(side=BOTTOM)

LeftBodyFrame  = LabelFrame(Body_frame,text='Product Item Details:',bd=2,width=600,height=380,padx=20,pady=10,
                       bg='yellow',relief=RIDGE,font=('Arial Bold',15))
LeftBodyFrame.pack(side=LEFT)

RightBodyFrame  = LabelFrame(Body_frame,text='Product Item Details:',bd=2,width=400,height=380,padx=20,pady=10,
                       bg='yellow',relief=RIDGE,font=('Arial Bold',15))
RightBodyFrame.pack(side=RIGHT)



#pID = StringVar()
#pName = StringVar()
#pPrice= StringVar()
#pQty = StringVar()
#pCompany = StringVar()
#pContact= StringVar()

#Adding the widgets
label_pid = Label(LeftBodyFrame,text="Product ID:",font=('Arial Bold',15),padx=2,bg='white',fg='blue')
label_pid.grid(row=0,column=0,pady=2,sticky=W)

entry_pid = Entry(LeftBodyFrame,font=('Arial Bold',20),bg='white',width=20)
entry_pid.grid(row=0,column=1,pady=2,sticky=W)

label_name = Label(LeftBodyFrame,text="Name of Item:",font=('Arial Bold',15),padx=2,bg='white',fg='blue')
label_name.grid(row=1,column=0,pady=2,sticky=W)

entry_name = Entry(LeftBodyFrame,font=('Arial Bold',20),bg='white',width=20)
entry_name.grid(row=1,column=1,pady=2,sticky=W)

label_price = Label(LeftBodyFrame,text="Price per Unit:",font=('Arial Bold',15),padx=2,bg='white',fg='blue')
label_price.grid(row=2,column=0,pady=2,sticky=W)

entry_price = Entry(LeftBodyFrame,font=('Arial Bold',20),bg='white',width=20)
entry_price.grid(row=2,column=1,pady=2,sticky=W)

label_qty = Label(LeftBodyFrame,text="Quality:",font=('Arial Bold',15),padx=2,bg='white',fg='blue')
label_qty.grid(row=3,column=0,pady=2,sticky=W)

entry_qty = Entry(LeftBodyFrame,font=('Arial Bold',20),bg='white',width=20)
entry_qty.grid(row=3,column=1,pady=2,sticky=W)

label_company = Label(LeftBodyFrame,text="Manufacture:",font=('Arial Bold',15),padx=2,bg='white',fg='blue')
label_company.grid(row=4,column=0,pady=2,sticky=W)

entry_company = Entry(LeftBodyFrame,font=('Arial Bold',20),bg='white',width=20)
entry_company.grid(row=4,column=1,pady=2,sticky=W)


label_contact = Label(LeftBodyFrame,text="Contacts:",font=('Arial Bold',15),padx=2,bg='white',fg='blue')
label_contact.grid(row=5,column=0,pady=2,sticky=W)

entry_contact = Entry(LeftBodyFrame,font=('Arial Bold',20),bg='white',width=20)
entry_contact.grid(row=5,column=1,pady=2,sticky=W)

label_contact = Label(LeftBodyFrame,padx=2)
label_contact.grid(row=6,column=0,pady=2,sticky=W)
label_contact = Label(LeftBodyFrame,padx=2)
label_contact.grid(row=7,column=0,pady=2,sticky=W)
label_contact = Label(LeftBodyFrame,padx=2)
label_contact.grid(row=8,column=0,pady=2,sticky=W)


#Add Scroll bar
scroll = Scrollbar(RightBodyFrame)
scroll.grid(row=0,column=1,sticky='ns')

product_list = Listbox(RightBodyFrame,width=40,height=16,font=('Arial ,Bold',15),yscrollcommand=scroll.set)

product_list.grid(row=0,column=0,padx=8)
scroll.config(command=product_list.yview)
#Adding Buttons
save_btn = Button(Operational_frame,text="Save",font=('Arial Bold',18),height=1,width=10,bd=4,command=Submit)
save_btn.grid(row=0,column=0)

show_btn = Button(Operational_frame,text="Show Data",font=('Arial Bold',18),height=1,width=10,bd=4,command=show)
show_btn.grid(row=0,column=1)

Clear_btn = Button(Operational_frame,text="Clear",font=('Arial Bold',18),height=1,width=10,bd=4)
Clear_btn.grid(row=0,column=2)

Delete_btn = Button(Operational_frame,text="Delete",font=('Arial Bold',18),height=1,width=10,bd=4)
Delete_btn.grid(row=0,column=3)

Update_btn = Button(Operational_frame,text="Edit",font=('Arial Bold',18),height=1,width=10,bd=4)
Update_btn.grid(row=0,column=5)

Search_btn = Button(Operational_frame,text="Search",font=('Arial Bold',18),height=1,width=10,bd=4)
Search_btn.grid(row=0,column=4)

Close_btn = Button(Operational_frame,text="Close",font=('Arial Bold',18),height=1,width=10,bd=4,command=Close)
Close_btn.grid(row=0,column=6)

# commit changes
connect.commit()

# Close connection
connect.close()
root.mainloop()