from tkinter import*
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk,messagebox
# for database
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Inventory Management $ystem   |   Developed By Kyamuddin Siddique  |  Presented by Priyadarshani Bhatt")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #====------all variables
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_Prod_ID=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qnty=StringVar()
        self.var_status=StringVar()
        
        
    
    # --=-----=-=
    
        product_frame=Frame(self.root, bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)
        
         # ---title--
        
        title=Label(product_frame,text="Manage Product Details",font=("sansarif",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        
        #====---category
        
         
        lbl_cat=Label(product_frame,text="Category",font=("sansarif",15),bg="white").place(x=25,y=60)
        
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list, state='readonly',justify=CENTER,font=("sansarif",15))
        cmb_cat.place(x=175,y=60,width=200)
        cmb_cat.current(0)
        
        
        # supplier==----
        
        
        
        lbl_sup=Label(product_frame,text="Supplier",font=("sansarif",15),bg="white").place(x=25,y=110)
        
        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list, state='readonly',justify=CENTER,font=("sansarif",15))
        cmb_sup.place(x=175,y=110,width=200)
        cmb_sup.current(0)
        
        # product name====--
        
        lbl_prd=Label(product_frame,text="Product Name",font=("sansarif",15),bg="white").place(x=25,y=160)
        
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("sansarif",15),bg="#f1eb9c").place(x=175,y=160,width=200)
        
        
        # product price==----
        
        
        lbl_price=Label(product_frame,text="Price",font=("sansarif",15),bg="white").place(x=25,y=210)
        
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("sansarif",15),bg="#f1eb9c").place(x=175,y=210,width=200)
        
        
        # ---> Quantity----==
        
        
        lbl_qnty=Label(product_frame,text="Quantity",font=("sansarif",15),bg="white").place(x=25,y=260)
        
        txt_qnty=Entry(product_frame,textvariable=self.var_qnty,font=("sansarif",15),bg="#f1eb9c").place(x=175,y=260,width=200)
        
        # --Status----->
        
        lbl_status=Label(product_frame,text="Status",font=("sansarif",15),bg="white").place(x=25,y=310)
        
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"), state='readonly',justify=CENTER,font=("sansarif",15))
        cmb_status.place(x=175,y=310,width=200)
        cmb_status.current(0)
        
        # buttons=---->
        
        btn_save=Button(product_frame,text="Save",command=self.add,font=("sansarif",15),bg="#2196f3",fg="white", cursor="hand2").place(x=10,y=400,width=100,height=28)
        
        btn_update=Button(product_frame,text="Update",command=self.update,font=("sansarif",15),bg="#4caf50",fg="white", cursor="hand2").place(x=120,y=400,width=100,height=28)
        
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("sansarif",15),bg="#f44336",fg="white", cursor="hand2").place(x=230,y=400,width=100,height=28)
        
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("sansarif",15),bg="#607d8b",fg="white", cursor="hand2").place(x=340,y=400,width=100,height=28)
    
    #--===->   serach baar
    
    
        Searchframe=LabelFrame(self.root,text="Search By",font=("caveat",15,"bold"), bd=2, relief=RIDGE, bg="white")
        Searchframe.place(x=480,y=7,width=600,height=80)
        
        # ---options (combobox  ya dropdown box)
        
        cmb_search=ttk.Combobox(Searchframe,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"), state='readonly',justify=CENTER,font=("sansarif",15))
        cmb_search.place(x=10, y=8, width=180)
        cmb_search.current(0)
        
        txt_search=Entry(Searchframe,textvariable=self.var_searchtxt, font=("sansarif",15),bg="#f1eb9c").place(x=200,y=10)
        
        btn_search=Button(Searchframe,text="Search",command=self.search,font=("sansarif",15),bg="#4caf50",fg="white", cursor="hand2").place(x=425,y=8,width=140,height=30)
        
        # product details
        
        pro_frame=Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=479,y=95,width=600,height=395)
        
        scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)
        
        self.product_table=ttk.Treeview(pro_frame,columns=("Prod_ID","Category","Supplier","name","price","qnty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("Prod_ID",text="Prod_ID")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qnty",text="Qnty")
        self.product_table.heading("status",text="Status")
        
        self.product_table["show"]="headings"
        
        self.product_table.column("Prod_ID",width=90)
        self.product_table.column("Category",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qnty",width=100)
        self.product_table.column("status",width=100)
        
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
        
        self.show()
        
        
    def fetch_cat_sup(self):
        self.cat_list.append("No Items In Cat")
        self.sup_list.append("No Record Of Sup")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
            
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
        
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
             
        
           
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product Already Present, try different",parent=self.root)    
                
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qnty,status) VALUES (?,?,?,?,?,?)",(
                         self.var_cat.get(),
                         self.var_sup.get(),
                         self.var_name.get(),
                         self.var_price.get(),
                         self.var_qnty.get(),
                         self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    
    
    
    def show(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             cur.execute("select * from product")
             rows=cur.fetchall()
             self.product_table.delete(*self.product_table.get_children())
             for row in rows:
                self.product_table.insert('',END,values=row)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
             
         
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        
        
        
        self.var_Prod_ID.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qnty.set(row[5])
        self.var_status.set(row[6])
                 
    
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_Prod_ID.get()=="":
                messagebox.showerror("Error","Please Select Product From List",parent=self.root)
            
            else:
                cur.execute("Select * from product where Prod_ID=?",(self.var_Prod_ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)    
                
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qnty=?,status=? where Prod_ID=?",(
                         self.var_cat.get(),
                         self.var_sup.get(),
                         self.var_name.get(),
                         self.var_price.get(),
                         self.var_qnty.get(),
                         self.var_status.get(),
                         self.var_Prod_ID.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_Prod_ID.get()=="":
                messagebox.showerror("Error","Select Product From The List",parent=self.root)
            
            else:
                cur.execute("Select * from product where Prod_ID=?",(self.var_Prod_ID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where Prod_ID=?",(self.var_Prod_ID.get(),))
                        con.commit()
                    messagebox.showinfo("Deleted","Product Record Deleted Successfully",parent=self.root)
                    self.clear()        
                
            
                
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qnty.set("")
        self.var_status.set("Active")
        self.var_Prod_ID.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        
        self.show()
                 
    def search(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             if self.var_searchby.get()=="Select":
                 messagebox.showerror("Error","Select the Options",parent=self.root)
             elif self.var_searchtxt.get()=="":
                 messagebox.showerror("Error","Search input should be required",parent=self.root)
             else:
                 cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.product_table.delete(*self.product_table.get_children())
                     for row in rows:
                          self.product_table.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!!",parent=self.root)
                     
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
        
        
        
        






if __name__=="__main__":       
    root=Tk()
    obj=productClass(root)
    root.mainloop()