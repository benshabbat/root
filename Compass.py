from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import pyodbc
import time as tm

# connect db
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-U456TC5\SQLEXPRESS;'
    'Database=ACDB;'
    'Trusted_Connection=yes;')
cursor = conn.cursor()

HEIGHT = 700
WIDTH = 1355
root = Tk()
root.resizable(width=False, height=False)

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="#263D42")
canvas.pack(fill=BOTH, side=LEFT, expand=True)
# Header
Title = Label(root, text="Communication Compass", bg='yellow', font="none 20 bold")
Title.place(relx=0.38, rely=0.01)
# Copyright
Actor = Label(root,
              text="© Almog Halevi, Yanit Golman, Chen-David Benshabbat, Ahmad Jbareen.    All rights reserved,Copyright.",
              bg='yellow', font="none 8 bold")
Actor.place(relx=0.00, rely=0.97)

# frame in the canvas>root>frame
frame = Frame(master=root, bg='white', padx=0, pady=1)
frame.place(relx=0.00, rely=0.08, relwidth=1.0, relheight=0.89)

# Scrollbar
scrollbar = Scrollbar(root)

# text to show what you search
T = Text(frame, height=13, width=85, background="gray", foreground="yellow", yscrollcommand=scrollbar.set,
         font=('Pratt Pro', 12, 'bold'))
T.place(relx=0.3, rely=0.06)

# customers & list packages Start
SelectCustomers = "select Customer_Id FROM customers"
SelectPackages = "select pack_id FROM packages"
cursor.execute(SelectCustomers)
cursor.execute(SelectPackages)
result = cursor.fetchall()
result2 = cursor.fetchall()
listCous = []
listPack = []
for i in result:
    for j in i:
        listCous.append(j)

for i in result:
    for j in i:
        listPack.append(j)


#########################Quarry Functions##############################


# checkF
def Date():
    T.delete(1.0, END)
    try:
        Select2 = 'SELECT First_Name,Last_Name,Join_date FROM customers Where Year(Join_date) = (select Year(Join_date) from customers where Customer_Id = ?)' \
                  ' AND Month(Join_date) = (select Month(Join_date) from customers where Customer_Id = ?)'
        c = [e1.get(), e1.get()]
        cursor.execute(Select2, c)
        ch = cursor.fetchall()
        if e1.get() == "" or int(e1.get()) not in listCous:
            T.insert(END, "Please insert id number")
        else:
            T.insert(END, "\t\t\t==== The year and month of customers ====\n\n")
            T.insert(END, "First Name:" + "\t\tLast Name:\t\tJoin Date:\t\t")
            for i in ch:
                T.insert(END, "\n " + i[0] + "\t\t" + i[1] + "\t\t" + i[2])
    except:
        T.insert(END, "Please insert id ")


# add new Account
def Add_Account2():
    T.delete(1.0, END)
    try:
        print("create Account")
        packId()
        cursor = conn.cursor()
        sql = 'insert into dbo.customers(First_Name,Last_Name,Birth_Date,Join_Date,City,State,Street,main_phone_num,secondary_phone_num,fax,monthly_discount,pack_id) values(?,?,?,?,?,?,?,?,?,?,?,?);'
        val = [e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get(),
               e12.get(), numberChoose.get()]

        # check validate
        if val[0].isalpha() and val[1].isalpha() and val[4].isalpha() and val[5].isalpha() and val[6].isalpha() \
                and val[7].isdigit() and val[8].isdigit() and val[9].isdigit() \
                and len(val[7]) == 9 and len(val[8]) == 10 and len(val[9]) == 9:
            cursor.execute(sql, val)
            conn.commit()
            T.insert(END, "Create...")
        # print(cursor.rowcount, "record inserted.")
        else:
            T.insert(END, "Please Try again. Bad Parameter.")
    except:
        T.insert(END, "Please Try again. Bad Parameter.  ")


