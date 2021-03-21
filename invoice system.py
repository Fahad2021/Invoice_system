from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Invoice System")
        bg_color="#ED1A23"
        fg="black"
        title=Label(self.root,text="Brotherhood Super Shop",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
    # .........variable.............
    # ........cosmetic........
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spary = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        # ......glocery.....
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.dall = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # .......cold_drinks.....
        self.maza = IntVar()
        self.seven_up = IntVar()
        self.tiger = IntVar()
        self.sprit = IntVar()
        self.fruto = IntVar()
        self.speed = IntVar()

        # .....total product price....
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()
        # .......customer .....
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()

        # ..................customer details frame
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),fg="white", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg, font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, font="arial 15", textvariable=self.c_name, bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg=fg, font=("times new roman", 18, "bold")).grid(row=0,column=2,padx=20,pady=5)
        cpn_txt = Entry(F1, width=15, font="arial 15", textvariable=self.c_phone, bd=7, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg=fg, font=("times new roman", 18, "bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt = Entry(F1, width=15, font="arial 15", textvariable=self, bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self, width=10, bd=7, font='arial 12 bold').grid(row=0,column=6,padx=10,pady=10)


root=Tk()
ob=Bill_App(root)
root.mainloop()