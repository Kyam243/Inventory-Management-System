from tkinter import*
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk,messagebox
# for database
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Inventory Management $ystem   |   Developed By Kyamuddin Siddique  |  Presented by Priyadarshani Bhatt")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # all variables---
        self.var_cat_id=StringVar()
        self.var_cat_name=StringVar()
        
        self.var_searchtxt=StringVar()
        
        
        
        
        # ----> Title <----
        
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP, fill=X,padx=10,pady=10)
        
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",25),bg="white",).place(x=30,y=80)
        
        txt_name=Entry(self.root,textvariable=self.var_cat_name,font=("goudy old style",18),bg="#f1eb9c",).place(x=35,y=140,width=300)
        
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=350,y=140,width=150,height=30)
        
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=510,y=140,width=150,height=30)
        
        # ===========Search Section======
        
        lbl_search=Label(self.root,text="Search Category by Name",font=("sansarif",16), bg="white")
        lbl_search.place(x=688, y=100,)
        
        # text field(textbox) using (entry/text) entry using for short or onelines data or text using for long data
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt, font=("sansarif",15),bg="#f1eb9c").place(x=695,y=140,width=250)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("sansarif",15),bg="#4caf50",fg="white", cursor="hand2").place(x=968,y=140,width=90,height=27)
        

    # category Details----- using tree view because tree view is more effective
        
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=688,y=190,width=390,height=300)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.category_table=ttk.Treeview(cat_frame,columns=("Cat_ID","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        
        self.category_table.heading("Cat_ID",text="Category ID")
        self.category_table.heading("name",text="Name")
        
        self.category_table["show"]="headings"
        
        self.category_table.column("Cat_ID",width=80)
        self.category_table.column("name",width=100)
        
        
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        
        # images---->
        self.im1=Image.open("images/cat01.jpg")
        self.im1=self.im1.resize((300,250))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=30,y=190)
        
        # self.im2=Image.open("images/cat01.jpg")
        # self.im2=self.im2.resize((330,250))
        # self.im2=ImageTk.PhotoImage(self.im2)
        
        
        # self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        # self.lbl_im2.place(x=740,y=190)
        
        self.im3=Image.open("images/cat002.jpg")
        self.im3=self.im3.resize((305,250))
        self.im3=ImageTk.PhotoImage(self.im3)
        
        
        self.lbl_im3=Label(self.root,image=self.im3,bd=2,relief=RAISED)
        self.lbl_im3.place(x=350,y=190)
        
        self.show()
    
    # category data base
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror( "Error","Category name should be required" ,parent=self.root)
            
            else:
                cur.execute( " Select * from category where name=? " ,(self.var_cat_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror( "Error","Category already present,try different" ,parent=self.root)    
                
                else:
                    cur.execute( " Insert into category (name) VALUES(?) " ,(
                         self.var_cat_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success"," Category Added Successfully ",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f" Error due to : {str(ex)} ",parent=self.root)
    
    
    def show(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             cur.execute("select * from category")
             rows=cur.fetchall()
             self.category_table.delete(*self.category_table.get_children())
             for row in rows:
                self.category_table.insert('',END,values=row)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        
         
        self.var_cat_id.set(row[0])
        self.var_cat_name.set(row[1])
    
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("Error","Please Select Category name",parent=self.root)
            
            else:
                cur.execute("Select * from category where name=?",(self.var_cat_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category Name",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where name=?",(self.var_cat_name.get(),))
                        con.commit()
                    messagebox.showinfo("Deleted","Category Record Deleted Successfully",parent=self.root)
                    self.clear()
                    self.show()
                    self.var_cat_id.set(" ")
                    self.var_cat_name.set(" ")  
                    
                
            
                
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)   
    
    
    def search(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             if self.var_searchtxt.get()=="":
                 self.show()
            #  elif self.var_searchtxt.get()=="":    
            #      messagebox.showerror("Error","Category ID/Name is required ",parent=self.root)
             else:
                 cur.execute("select * from category where name LIKE '%"+(self.var_searchtxt.get()+"%'"))
                 row=cur.fetchall()
                 if len(row)!=None:
                     self.category_table.delete(*self.category_table.get_children())
                     for row in row:
                          self.category_table.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!!",parent=self.root)
                    #  name LIKE '%"+self.var_search.get()+"%'
                     
                     
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
             
    
    
    
    def clear(self):
        self.var_cat_id.set("")
        self.var_cat_name.set("")         
        self.show()
        



if __name__=="__main__":       
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()        