# show all business customers -> show quarry work E :
def checkE():
    T.delete(1.0, END)
    Select = "select First_Name,monthly_discount,customers.pack_id,main_phone_num,secondary_phone_num FROM packages,customers  WHERE sector_id = 2 "
    cursor.execute(Select)
    ch = cursor.fetchall()
    T.insert(END, "\t\t\t==== The business customers ====\n\n")
    T.insert(END, "First Name:" + "\t\tDiscount:\t\tPack Number:\t\tMain Phone:\t\tSecondary Phone:")
    for i in ch:
        T.insert(END, "\n " + i[0] + "\t\t")

        if i[1] is None:
            T.insert(END, "null" + "\t\t")
        if i[1] is not None:
            T.insert(END, str(i[1]) + "\t\t")

        if i[2] is None:
            T.insert(END, "null" + "\t\t")
        if i[2] is not None:
            T.insert(END, str(i[2]) + "\t\t")

        T.insert(END, i[3] + "\t\t")

        if i[4] is None:
            T.insert(END, "null" + "\t\t")
        if i[4] is not None:
            T.insert(END, str(i[4]) + "\t\t")


# show quarry work G all 5MBps :
def checkG():
    T.delete(1.0, END)
    Select = "select First_Name,Last_Name,City,State,customers.pack_id FROM customers,packages WHERE speed = '5Mbps' "
    cursor.execute(Select)
    ch = cursor.fetchall()
    T.insert(END, "\t\t\t==== All the customers with 5Mbps ====\n\n")
    T.insert(END, "First Name:" + "\t\tLast Name:\t\tCity:\t\tState:\t\tPack Number:")
    for i in ch:
        T.insert(END, "\n " + i[0] + "\t\t" + i[1] + "\t\t")

        if i[2] is None:
            T.insert(END, "null" + "\t\t")
        if i[2] is not None:
            T.insert(END, str(i[2]) + "\t\t")

        if i[3] is None:
            T.insert(END, "null" + "\t\t")
        if i[3] is not None:
            T.insert(END, str(i[3]) + "\t\t")

        if i[4] is None:
            T.insert(END, "null" + "\t\t")
        if i[4] is not None:
            T.insert(END, str(i[4]) + "\t\t")


# show quarry work H :
def checkH():
    T.delete(1.0, END)
    Select = "SELECT First_Name, monthly_discount,customers.pack_id FROM customers " \
             "FULL OUTER JOIN packages on customers.pack_id = packages.pack_id WHERE packages.monthly_payment > (SELECT AVG(monthly_payment) FROM dbo.packages)"
    cursor.execute(Select)
    ch = cursor.fetchall()
    T.insert(END, "\t\t==== Customers whose payment is larger than average ====\n\n")
    T.insert(END, "First Name:" + "\t\tDiscount:\t\tPack Number:")
    for i in ch:
        if i[0] is None:
            T.insert(END, "\n " + "null" + "\t\t")
        if i[0] is not None:
            T.insert(END, "\n " + str(i[0]) + "\t\t")

        if i[1] is None:
            T.insert(END, "null" + "\t\t")
        if i[1] is not None:
            T.insert(END, str(i[1]) + "\t\t")

        if i[2] is None:
            T.insert(END, "null" + "\t\t")
        if i[2] is not None:
            T.insert(END, str(i[2]) + "\t\t")


# Delete Costumer
def DeleteCost():
    T.delete(1.0, END)
    try:
        Rolname = e1.get()
        if int(Rolname) not in listCous:
            T.insert(END, "The Costumer id: " + Rolname + " was not Found")
        else:
            Select = "DELETE FROM customers WHERE Customer_Id  = '%s'" % (Rolname)
            cursor.execute(Select)
            conn.commit()
            T.insert(END, "the record was deleted:" + Rolname)
    except:
        T.insert(END, "Please enter ID NUMBER")


#########################button functions##############################


# add new pack
def Add_packTest():
    T.delete(1.0, END)
    try:
        cursor = conn.cursor()
        cursor.execute(
            'insert into dbo.packages(speed,strt_date,monthly_payment,sector_id) values(?,?,?,?);',
            (
                e14.get(), e15.get(), e16.get(), var.get())
        )
        conn.commit()
        T.insert(END, "Create new Pack")
        print(cursor.rowcount, "record inserted.")
    except:
        T.insert(END, "Please Try again. Bad Parameter.")


# close the app - > Exit_button
def close_window():
    MsgBox = messagebox.askquestion('Exit App', 'Really Quit?', icon='error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Welcome Back', 'Welcome back to the App')


