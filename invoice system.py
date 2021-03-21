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
        c_bill_txt = Entry(F1, width=15, font="arial 15",  bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search",width=10, bd=7, font='arial 12 bold').grid(row=0,column=6,padx=10,pady=10)


        #...........cosmatics frame
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg="white", bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)
        bath_lbl=Label(F2,text="Bath Soap",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt =Entry(F2, width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        face_cream__txt =Entry(F2, width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        face_w_lbl=Label(F2,text="Face Wash",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        face_w__txt =Entry(F2, width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        Hair_s__txt =Entry(F2, width=10,textvariable=self.spary,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        Hair_g_lbl=Label(F2,text="Hair Gell",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Hair_g__txt =Entry(F2, width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        Body__lbl=Label(F2,text="Body Loshan",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        Body__txt =Entry(F2, width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        #...........Grocery frame
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Glocery", font=("times new roman", 15, "bold"),fg="white", bg=bg_color)
        F3.place(x=340, y=180,width=325,height=380)
        g1_lbl=Label(F3,text="Rice",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g1_txt =Entry(F3, width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        g2_lbl=Label(F3,text="Food Oil",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_cream__txt =Entry(F3, width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        g3_lbl=Label(F3,text="Daal",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3__txt =Entry(F3, width=10,textvariable=self.dall,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        g4_lbl=Label(F3,text="Wheat",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4__txt =Entry(F3, width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        g5_lbl=Label(F3,text="Sugar",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5__txt =Entry(F3, width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        g6__lbl=Label(F3,text="Tea",font=('times new roman',16,"bold"),bg=bg_color,fg=fg).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        g6__txt =Entry(F3, width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

root=Tk()
ob=Bill_App(root)
root.mainloop()