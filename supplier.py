from tkinter import*
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk,messagebox
# for database
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Inventory Management $ystem   |   Developed By Kyamuddin Siddique  |  Presented by Priyadarshani Bhatt")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ------------======-------===========================
        # All Variables--------
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        
        # self.root-----
        
        # self.root=LabelFrame(self.root,text="Search employee",font=("caveat",15,"bold"), bd=2, relief=RIDGE, bg="white")
        # self.root.place(x=250,y=20,width=600,height=70)
        
        # ---options (combobox  ya dropdown box)
        
        lbl_search=Label(self.root,text="Search by Invoice No.",font=("sansarif",14))
        lbl_search.place(x=625, y=80,)
        
        # text field(textbox) using (entry/text) entry using for short or onelines data or text using for long data
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt, font=("sansarif",15),bg="#f1eb9c").place(x=830,y=80,width=135)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("sansarif",15),bg="#4caf50",fg="white", cursor="hand2").place(x=975,y=79,width=85,height=27)
        
        
        # ---title--
        
        title=Label(self.root,text="Supplier Details",font=("sansarif",20, "bold"),bg="#0f4d7d",fg="white").place(x=40,y=10,width=1020, height=40)
        
        
        
        # content----------
        
        # 1st Row
        
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("sansarif",15),bg="white").place(x=40,y=80)
                
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("sansarif",15),bg="#f1eb9c").place(x=165,y=80,width=180)        
        
        
        # 2nd Row
        
        lbl_name=Label(self.root,text="Name",font=("sansarif",15),bg="white").place(x=40,y=120)
                        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("sansarif",15),bg="#f1eb9c").place(x=165,y=120,width=180)        
        
        
        
        # 3rd Row
        
        lbl_contact=Label(self.root,text="Contact No.",font=("sansarif",15),bg="white").place(x=40,y=160)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("sansarif",15),bg="#f1eb9c").place(x=165,y=160,width=180)
                
        
        
        # 4th Row------
        
        lbl_desc=Label(self.root,text="Description",font=("sansarif",15),bg="white").place(x=40,y=200)
        
        
        self.txt_desc=Text(self.root,font=("sansarif",15),bg="#f1eb9c")
        self.txt_desc.place(x=165,y=200,width=430,height=170)
        
        
        
        
        
        # button before content------
        
        btn_save=Button(self.root,text="Save",command=self.add,font=("sansarif",15),bg="#2196f3",fg="white", cursor="hand2").place(x=165,y=432,width=100,height=35)
        
        btn_update=Button(self.root,text="Update",command=self.update,font=("sansarif",15),bg="#4caf50",fg="white", cursor="hand2").place(x=275,y=432,width=100,height=35)
        
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("sansarif",15),bg="#f44336",fg="white", cursor="hand2").place(x=385,y=432,width=100,height=35)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("sansarif",15),bg="#607d8b",fg="white", cursor="hand2").place(x=495,y=432,width=100,height=35)
        
        
        
        
        
        # supplier Details----- using tree view because tree view is more effective
        
        
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=625,y=120,width=435,height=350)
        
        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)
        
        self.supplierTable=ttk.Treeview(sup_frame,columns=("Invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        
        self.supplierTable.heading("Invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact No.")
        self.supplierTable.heading("desc",text="Description")
        
        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("Invoice",width=80)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=150)
        
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        
        self.show()
        
        
        # ---====--==-=-=--=-=-=-=-=-=-=-=-creating data base or extracting them---==-=-=
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No. already assigned,try different",parent=self.root)    
                
                else:
                    cur.execute("Insert into supplier (Invoice,name,contact,desc) VALUES (?,?,?,?)",(
                         self.var_sup_invoice.get(),
                         self.var_name.get(),
                         self.var_contact.get(),
                         self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    
    
    
    def show(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             cur.execute("select * from supplier")
             rows=cur.fetchall()
             self.supplierTable.delete(*self.supplierTable.get_children())
             for row in rows:
                self.supplierTable.insert('',END,values=row)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
             
         
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        
        
        
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),
                 
    
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)    
                
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where Invoice=?",(
                         self.var_name.get(),
                         self.var_contact.get(),
                         self.txt_desc.get('1.0',END),
                         self.var_sup_invoice.get(),
                         
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            
            else:
                cur.execute("Select * from supplier where Invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where Invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                    messagebox.showinfo("Deleted","Supplier Record Deleted Successfully",parent=self.root)
                    self.clear()  
                    
                
            
                
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END),
        self.var_searchtxt.set("")
        
        self.show()
                 
    def search(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             if self.var_searchtxt.get()=="":
                 self.show()
            #  elif self.var_searchtxt.get()=="":    
            #      messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
             else:
                 cur.execute("select * from supplier where Invoice LIKE '%"+(self.var_searchtxt.get()+"%'"))
                 row=cur.fetchall()
                 if len(row)!=None:
                     self.supplierTable.delete(*self.supplierTable.get_children())
                     for row in row:
                          self.supplierTable.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!!",parent=self.root)
                     
                     
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       
        
if __name__=="__main__":       
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()