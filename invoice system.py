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

root=Tk()
ob=Bill_App(root)
root.mainloop()