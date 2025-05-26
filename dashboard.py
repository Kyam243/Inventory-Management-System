from tkinter import*
 #pip install pillow
from PIL import Image, ImageTk 
# photo ke path ke liye add hua hai ------
import tkinter

#importing employee file (dashboard)   -- if employee is store in another folder  keyword using -----from subpython.employee import employeeclass
from employee import employeeClass 

# importing supplier file using supplier class 
from supplier import supplierClass

# importing category python file from category class
from category import categoryClass

# importing product python file
from product import productClass

# importing sales python file from sales class
from sales import salesClass

import sqlite3
from tkinter import messagebox
import os
import time  
from rembg import remove


class IMS:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management $ystem   |   Developed By Kyamuddin Siddique | Priyadarshani Bhatt | Md. Ahmad Raza Ansari")
        # self.root.config(bg="white")
        
        
        # photo wala hai
        # image_path=PhotoImage(file=r"images/logo01.png")
        # bg_image=tkinter.Label(self.root,image=image_path)
        # bg_image.place(relheight=1,relwidth=1)
        
        
        
        
        
        # ------title------
        self.icon_title=PhotoImage(file="images/l01.png")
        # self.icon1_title=PhotoImage(file="images/logo01.png")
        title=Label(self.root,text="Inventory Management $ystem",image=self.icon_title,compound=LEFT,font=("bebas Neue", 30,"bold"), bg="#401b3a",fg="sky blue",anchor="w", padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        
        
        
        # ----button logout----
        btn_logout=Button(self.root,text="Logout",command=self.logout, font=("sansarif",15,"bold"),bg="#ff5733", cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        
        
        # clocks --
        
        self.lbl_clock=Label(self.root,text="Welcome Dear ! We are thrilled to have you here\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        
        
        
        # <-----images--->
        
        self.im1=Image.open("images/logo01.png")
        self.im1=self.im1.resize((240,200))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        
        self.lbl_im1=Label(self.root,image=self.im1)
        self.lbl_im1.place(x=200,y=500)
        # -----<>
        self.im2=Image.open("images/logo01.png")
        self.im2=self.im2.resize((340,300))
        self.im2=ImageTk.PhotoImage(self.im2)
        
        
        self.lbl_im2=Label(self.root,image=self.im2)
        self.lbl_im2.place(x=1010,y=400)
        # -----<>
        
        self.im3=Image.open("images/logo01.png")
        self.im3=self.im3.resize((150,120))
        self.im3=ImageTk.PhotoImage(self.im3)
        
        
        self.lbl_im3=Label(self.root,image=self.im3)
        self.lbl_im3.place(x=160,y=110)
        
        self.im6=Image.open("images/logo01.png")
        self.im6=self.im6.resize((100,70))
        self.im6=ImageTk.PhotoImage(self.im6)
        
        
        self.lbl_im6=Label(self.root,image=self.im6)
        self.lbl_im6.place(x=800,y=130)
        
        # -----<>
        self.im4=Image.open("images/logo01.png")
        self.im4=self.im4.resize((60,40))
        self.im4=ImageTk.PhotoImage(self.im4)
        
        
        self.lbl_im4=Label(self.root,image=self.im4)
        self.lbl_im4.place(x=565,y=340)
        # -----<>
        self.im5=Image.open("images/logo01.png")
        self.im5=self.im5.resize((110,100))
        self.im5=ImageTk.PhotoImage(self.im5)
        
        
        self.lbl_im5=Label(self.root,image=self.im5)
        self.lbl_im5.place(x=1328,y=180)
        # -----<>
        self.im7=Image.open("images/logo01.png")
        self.im7=self.im7.resize((40,30))
        self.im7=ImageTk.PhotoImage(self.im7)
        
        
        self.lbl_im7=Label(self.root,image=self.im7)
        self.lbl_im7.place(x=750,y=550)
        # -----<>
        
        # ---left Menu  placing by using frame---
        # including image
        self.Menulogo=Image.open("images/menu_im.png")
        
        # resizing image and enhancing quality
        self.Menulogo=self.Menulogo.resize((200,202))
        
        # calling the image 
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=600)
        
        # placing the image
        
        lbl_menuLogo=Label(LeftMenu,image=self.Menulogo,bg="lightyellow")
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        
        # ---menu---
        
        
        self.icon_side=PhotoImage(file="images/side.png")

        
        lbl_menu=Label(LeftMenu,text="Menu", font=("Bree serif",25,),bg="#009888").pack(side=TOP,fill=X)
        
        # btn_emp=Button(LeftMenu,text="Employee",command=self.employee,compound=LEFT,anchor="w",padx=60,bg="white",fg="#00759e",font=("times new roman",13),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").pack(side=TOP, fill=X)
        
        # btn_sup=Button(LeftMenu,text="Supplier",command=self.supplier,compound=LEFT, anchor="w",padx=60,bg="white",fg="#00759e",font=("times new roman",13),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").pack(side=TOP, fill=X)
        
        # btn_categ=Button(LeftMenu,text="Category",command=self.category,compound=LEFT, anchor="w",padx=60,bg="white",fg="#00759e",font=("times new roman",13),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").pack(side=TOP, fill=X)
        
        # btn_prod=Button(LeftMenu,text="Product",command=self.product,compound=LEFT, anchor="w",padx=60,bg="white",fg="#00759e",font=("times new roman",13),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").pack(side=TOP, fill=X)
        
        # btn_sales=Button(LeftMenu,text="Sales",command=self.sales,compound=LEFT, anchor="w",padx=60,bg="white",fg="#00759e",font=("times new roman",13),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").pack(side=TOP, fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5,pady=2,anchor="w", font=("sansarif",20, "bold"),bg="#e0ffff", bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
    # command attribute ka use employee wale section(function) ko call krne ke liye kiya gya hai
        
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier, image=self.icon_side, compound=LEFT, padx=5,pady=2,anchor="w", font=("sansarif",20, "bold"),bg="#e0ffff", bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_category=Button(LeftMenu,text="Category",command=self.category, image=self.icon_side, compound=LEFT, padx=5,pady=2,anchor="w", font=("sansarif",20, "bold"),bg="#e0ffff", bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_product=Button(LeftMenu,text="Product",command=self.product, image=self.icon_side, compound=LEFT, padx=5,pady=2,anchor="w", font=("sansarif",20, "bold"),bg="#e0ffff", bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales, image=self.icon_side, compound=LEFT, padx=5,pady=2,anchor="w", font=("sansarif",20, "bold"),bg="#e0ffff", bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_exit=Button(LeftMenu,text="Exit", image=self.icon_side, compound=LEFT, padx=5,pady=2,anchor="w", font=("sansarif",20, "bold"),bg="#e0ffff", bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        #-- content--
        
        
        self.lbl_employee=Label(self.root,text="Total Employee\n [ 0 ]" ,bd=0, relief=RIDGE, fg="#460000",font=("geudy old style",20,"bold"))
        self.lbl_employee.place(x=270,y=230,height=100,width=300)
        
        
        # self.lbl_supplier=Label(self.root,text="Total Supplier\n [ 0 ]" ,bd=5, relief=RIDGE, bg="#ccffff",fg="#460000",font=("geudy old style",20,"bold"))
        # self.lbl_supplier.place(x=620,y=115,height=100,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n [ 0 ]" ,bd=0, relief=RIDGE,fg="#460000",font=("geudy old style",20,"bold"))
        self.lbl_supplier.place(x=620,y=230,height=100,width=300)
        
        
        self.lbl_category=Label(self.root,text="Total Category\n [ 0 ]" ,bd=0, relief=RIDGE,fg="#460000",font=("geudy old style",20,"bold"))
        self.lbl_category.place(x=970,y=230,height=100,width=300)
        
        
        self.lbl_product=Label(self.root,text="Total Product\n [ 0 ]" ,bd=0, relief=RIDGE,fg="#460000",font=("geudy old style",20,"bold"))
        self.lbl_product.place(x=270,y=380,height=100,width=300)
        
        
        self.lbl_sales=Label(self.root,text="Total Sales\n [ 0 ]" ,bd=0, relief=RIDGE,fg="#460000",font=("geudy old style",20,"bold"))
        self.lbl_sales.place(x=620,y=380,height=100,width=300)

        
        
        
        
        
         
        
        # --Footer---
        
        
        lbl_footer=Label(self.root,text="IMS-Inventory Management system  |  Developed by Kyamuddin Siddique | Priyadarshani Bhatt | Md. Ahmad Raza Ansari \nFor Any Querry Cont. : 8874381506", font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()

        
#====================================================================================================
        #  definig employee section (accessing employee,.py from another dashboard) using def (define constroctur )
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)    
    
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)    
    
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)    
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)    
    
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n [ {str(len(product))} ]')
                
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n [ {str(len(supplier))} ]')
                
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n [ {str(len(category))} ]') 
               
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n [ {str(len(employee))} ]')
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total sales\n [{str(bill)}]')
            
            time_=time.strftime("%H:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome Dear ! We are thrilled to have you here\t\t Date: {str(date_)} \t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
            
              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python main.py")

        
if __name__=="__main__":       
    root=Tk()
    obj=IMS(root)
    root.mainloop()
   