# search query with a ID
def Search():
    T.delete(1.0, END)
    try:
        Id = e1.get()
        Select = "SELECT * FROM customers WHERE [Customer_Id] = '%s'" % Id
        cursor.execute(Select)
        result = cursor.fetchall()
        dbId = result[0]
        messagebox.askokcancel("Information", "Record Already exists.")
        T.insert(END, "\t\t\t==== Account information ====\n\n")
        for i in result:
            if i[0] is None:
                T.insert(END, "null" + "\t\t")
            if i[0] is not None:
                T.insert(END,
                         "Customer Id:\t" + str(i[0]) + "\nFirst Name:\t" + str(i[1]) + "\nLast Name:\t" + str(i[2]))
                T.insert(END, "\nBirth Date:\t" + str(i[3]) + "\nJoin Date:\t" + str(i[4]) + "\nCity:" + str(i[5]))
                T.insert(END, "\nState:" + str(i[6]) + "\nStreet:" + str(i[7]) + "\nMain phone:" + str(i[8]))
                T.insert(END, "\nsecondary phone:" + str(i[9]) + "\nfax:" + str(i[10]) +
                         "\nMonthly discount:" + str(i[11]) + "\nPack id:" + str(i[12]))
    except:
        messagebox.askokcancel("Information", "Record Already no exists.")


# Show table packages :
def ShowPackages():
    T.delete(1.0, END)
    Select2 = "select packages.pack_id,packages.monthly_payment,speed FROM packages"
    cursor.execute(Select2)
    ch = cursor.fetchall()
    T.insert(END, "\t==== The packages list ====\n\n")
    T.insert(END, "Pack id:" + "\t\tMonthly_payment:\t\t\tSpeed:\n")
    for i in ch:
        if i[0] is None:
            T.insert(END, "\nnull" + "\t\t")
        if i[0] is not None:
            temp = i[0]
            c = str(temp)
            T.insert(END, "\n" + c + "\t\t")

        if i[1] is None:
            T.insert(END, "null" + "\t\t\t")
        if i[1] is not None:
            temp = i[1]
            c = str(temp)
            T.insert(END, c + "\t\t\t")

        if i[2] is None:
            T.insert(END, "null" + "\t\t")
        if i[2] is not None:
            temp = i[2]
            c = str(temp)
            T.insert(END, c + "\t\t")


# DeletePackages
def DeletePackages():
    T.delete(1.0, END)
    try:
        Rolname = e1.get()
        if Rolname == "" or int(Rolname) not in listPack:
            T.insert(END, "Please enter id-packages\nThe Package was not Found.")
        else:
            Select = "DELETE FROM packages WHERE pack_id  = '%s'" % (Rolname)
            cursor.execute(Select)
            conn.commit()
            T.insert(END, "the Packages was delete: " + Rolname)
    except:
        T.insert(END, "Please enter id-packages,The Package was not Found.")


