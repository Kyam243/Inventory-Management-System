import sqlite3
def create_db():
    # making connection to the database file using con variable 
    con=sqlite3.connect(database=r'ims.db')
    
    # r is just like a path for avoiding errors
    
    
    # belowe curser are used for executing querry
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    
    con.commit()
    
    
    # supplier table
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(Invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    
    con.commit()
    
    # category table---
    cur.execute("CREATE TABLE IF NOT EXISTS category(Cat_ID INTEGER PRIMARY KEY ,name text )")
    
    con.commit()
    
    # product table
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(Prod_ID INTEGER PRIMARY KEY ,Category text,Supplier text,name text,price text,qnty text,status text)")
    
    con.commit()
    
    
    # calling create_db function
create_db()