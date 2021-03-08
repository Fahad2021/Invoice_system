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
        

root=Tk()
ob=Bill_App(root)
root.mainloop()