# clear the entry
def Clear():
    T.delete(1.0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e4.insert(0, 'mm-dd-yyyy')
    e5.delete(0, END)
    e5.insert(0, 'mm-dd-yyyy')
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e9.insert(0, '9 -  Digits')
    e10.delete(0, END)
    e10.insert(0, '10 - Digits')
    e11.delete(0, END)
    e11.insert(0, '9 - Digits')
    e12.delete(0, END)
    e12.insert(0, '00.00')
    e15.delete(0, END)
    e15.insert(0, 'mm-dd-yyyy')
    e14.delete(0, END)
    e14.insert(0, '--Mbps')
    e16.delete(0, END)
    e16.insert(0, '00')


#########################TEST##############################

# show all customers for QA
def checkList():
    cursor.execute("select * from customers")
    r = cursor.fetchall()
    for row in r:
        print(row)


###############################################################

########################Combobox#############################

# Combobox to reloading the account
def callbackFunc(event):
    print(numberChoose.current(), numberChoose.get())
    packId()


# Update the list of ComboBox
def packtId():
    Select = "select pack_id FROM packages"
    cursor.execute(Select)
    result = cursor.fetchall()
    list = []
    for i in result:
        for j in i:
            list.append(j)
            numberChoose['values'] = list
    return list


numberChoose = Combobox(frame, postcommand=packtId)
numberChoose.grid(row=12, column=1)
numberChoose.bind("<<ComboboxSelected>>", callbackFunc)


# update Choose number of pack_id
def packId():
    try:
        if numberChoose.get() != "":
            print("its:", numberChoose.get())
            list.append(numberChoose.get())
    except:
        print("Please Choose pack id..")


####################endCombobox#############################


# "UPDATE new pack id
def UpDatePack():
    global cursor
    T.delete(1.0, END)
    try:
        if int(e17.get()) not in listCous:
            T.insert(END, "The Customer Id : was not found.")

        else:
            cursor = conn.cursor()
            cursor.execute(
                'update dbo.customers set pack_id = ? where Customer_Id = ? ',
                (
                    e18.get(), e17.get())
            )
            conn.commit()
            T.insert(END, "The Package was update...")
    except:
        T.insert(END, "Error: Bad parameters. can not found this package")


# Digital Clock
def display_time():
    current_time = tm.strftime('%H:%M:%S')
    clock_label['text'] = current_time
    root.after(1000, display_time)


#########################Buttons##############################

checkF = Button(frame, text="CheckF", width=12, height=2, bg="#263D42", fg="white", command=Date)
checkF.place(relx=0.90, rely=0.4)

checkH = Button(frame, text="CheckH", width=12, height=2, bg="#263D42", fg="white", command=checkH)
checkH.place(relx=0.90, rely=0.30)

checkE = Button(frame, text="CheckE", width=12, height=2, bg="#263D42", fg="white", command=checkE)
checkE.place(relx=0.90, rely=0.20)

UpDatePack_Button = Button(frame, text="Update Packages", width=12, height=2, bg="#263D42", fg="white",
                           command=UpDatePack)
UpDatePack_Button.place(relx=0.65, rely=0.65)

Add_Button = Button(frame, text="Delete Packages", width=12, height=2, bg="#263D42", fg="white", command=DeletePackages)
Add_Button.place(relx=0.80, rely=0.7)

button = Button(frame, text="Search", bg="#263D42", width=12, height=2, fg="white", command=Search)
button.place(relx=0.80, rely=0.5)

delete_Button = Button(frame, text="Delete Customer", bg="#263D42", width=12, height=2, fg="white", command=DeleteCost)
delete_Button.place(relx=0.80, rely=0.6)

Clear_Button = Button(frame, text="Clear", width=10, height=2, bg="green", fg="white", command=Clear)
Clear_Button.place(relx=0.83, rely=0.92)

checkq2 = Button(frame, text="CheckIn", width=12, height=2, bg="#263D42", fg="white", command=checkList)
checkq2.place(relx=0.90, rely=0.7)

InsertIn = Button(frame, text="Insert", width=12, height=2, bg="#263D42", fg="white", command=Add_Account2)
InsertIn.place(relx=0.15, rely=0.75)

Check_btn2 = Button(frame, text="CheckG", width=12, height=2, bg="#263D42", fg="white", command=checkG)
Check_btn2.place(relx=0.90, rely=0.5)

Check_btn3 = Button(frame, text="Show Packages", width=12, height=2, bg="#263D42", fg="white", command=ShowPackages)
Check_btn3.place(relx=0.90, rely=0.6)

Add_New_Packt = Button(frame, text="Add package", width=12, height=2, bg="#263D42", fg="white", command=Add_packTest)
Add_New_Packt.place(relx=0.40, rely=0.75)

# button exit from app
Exit_button = Button(frame, text="Exit", bg='Red', width=10, height=2, font="none 8 bold", command=close_window)
Exit_button.place(relx=0.92, rely=0.92)

# All the Label
# for add Account
label1 = Label(frame, text="Customer Id:", width=20, height=2, bg="skyblue", fg="black").grid(row=0, column=0)
label2 = Label(frame, text="First Name:", width=20, height=2, bg="pink").grid(row=1, column=0)
label3 = Label(frame, text="Last Name:", width=20, height=2, bg="pink").grid(row=2, column=0)
label4 = Label(frame, text="Birth Date:", width=20, height=2, bg="pink").grid(row=3, column=0)
label5 = Label(frame, text="Join Date:", width=20, height=2, bg="pink").grid(row=4, column=0)
label6 = Label(frame, text="City:", width=20, height=2, bg="pink").grid(row=5, column=0)
label7 = Label(frame, text="State:", width=20, height=2, bg="pink").grid(row=6, column=0)
label8 = Label(frame, text="Street:", width=20, height=2, bg="pink").grid(row=7, column=0)
label9 = Label(frame, text="Main phone:", width=20, height=2, bg="pink").grid(row=8, column=0)
label10 = Label(frame, text="Secondary phone:", width=20, height=2, bg="pink").grid(row=9, column=0)
label11 = Label(frame, text="Fax:", width=20, height=2, bg="pink").grid(row=10, column=0)
label12 = Label(frame, text="Monthly discount:", width=20, height=2, bg="pink").grid(row=11, column=0)
label13 = Label(frame, text="Pack id:", width=20, height=2, bg="pink").grid(row=12, column=0)
# for the new pack
label14 = Label(frame, text="Speed:", width=20, height=2, bg="pink").grid(row=9, column=2)
label15 = Label(frame, text="Monthly payment:", width=20, height=2, bg="pink").grid(row=11, column=2)
label16 = Label(frame, text="Start Date:", width=20, height=2, bg="pink").grid(row=10, column=2)
label17 = Label(frame, text="Sector:", width=20, height=2, bg="pink").grid(row=12, column=2)
# for update pack
label18 = Label(frame, text="Id number:", width=20, height=2, bg="pink").grid(row=9, column=6)
label19 = Label(frame, text="New pack:", width=20, height=2, bg="pink").grid(row=10, column=6)

# All the Entry:
# ID_NUMBER
e1 = Entry(frame, width=25, borderwidth=7, )
e1.grid(row=0, column=1)
# FIRST NAME
e2 = Entry(frame, width=30, borderwidth=8)
e2.grid(row=1, column=1)
# LAST NAME
e3 = Entry(frame, width=30, borderwidth=8)
e3.grid(row=2, column=1)
e4 = Entry(frame, width=30, borderwidth=8)
e4.grid(row=3, column=1)
e4.insert(0, 'mm-dd-yyyy')
e5 = Entry(frame, width=30, borderwidth=8)
e5.grid(row=4, column=1)
e5.insert(0, 'mm-dd-yyyy')
e6 = Entry(frame, width=30, borderwidth=8)
e6.grid(row=5, column=1)
e7 = Entry(frame, width=30, borderwidth=8)
e7.grid(row=6, column=1)
e8 = Entry(frame, width=30, borderwidth=8)
e8.grid(row=7, column=1)
e9 = Entry(frame, width=30, borderwidth=8)
e9.grid(row=8, column=1)
e9.insert(0, '9 -  Digits')
e10 = Entry(frame, width=30, borderwidth=8)
e10.grid(row=9, column=1)
e10.insert(0, '10 - Digits')
e11 = Entry(frame, width=30, borderwidth=8)
e11.grid(row=10, column=1)
e11.insert(0, '9 - Digits')
e12 = Entry(frame, width=30, borderwidth=8)
e12.grid(row=11, column=1)
e12.insert(0, '00.00')

# for the new pack
# speed
e14 = Entry(frame, width=20, borderwidth=8)
e14.grid(row=9, column=4)
e14.insert(0, '--Mbps')
# start-day
e15 = Entry(frame, width=20, borderwidth=8)
e15.grid(row=10, column=4)
e15.insert(0, 'mm-dd-yyyy')
# Monthly_discount
e16 = Entry(frame, width=20, borderwidth=8)
e16.grid(row=11, column=4)
e16.insert(0, '00')

var = IntVar()
R1 = Radiobutton(frame, text="private", variable=var, value=1)
R1.grid(row=12, column=4)
R2 = Radiobutton(frame, text="business", variable=var, value=2)
R2.grid(row=12, column=5)

# for update
e17 = Entry(frame, width=20, borderwidth=8)
e17.grid(row=9, column=7)
e18 = Entry(frame, width=20, borderwidth=8)
e18.grid(row=10, column=7)

# for the Clock
clock_label = Label(root, font='ariel 20', bg='#263D42', fg='white')
clock_label.place(relx=0.88, rely=0.01, relwidth=0.1, relheight=0.06)
display_time()
# the end of the loop of the method
root.mainloop()
# Close Connection with the DB
# messagebox.showinfo('Welcome ', 'Welcome to the App')
conn.close()
