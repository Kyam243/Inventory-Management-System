from tkinter import*

from kivy.app import App

 #pip install pillow
from PIL import Image, ImageTk 
# photo ke path ke liye add hua hai ------  

from tkinter import ttk,messagebox 
import sqlite3
import time
import os
import tempfile


class BillClass(App):
    def __init__(self , root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management $ystem   |   Developed By Kyamuddin Siddique | Priyadarshani Bhatt | Md. Ahmad Raza Ansari")
        self.root.config(bg="white")
        self.cart_list=[]
        self.check_print=0
        

        
        # ------title------
        self.icon_title=PhotoImage(file="images/l01.png")
        # self.icon1_title=PhotoImage(file="images/logo01.png")
        title=Label(self.root,text="Inventory Management $ystem",image=self.icon_title,compound=LEFT,font=("bebas Neue", 30,"bold"), bg="#401b3a",fg="sky blue",anchor="w", padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        
        
        
        # ----button logout----
        btn_logout=Button(self.root,text="Logout",command=self.logout, font=("sansarif",15,"bold"),bg="#ff5733", cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        
        
        # clocks --
        
        self.lbl_clock=Label(self.root,text="Welcome Dear ! We are thrilled to have you here\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        # ===Product Frame===
        
        ProductFrame1 = Frame(self.root , bd=4, relief=RIDGE , bg="white")
        ProductFrame1.place(x=10, y=110, width=410, height=570)
        
        PrudctTitle = Label(ProductFrame1, text="All Products", font=("goudy old style", 20 , "bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        # product frame2 which is in product frmae 1   // search frame
        
        self.var_search=StringVar()
        ProductFrame2 = Frame(ProductFrame1 , bd=2, relief=RIDGE , bg="white")
        ProductFrame2.place(x=2, y=42, width=398, height=90)
        
        lbl_search= Label(ProductFrame2, text="Search Product | By Name" , font=("times new roman",15 , "bold"),bg="white",fg="green").place(x=2,y=5)
        
        
        lbl_search=Label(ProductFrame2, text="Product Name", font=("times new roman",15 , "bold"),bg="white").place(x=2 , y=45)
        txt_search=Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman",15),bg="lightyellow").place(x=130 , y=47 , width=150 , height=22)
        
        btn_search= Button(ProductFrame2, text="Search",command=self.search,font=("goudy old style", 15),bg="#2196f3",fg="white", cursor="hand2").place(x=285, y=47, width=100, height=22)
        
        btn_show= Button(ProductFrame2, text="Show All",command=self.show,font=("goudy old style", 15),bg="#083531",fg="white", cursor="hand2").place(x=285, y=10, width=100, height=22)
        
        
        
        # Product Frame 3----- using tree view because tree view is more effective
        # or product detail frame
        
        
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=398)
        
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(ProductFrame3,columns=("Prod_ID","name","price","qnty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        
        self.product_Table.heading("Prod_ID",text="Prod_ID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qnty",text="Qnty")
        self.product_Table.heading("status",text="Status")
        
        self.product_Table["show"]="headings"
        
        self.product_Table.column("Prod_ID",width=50)
        self.product_Table.column("name",width=110)
        self.product_Table.column("price",width=90)
        self.product_Table.column("qnty",width=50)
        self.product_Table.column("status",width=70)
        
        
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note= Label(ProductFrame1 , text="Note : 'Enter 0 Quantity to remove the Product from the Cart'",font=("goudy old style",10,),anchor='w',bg="white",fg="red").pack(side=BOTTOM , fill=X)
        
        
        # == coustmer frame
        
        self.var_name = StringVar()
        self.var_contact= StringVar()
        
        CoustmerFarme = Frame(self.root , bd=4, relief=RIDGE , bg="white")
        CoustmerFarme.place(x=424, y=110, width=520, height=70)
        
        CoustmerTitle = Label(CoustmerFarme, text="Customer Details", font=("goudy old style", 15),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(CoustmerFarme, text="Name", font=("times new roman",15),bg="white").place(x=5 , y=35)
        txt_name=Entry(CoustmerFarme, textvariable=self.var_name, font=("times new roman",13),bg="lightyellow").place(x=70 , y=35 , width=160)
        
        lbl_contact=Label(CoustmerFarme, text="Contact No.", font=("times new roman",15),bg="white").place(x=260 , y=35)
        txt_contact=Entry(CoustmerFarme, textvariable=self.var_contact, font=("times new roman",13),bg="lightyellow").place(x=365 , y=35 , width=140)
        
        
        # ==== Calculator & cart frame===

        Calcu_Cart_Farme = Frame(self.root , bd=2, relief=RIDGE , bg="white")
        Calcu_Cart_Farme.place(x=424, y=190, width=520, height=360)
        
        # ==== Calculator frame===
        self.var_cal_input = StringVar()
        Calcu_Frame = Frame(Calcu_Cart_Farme , bd=10, relief=RIDGE , bg="white")
        Calcu_Frame.place(x=5, y=10, width=268, height=340)
        
        txt_cal_input = Entry(Calcu_Frame, textvariable=self.var_cal_input, font=('arial',15 , 'bold'), width=21 , bd=10 , relief=GROOVE , state='readonly', justify=RIGHT).grid(row=0 , columnspan=4)
        
        btn_7 = Button(Calcu_Frame , text='7' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(7),bd=4,width=4, pady=13 , cursor='hand2').grid(row=1 , column=0)
        btn_8 = Button(Calcu_Frame , text='8', font=('arial', 15 , 'bold'),command=lambda:self.get_input(8),bd=4,width=4, pady=13, cursor='hand2').grid(row=1 , column=1)
        btn_9 = Button(Calcu_Frame , text='9' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(9),bd=4,width=4, pady=13, cursor='hand2').grid(row=1 , column=2)
        btn_sum = Button(Calcu_Frame , text='+' , font=('arial', 15 , 'bold'),command=lambda:self.get_input('+'),bd=4,width=4, pady=13,cursor='hand2').grid(row=1 , column=3)
        
        btn_4 = Button(Calcu_Frame , text='4' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(4),bd=4,width=4, pady=13 , cursor='hand2').grid(row=2 , column=0)
        btn_5 = Button(Calcu_Frame , text='5', font=('arial', 15 , 'bold'),command=lambda:self.get_input(5),bd=4,width=4, pady=13, cursor='hand2').grid(row=2 , column=1)
        btn_6 = Button(Calcu_Frame , text='6' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(6),bd=4,width=4, pady=13, cursor='hand2').grid(row=2 , column=2)
        btn_sub = Button(Calcu_Frame , text='-' , font=('arial', 15 , 'bold'),command=lambda:self.get_input('-'),bd=4,width=4, pady=13,cursor='hand2').grid(row=2, column=3)
        
        btn_1 = Button(Calcu_Frame , text='1' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(1),bd=4,width=4, pady=13 , cursor='hand2').grid(row=3 , column=0)
        btn_2 = Button(Calcu_Frame , text='2', font=('arial', 15 , 'bold'),command=lambda:self.get_input(2),bd=4,width=4, pady=13, cursor='hand2').grid(row=3 , column=1)
        btn_3 = Button(Calcu_Frame , text='3' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(3),bd=4,width=4, pady=13, cursor='hand2').grid(row=3 , column=2)
        btn_mult = Button(Calcu_Frame , text='*' , font=('arial', 15 , 'bold'),command=lambda:self.get_input('*'),bd=4,width=4, pady=13,cursor='hand2').grid(row=3, column=3)
        
        btn_0 = Button(Calcu_Frame , text='0' , font=('arial', 15 , 'bold'),command=lambda:self.get_input(0),bd=4,width=4, pady=13 , cursor='hand2').grid(row=4 , column=0)
        btn_c = Button(Calcu_Frame , text='C', font=('arial', 15 , 'bold'),command=self.clear_cal,bd=4,width=4, pady=13, cursor='hand2').grid(row=4 , column=1)
        btn_eq = Button(Calcu_Frame , text='=' , font=('arial', 15 , 'bold'),command=self.perform_cal,bd=4,width=4, pady=13, cursor='hand2').grid(row=4 , column=2)
        btn_div = Button(Calcu_Frame , text='/' , font=('arial', 15 , 'bold'),command=lambda:self.get_input('/'),bd=4,width=4, pady=13,cursor='hand2').grid(row=4, column=3)
        
        # ===Cart Frame====
        
        Cart_Frame=Frame(Calcu_Cart_Farme,bd=3,relief=RIDGE)
        Cart_Frame.place(x=276,y=8,width=240,height=342)
        
        self.Cart_Title = Label(Cart_Frame, text="Cart \t Total Product : [0]", font=("goudy old style", 13),bg="lightgray")
        self.Cart_Title.pack(side=TOP,fill=X)
        
        
        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)
        
        self.Cart_Table=ttk.Treeview(Cart_Frame,columns=("Prod_ID","name","price","qnty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Cart_Table.xview)
        scrolly.config(command=self.Cart_Table.yview)
        
        self.Cart_Table.heading("Prod_ID",text="Prod_ID")
        self.Cart_Table.heading("name",text="Name")
        self.Cart_Table.heading("price",text="Price")
        self.Cart_Table.heading("qnty",text="Qnty")
        
        self.Cart_Table["show"]="headings"
        
        self.Cart_Table.column("Prod_ID",width=40)
        self.Cart_Table.column("name",width=80)
        self.Cart_Table.column("price",width=55)
        self.Cart_Table.column("qnty",width=25)
        
        
        self.Cart_Table.pack(fill=BOTH,expand=1)
        self.Cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)
        
        # ==== Add cart buttons frame===
        self.var_P_ID=StringVar()
        self.var_cname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        
        Add_Cart_Farme = Frame(self.root , bd=2, relief=RIDGE , bg="white")
        Add_Cart_Farme.place(x=424, y=560, width=520, height=120)
        
        lbl_Prod_name = Label(Add_Cart_Farme, text="Product Name", font=("times new roman",15),bg="white").place(x=5, y=5)
        txt_Prod_name = Entry(Add_Cart_Farme,textvariable=self.var_cname , font=("times new roman",15),bg="#f1eb9c", state='readonly').place(x=5, y=35 , width=190 , height=22)
        
        lbl_P_price = Label(Add_Cart_Farme, text="Price Per Quantity", font=("times new roman",15),bg="white").place(x=220, y=5)
        txt_P_price = Entry(Add_Cart_Farme,textvariable=self.var_price , font=("times new roman",15),bg="#f1eb9c", state='readonly').place(x=220, y=35 , width=160 , height=22)
        
        lbl_P_qty = Label(Add_Cart_Farme, text="Quantity", font=("times new roman",15),bg="white").place(x=400, y=5)
        txt_P_qty = Entry(Add_Cart_Farme,textvariable=self.var_qty , font=("times new roman",15),bg="#f1eb9c").place(x=400, y=35 , width=100 , height=22)
        
        self.lbl_inStock = Label(Add_Cart_Farme, text="In Stock", font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5, y=70)
        
        btn_clear_cart=Button(Add_Cart_Farme, text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="#607d8b",cursor="hand2").place(x=180,y=70 , width=110 , height=30)
        btn_add_cart=Button(Add_Cart_Farme, text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="#4caf50",cursor="hand2").place(x=320,y=70 , width=180 , height=30)
        
        
        # ====== bill section area
        billFrame= Frame(self.root , bd=2 , relief=RIDGE , bg='white')
        billFrame.place(x=950 , y=110 , width=405 , height=440)
        
        billTitle = Label(billFrame, text="Customer Bill Area", font=("goudy old style", 20 , "bold"),bg="purple",fg="white").pack(side=TOP,fill=X)
        
        scrolly = Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        
        scrolly.config(command=self.txt_bill_area.yview)
        
        
        # ==== Billing buttons===
        billMenuFrame= Frame(self.root , bd=2 , relief=RIDGE , bg='white')
        billMenuFrame.place(x=950 , y=560 , width=405 , height=120)
        
        self.lbl_amnt = Label(billMenuFrame, text='Bill Amount\n[0]', font=("goudy old style", 11 ,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2 , y=5 , width=120 , height=60)
        
        self.lbl_discount = Label(billMenuFrame, text='Discount\n[5%]', font=("goudy old style", 12 ,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=127 , y=5 , width=110 , height=60)
        
        self.lbl_net_pay = Label(billMenuFrame, text='Payable Amount\n[0]', font=("goudy old style", 12 ,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=242 , y=5 , width=156 , height=60)
        
        
        # === butttons of bill areas==
         
        btn_print = Button(billMenuFrame, text='Print',cursor='hand2',command=self.print_bill, font=("goudy old style", 13 ,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2 , y=70 , width=120 , height=43)
        
        btn_clear_all= Button(billMenuFrame, text='Clear All',cursor='hand2',command=self.clear_all, font=("goudy old style", 13 ,"bold"),bg="#607d8b",fg="white")
        btn_clear_all.place(x=127 , y=70 , width=110 , height=43)
        
        btn_generate= Button(billMenuFrame, text='Generate / Save Bill',command=self.generate_bill,cursor='hand2', font=("goudy old style", 12 ,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=242 , y=70 , width=156 , height=43)
        
        
        footer=Label(self.root , text="Inventory Management System | developed by Kyamuddin Siddique", font=("times new roman", 11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.show()
        # self.bill_top()
        self.update_date_time()
        
        # ====== All calculator Buttons Functions=====
    
    def get_input(self , num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)    
    
    
    def clear_cal(self):
        self.var_cal_input.set('')    
    
    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    
    
    
    def show(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             cur.execute("select Prod_ID,name,price,qnty,status from product where status='Active'")
             rows=cur.fetchall()
             self.product_Table.delete(*self.product_Table.get_children())
             for row in rows:
                self.product_Table.insert('',END,values=row)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Please Enter Name To Search",parent=self.root)
            else:
                cur.execute("select Prod_ID,name,price,qnty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!!!",parent=self.root)
                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_P_ID.set(row[0])
        self.var_cname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
    
    
    def get_data_cart(self,ev):
        f=self.Cart_Table.focus()
        content=(self.Cart_Table.item(f))
        row=content['values']
        self.var_P_ID.set(row[0])
        self.var_cname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
    
    
    def add_update_cart(self):
        if self.var_P_ID.get()=='':
            messagebox.showerror('Error',"Please Select Product from List",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror('Error',"Please Enter Quantity",parent=self.root)  
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error',"Please Enter Less Quantity Than Actual Quantity",parent=self.root)  
        else:
            # price_calcu=int(self.var_qty.get())*float(self.var_price.get())
            # price_calcu=float(price_calcu)
            price_calcu=self.var_price.get()
            cart_data=[self.var_P_ID.get(),self.var_cname.get(),price_calcu,self.var_qty.get(),self.var_stock.get()]
            
            # Update cart====
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_P_ID.get()==row[0]:
                    present='yes'
                    break
            
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('confirm',"Product Already in Cart \nDo You Want to Update | Remove Product From Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_calcu   # price    
                        self.cart_list[index_][3]=self.var_qty.get()  #quantity update    
            else:
                self.cart_list.append(cart_data)
            
            self.show_cart()
            self.bill_update()
    
    
    def bill_update(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amnt.config(text=f'Bill Amount(Rs.)\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay(Rs.)\n{str(self.net_pay)}')
        self.Cart_Title.config(text=f"Cart \t Total Product : [{str(len(self.cart_list))}]")
        
    def show_cart(self):
         try:
            self.Cart_Table.delete(*self.Cart_Table.get_children())
            for row in self.cart_list:
                self.Cart_Table.insert('',END,values=row)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def generate_bill(self):
        if self.var_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are Required",parent=self.root)
        elif len(self.cart_list)<=0:
            messagebox.showerror("Error",f"Please Add Product to the Cart",parent=self.root)
        else:
            # bill top===
            self.bill_top()
            # ===bill middle==
            self.bill_middle()
            # ===bill bottom==
            self.bill_bottom()
            
            #  saving bills in bill folder
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been Generated/Saved",parent=self.root)
            self.check_print=1
            
                      
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_tempelate=f'''
\t\tKyam's-Inventory
    Mob. No. 8874381506 , Uttar Pradesh-274404
{str("*"*47)}
 Customer Name: {self.var_name.get()}
 Mob. No.:{self.var_contact.get()}
 Bill No.:{str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQNTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)   
        self.txt_bill_area.insert('1.0',bill_top_tempelate)   
    
    def bill_bottom(self):
        bill_bottom_templete=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_templete)             
    
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                Prod_ID=row[0]
                name=row[1]
                qnty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+row[3]+"\tRs."+price)
                #=====udating quantity in product table==== 
                cur.execute('Update product set qnty=?,status=? where Prod_ID=?',(
                    qnty,
                    status,
                    Prod_ID
                    
                ))
                con.commit()
            con.close()
            self.show()    
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def clear_cart(self):
        self.var_P_ID.set('')
        self.var_cname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.Cart_Title.config(text=f"Cart \t Total Product : [0]")
        self.var_search.set('')
        self.check_print=0
        self.clear_cart()
        self.show()
        self.show_cart()    
    
    
    def update_date_time(self):
        time_=time.strftime("%H:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome Dear ! We are thrilled to have you here\t\t Date: {str(date_)} \t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
    
    def print_bill(self):
        if self.check_print==1:
            messagebox.showinfo('Print',"Please wait while Printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print',"Please Generate Bill First",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python main.py")
                       
if __name__=="__main__":       
    root=Tk()
    obj=BillClass(root)
    root.mainloop()
