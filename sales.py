from tkinter import*
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk,messagebox
# for database
import sqlite3
# os means operating system used to get data or element from the folder to show
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+140")
        self.root.title("Inventory Management $ystem   |   Developed By Kyamuddin Siddique  |  Presented by Priyadarshani Bhatt")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.bill_list=[]
        self.var_invoice=StringVar()
        
        # title--->
        lbl_title=Label(self.root,text="Bill Section",font=("goudy old style",28),bg="#191970",fg="white",bd=3,relief=RIDGE).pack(side=TOP, fill=X,padx=10,pady=10)
        
        lbl_invoice=Label(self.root,text="Invoice No. ", font=("times new roman", 15),bg="white").place(x=30,y=80)
        
        txt_invoice=Entry(self.root,textvariable=self.var_invoice, font=("times new roman", 15),bg="#f1eb9c").place(x=140,y=80, width=200,height=28)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3", fg="white",cursor="hand2").place(x=360,y=80,width=120,height=26)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="#607d8b", fg="white",cursor="hand2").place(x=490,y=80,width=120,height=26)
        
        # Bill list---=-->
         
        sales_Frame=Frame(self.root,bd=2,relief=RIDGE)
        sales_Frame.place(x=30,y=130,width=200,height=340)
        
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.sales_List=Listbox(sales_Frame,font=("sansarif",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_List.yview)
        self.sales_List.pack(fill=BOTH,expand=1)
        self.sales_List.bind("<ButtonRelease-1>",self.get_data)
        # Bill Area---=->
        bill_Frame=Frame(self.root,bd=2,relief=RIDGE)
        bill_Frame.place(x=260,y=130,width=410,height=340)

        lbl_title2=Label(bill_Frame,text="Customer Bill Section",font=("goudy old style",19),bg="#98fb98").pack(side=TOP, fill=X)

        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="#f1eb9c",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        # image----->
        self.bill_img1=Image.open("images/cat2.jpg")
        self.bill_img1=self.bill_img1.resize((450,300))
        self.bill_img1=ImageTk.PhotoImage(self.bill_img1)
        
        lbl_image=Label(self.root,image=self.bill_img1,bd=0)
        lbl_image.place(x=680,y=120)

        self.show()
# ===------== functions --==to get data from bill folder in the bil list using OS which is imported above
    
    def show(self):
        del self.bill_list[:]
        self.sales_List.delete(0,END)
        # print(os.listdir('bill'))
        for i in os.listdir('bill'):
            # if i.split('.')[-1] <--- yah list ko split kr dega '.'or '-1 se jis se '.' ke baad ka file name show hoga means extention show hoga 
            if i.split('.')[-1]=='txt':
                self.sales_List.insert(END,i)
                self.bill_list.append(i.split('.')[0])
        
    
    def get_data(self,ev):
        index_=self.sales_List.curselection()
        file_name=self.sales_List.get(index_)
        
        # print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()    
    
    
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. Should Be Required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)        
    
    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)    
        
    
    
if __name__=="__main__":       
    root=Tk()
    obj=salesClass(root)
    root.mainloop()