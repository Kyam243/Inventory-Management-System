from tkinter import*

# kivy===+=====================================
from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# ========================================================

from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import sqlite3  
import os
import email_pass 
import smtplib
import time

class Login_System(App):
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome Dear !!!! Have A Lovely Day | Developed By Kyamuddin Siddique")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        # self.icon = "logIcon1.png"
        
        self.otp=''
        
        # images
        self.im_bg=Image.open("images/logBg1.jpg")
        self.im_bg=self.im_bg.resize((1370,700))
        self.im_bg=ImageTk.PhotoImage(self.im_bg)
        
        
        self.lbl_im_bg=Label(self.root,image=self.im_bg)
        self.lbl_im_bg.place(x=0,y=0)
        
        
        # self.first_img=ImageTk.PhotoImage(file="images/phone.png")
        # self.lbl_first_img=Label(self.root,image=self.first_img,bd=0).place(x=200,y=45)
        
        
        # =====login Frame=====
        self.var_user_Id=StringVar()
        self.var_password=StringVar()
        login_frame=Frame(self.root,bd=0,relief=RIDGE,bg="#a9a9a9")
        login_frame.place(x=380,y=110,width=350,height=490)
        
        self.imk_bg=Image.open("images/key.png")
        self.imk_bg=self.imk_bg.resize((70,60))
        self.imk_bg=ImageTk.PhotoImage(self.imk_bg)
        
        
        self.lbl_imk_bg=Label(login_frame,image=self.imk_bg,bg="#a9a9a9")
        self.lbl_imk_bg.place(x=150,y=20)
        
        
        
        title=Label(login_frame,text="Login To Continue",bg="#a9a9a9",fg="#191970",font=("times new roman",28,"bold")).place(x=25,y=85,relwidth=1)
        
        self.var_utype=StringVar()
        
        cmb_utype=ttk.Combobox(login_frame,textvariable=self.var_utype,values=("User Type","Admin","Employee",), state='readonly',justify=CENTER,font=("sansarif",13))
        cmb_utype.place(x=55,y=140,width=205)
        cmb_utype.current(0)
        
        
        lbl_user=Label(login_frame,text="User ID",font=("Andalus",14),bg="#a9a9a9",fg="black").place(x=55,y=180)
        txt_user_name=Entry(login_frame,textvariable=self.var_user_Id,font=("times new roman",15)).place(x=55,y=210)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",14),bg="#a9a9a9",fg="black").place(x=55,y=255)
        txt_pass=Entry(login_frame,textvariable=self.var_password,show="*",font=("times new roman",15)).place(x=55,y=290)
        
        # lbl_user=Label(login_frame,text="User ID",font=("Andalus",14),bg="#a9a9a9",fg="black").place(x=55,y=190)
        # txt_user_name=Entry(login_frame,textvariable=self.var_user_Id,font=("times new roman",15)).place(x=55,y=220)
        
        # lbl_pass=Label(login_frame,text="Password",font=("Andalus",14),bg="#a9a9a9",fg="black").place(x=55,y=265)
        # txt_pass=Entry(login_frame,textvariable=self.var_password,show="*",font=("times new roman",15)).place(x=55,y=305)
        
        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",13,"bold"),bg="#87cefa",fg="black",activebackground="#00b0f0",activeforeground="black",cursor="hand2").place(x=162,y=355,width=95,height=30)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=420,width=250,height=2)
        or_hr=Label(login_frame,text="OR",font=("times new roman",15,"bold"),fg="lightgray",bg="#a9a9a9").place(x=150,y=405)
        
        btn_forget=Button(login_frame,text="Forget Password",command=self.forget_pass,bg="#a9a9a9",fg="#00759e",font=("times new roman",13),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").place(x=100,y=440)
        
        # btn_sign=Button(login_frame,text="Sign UP",bg="#a9a9a9",fg="#00759e",font=("times new roman",15),bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").place(x=55,y=355)
        
        # btn_login=Button(login_frame,text="Log In",command=self.login,bg="#a9a9a9",fg="#00759e",font=("times new roman",15),cursor="hand2",bd=0,activebackground="#a9a9a9",activeforeground="#0000ff").place(x=162,y=355)
        
        
        # animation images
        # self.im1=ImageTk.PhotoImage(file="images/imglog12.png")
        self.im1=Image.open("images/imglog12.png")
        self.im1=self.im1.resize((230,415))
        self.im1=ImageTk.PhotoImage(self.im1)
    
        self.im2=Image.open("images/imglog13.png")
        self.im2=self.im2.resize((230,415))
        self.im2=ImageTk.PhotoImage(self.im2)
    
        self.im3=Image.open("images/logAni17.png")
        self.im3=self.im3.resize((230,415))
        self.im3=ImageTk.PhotoImage(self.im3)
    
        self.im4=Image.open("images/logAmi9.png")
        self.im4=self.im4.resize((230,415))
        self.im4=ImageTk.PhotoImage(self.im4)
    
        self.im5=Image.open("images/logAni1.png")
        self.i52=self.im5.resize((230,415))
        self.im5=ImageTk.PhotoImage(self.im5)
    
        self.im6=Image.open("images/logAni2.jpeg")
        self.im6=self.im6.resize((230,415))
        self.im6=ImageTk.PhotoImage(self.im6)
    
        self.im7=Image.open("images/logAni3.jpeg")
        self.im7=self.im7.resize((230,415))
        self.im7=ImageTk.PhotoImage(self.im7)
    
        self.im8=Image.open("images/logAni6.jpeg")
        self.im8=self.im8.resize((230,415))
        self.im8=ImageTk.PhotoImage(self.im8)
    
        self.im9=Image.open("images/logAni7.jpeg")
        self.im9=self.im9.resize((230,415))
        self.im9=ImageTk.PhotoImage(self.im9)
    
        self.im10=Image.open("images/logAni8.jpeg")
        self.im10=self.im10.resize((230,415))
        self.im10=ImageTk.PhotoImage(self.im10)
    
        self.im11=Image.open("images/logAni10.png")
        self.im11=self.im11.resize((230,415))
        self.im11=ImageTk.PhotoImage(self.im11)
    
        self.im12=Image.open("images/logAni11.png")
        self.im12=self.im12.resize((230,415))
        self.im12=ImageTk.PhotoImage(self.im12)
    
        
        # self.im2=ImageTk.PhotoImage(file="images/imglog13.png")
        
        self.lbl_change_img=Label(self.root,bg="#a9a9a9")
        self.lbl_change_img.place(x=730,y=110,width=260,height=490)
        
        lbl_footer=Label(self.root,text="IMS-Inventory Management system  |  Developed by Kyamuddin Siddique | Priyadarshani Bhatt | Md. Ahmad Raza Ansari \nFor Any Querry Cont. : 8874381506", font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        
        
        self.animate()
        
        
     # all functions =======

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        # self.im3=self.im4
        # self.im4=self.im5
        # self.im5=self.im6
        # self.im6=self.im7
        # self.im7=self.im8
        # self.im8=self.im9
        # self.im9=self.im10
        # self.im10=self.im11
        # self.im11=self.im12
        # self.im12=self.im
        self.lbl_change_img.config(image=self.im)
        self.lbl_change_img.after(2000,self.animate)


    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_user_Id.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:    
                cur.execute("select utype from employee where Emp_ID=? AND pass=?",(self.var_user_Id.get(),self.var_password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid User ID / Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")    
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def forget_pass(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_user_Id.get()=="":
                messagebox.showerror("Error","User Type & User ID Must be Required",parent=self.root)
            else:    
                cur.execute("select email from employee where Emp_ID=?",(self.var_user_Id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid User ID , Please Try Again",parent=self.root)
                else:
                    
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_confi_pass=StringVar()
                    # calling send email function for otp
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error , Please try Again",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    
                    tittle=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg="#3f51b5",fg='white').pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP sent on Registered email",font=('times new roman',15,)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=('times new roman',15,),bg='lightyellow').place(x=20,y=100,width=250,height=30)
                    
                    self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=('times new roman',15,),bg='lightblue')
                    self.btn_reset.place(x=280,y=100,width=100,height=30)
                    
                    
                    lbl_new_pass=Label(self.forget_win,text="New Password",font=('times new roman',15,)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=('times new roman',15,),bg='lightyellow').place(x=20,y=190,width=250,height=30)
                    
                    lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=('times new roman',15,)).place(x=20,y=225)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_confi_pass,font=('times new roman',15,),bg='lightyellow').place(x=20,y=255,width=250,height=30)
                    
                    self.btn_update=Button(self.forget_win,text="Update",command=self.update_pass,state=DISABLED,font=('times new roman',15,),bg='lightblue')
                    self.btn_update.place(x=150,y=300,width=100,height=30)
                        
                    
                    
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    
    
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        
        subj="Kyam's Inventory-Reset Password OTP"
        msg=f"Dear Sir/Madam,\n\nYour OTP For Password Reset is {str(self.otp)}.\n\nwith Regards, \nKyam's Team"
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'
    
    
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Inailid OTP, Please Try Again",parent=self.forget_win)    
    
    def update_pass(self):
        if self.var_new_pass.get()=="" or self.var_confi_pass.get()=="":
            messagebox.showerror("Error","Password is Required",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_confi_pass.get():
            messagebox.showerror("Error","New Password & Confirm Password Must be Same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee SET pass=? where Emp_ID=?",(self.var_new_pass.get(),self.var_user_Id.get()))    
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
        
root=Tk()
obj=Login_System(root)
root.mainloop()    
