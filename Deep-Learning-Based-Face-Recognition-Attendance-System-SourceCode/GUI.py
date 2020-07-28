# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:07:57 2020

@author: VINAYAKA MUDRADI
"""


try:
    import Tkinter as tk
except:
    import tkinter as tk
import os
from tkinter import *
from functools import partial 
from tkinter import messagebox
import MySQLdb as msd
from threading import Thread

try:
    db= msd.connect('localhost','root','vinayaka','attendancesystem')
    print("\n [INFO] Database Connection Successful..!\n Connected to LocalHost")
    #messagebox.showinfo("Success", "Connection to LocalHost is Successful")
    
except msd.Error as e:
    print("We got this error Specified below: "+str(e))
    #messagebox.showinfo("Failure", "Connection to LocalHost is Unsuccessful")
    exit(0)

cursor=db.cursor()

def addStudentData(usn,name,email):
    
    try:
        Query="INSERT INTO student (USN,Name,Email) VALUES ('%s','%s','%s')" %(str(usn.get()),str(name.get()),str(email.get()))
        cursor.execute(Query)
        messagebox.showinfo("Success", "Student information having USN "+str(usn.get())+" is added Successfully")
    except:
        messagebox.showinfo("Failure", "There occured some error in adding data of the student having USN "+str(usn.get())+"\nNote:It may be because of data already exists.")
        


def studentInfo(application=None):
    if application!=None:
        application.destroy()
    
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
    # sets the geometry of toplevel 
    newWindow.geometry("900x500+220+50")
    newWindow['bg']='#B8E2FC'
    usn = tk.StringVar()
    name=tk.StringVar()
    email=tk.StringVar()
    password=tk.StringVar()
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Student Information", bg="#B8E2FC", fg="#006400",font = ('Helvetica',20,"bold"))
    display.pack(fill=BOTH)
    #start
    Label(newWindow, text="Please enter the details",bg="#B8E2FC",font=("Times New Roman",15,"bold")).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    
    Label(newWindow, text="USN:", bg="#B8E2FC",font=(1),fg="red").pack()
    usn_entry = Entry(newWindow, textvariable=usn,font=(5))
    usn_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Name:",bg="#B8E2FC",font=(1),fg="red").pack()
    name_entry = Entry(newWindow, textvariable=name,font=(5))
    name_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Email ID:",bg="#B8E2FC",font=(1),fg="red").pack()
    email_entry = Entry(newWindow, textvariable=email,font=(5))
    email_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    result= partial(addStudentData,usn,name, email)
    Button(newWindow, text="Add Data", width=10, height=1,bg="black",fg="white",command=result).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    #errorMessage=Label(newWindow, text="hiii",bg="#B8E2FC",font = ('Helvetica',10),fg="red")
    #result= partial(checkAdminCredential,newWindow,errorMessage, username, password)
    
    #Button(newWindow, text="Login", width=10, height=1,bg="black",fg="white", command=result).pack()
    #errorMessage.pack()
    Label(newWindow, text="",bg="black",fg="black",font = ('Helvetica',1)).pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    #end
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Button(newWindow,text="BACK",command=lambda:[adminPage(newWindow)],width=50,bg="black",fg="white").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',10,"bold"),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)



def addFacultyData(password,name,email):
    
    try:
        Query="INSERT INTO faculty (Name,Password,EmailID) VALUES ('%s','%s','%s')" %(str(name.get()),str(password.get()),str(email.get()))
        cursor.execute(Query)
        messagebox.showinfo("Success", "Faculty information having EmailID "+str(email.get())+" is added Successfully")
    except:
        messagebox.showinfo("Failure", "There occured some error in adding data of the faculty having EmailID "+str(email.get())+"\nNote:It may be because of data already exists.")
       


def facultyInfo(application=None):
    if application!=None:
        application.destroy()
    
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("900x500+220+50")
    newWindow['bg']='#B8E2FC'
    password = tk.StringVar()
    name=tk.StringVar()
    email=tk.StringVar()
    password=tk.StringVar()
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Faculty Information", bg="#B8E2FC", fg="#006400",font = ('Helvetica',20,"bold"))
    display.pack(fill=BOTH)
    #start
    Label(newWindow, text="Please enter the details",bg="#B8E2FC",font=("Times New Roman",15,"bold")).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    
    Label(newWindow, text="Name:", bg="#B8E2FC",font=(1),fg="red").pack()
    usn_entry = Entry(newWindow, textvariable=name,font=(5))
    usn_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Email ID:",bg="#B8E2FC",font=(1),fg="red").pack()
    name_entry = Entry(newWindow, textvariable=email,font=(5))
    name_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Password:",bg="#B8E2FC",font=(1),fg="red").pack()
    email_entry = Entry(newWindow, textvariable=password,font=(5))
    email_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    result= partial(addFacultyData,password,name, email)
    Button(newWindow, text="Add Data", width=10, height=1,bg="black",fg="white",command=result).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    #errorMessage=Label(newWindow, text="hiii",bg="#B8E2FC",font = ('Helvetica',10),fg="red")
    #result= partial(checkAdminCredential,newWindow,errorMessage, username, password)
    
    #Button(newWindow, text="Login", width=10, height=1,bg="black",fg="white", command=result).pack()
    #errorMessage.pack()
    Label(newWindow, text="",bg="black",fg="black",font = ('Helvetica',1)).pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    #end
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Button(newWindow,text="BACK",command=lambda:[adminPage(newWindow)],width=50,bg="black",fg="white").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',10,"bold"),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    

def callbackPreprocess():
    os.system('baseofimage.py')
    print("Preprocess Completed Successfully.")
 

def preprocessData():
    messagebox.showinfo("INFO","Preprocess started Successfully. It may take some time. Kindly wait!")
    Thread(target=callbackPreprocess).start()
    

def callbackTrain():
    os.system('train.py')
    print("Training Completed Successfully.")
    #message.config(text="Training completed Successfully.")


def trainModel():
    messagebox.showinfo("INFO","Training started Successfully. It may take some time. Kindly wait!")
    Thread(target=callbackTrain).start()
        
    
def adminPage(application=None):
    if application!=None:
        application.destroy()
    
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("900x500+220+50") 
  
    # A Label widget to show in toplevel 
    newWindow['bg']='#B8E2FC'
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Administrator Section", bg="#B8E2FC", fg="#006400",font = ('Helvetica',25,"bold"))
    display.pack(fill=BOTH)
    Label(newWindow, text="Choose Your Option:",bg="#B8E2FC",font=("Times New Roman",15,"bold")).pack()
    Button(newWindow,text="Add Student Info",bg="white",fg="black",width=30,bd=5,command=lambda:[studentInfo(newWindow)]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    Button(newWindow,text="Add Faculty Info",bg="white",fg="black",width=30,bd=5,command=lambda:[facultyInfo(newWindow)]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    message=Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',15),fg="red")
    Button(newWindow,text="Preprocess Student Data",bg="white",fg="black",width=30,bd=5,command=lambda:[preprocessData()]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    Button(newWindow,text="Train CNN Model",bg="white",fg="black",width=30,bd=5,command=lambda:[trainModel()]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    
    Button(newWindow,text="LOGOUT",command=lambda:[startPage(newWindow)],width=50,bg="black",fg="white").pack()
    message.pack()
    Label(newWindow, text="",bg="black",fg="black",font = ('Helvetica',2)).pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',4),fg="red").pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',11,"bold"),fg="red").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',4),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)


def callbackAttendance():
    os.system('npp.py')
    print("Attendance Taken Successfully.")
    

def takeAttendance(): 
    Thread(target=callbackAttendance).start()


def viewAttendance():
    os.system("start Attendance_sheet.xlsx")
    print("Attendance sheet opened successfully.")


def checkFacultyPassword(message,facultyUser,oldPassword,updateButton):
    #print(facultyUser)
    Query="SELECT * FROM faculty WHERE Name='%s' and Password='%s'"%(str(facultyUser),str(oldPassword.get()))
    cursor.execute(Query)
    result=cursor.fetchall()
    #print(result)
    if len(result)==0:
        message.config(text="Old Password is Invalid!")
        updateButton["state"]="disabled"
    else:
        message.config(text="Verified")
        updateButton["state"]="active"


def updateFacultyPassword(message,facultyUser,newPassword,new_password,old_password):
    Query="UPDATE faculty SET Password='%s' WHERE Name='%s'"%(str(newPassword.get()),str(facultyUser))
    cursor.execute(Query)
    new_password.delete(0,END)
    old_password.delete(0,END)
    message.config(text="Password Updated Successfully.")



def changePasswordWindow(facultyUser,application=None):
    if application!=None:
        application.destroy()
    
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
  
    # sets the geometry of toplevel  
    newWindow.geometry("900x500+220+50") 
  
    # A Label widget to show in toplevel 
    newWindow['bg']='#B8E2FC'  
    oldpassword=tk.StringVar() 
    newPassword=tk.StringVar()
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Change Password", bg="#B8E2FC", fg="#006400",font = ('Helvetica',20,"bold"))
    display.pack(fill=BOTH)
    Label(newWindow, text="Old Password:", bg="#B8E2FC",font=(1),fg="red").pack()
    old_password = Entry(newWindow, textvariable=oldpassword,font=(5))
    old_password.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack() 
    Message=Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',15),fg="red")
    new_password = Entry(newWindow, textvariable=newPassword,font=(5))
    
    result2= partial(updateFacultyPassword,Message, facultyUser, newPassword,new_password,old_password)
    updateButton=Button(newWindow, text="Update", width=10, height=1,bg="black",fg="white", command=result2)
    result1= partial(checkFacultyPassword,Message, facultyUser, oldpassword,updateButton)
    Button(newWindow, text="Verify", width=10, height=1,bg="black",fg="white", command=result1).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',3)).pack() 
    Label(newWindow, text="New Password:", bg="#B8E2FC",font=(1),fg="red").pack()
    
    
    new_password.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack() 
    
    updateButton.pack()
    updateButton["state"]="disabled"
    Message.pack()
    Button(newWindow,text="LOGOUT",command=lambda:[startPage(newWindow)],width=50,bg="black",fg="white").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',5)).pack() 
    Label(newWindow, text="",bg="black",fg="black",font = ('Helvetica',2)).pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',4),fg="red").pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',11,"bold"),fg="red").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',4),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)


def callBackNotify():
    os.system('mail.py')
    print("Email sent to students mentioning their Attendance status.")
    
    
def notifyStudent():
    Thread(target=callBackNotify).start()
    
    
    
def facultyPage(application=None,facultyUser=None):
    if application!=None:
        application.destroy()
    
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
  
    # sets the geometry of toplevel  
    newWindow.geometry("900x500+220+50") 
  
    # A Label widget to show in toplevel 
    newWindow['bg']='#B8E2FC'  
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Faculty Section", bg="#B8E2FC", fg="#006400",font = ('Helvetica',25,"bold"))
    display.pack(fill=BOTH)
    message=Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',15),fg="red")
    Label(newWindow, text="Choose Your Option:",bg="#B8E2FC",font=("Times New Roman",15,"bold")).pack()
    Button(newWindow,text="Take Attendance",bg="white",fg="black",width=30,bd=5,command=lambda:[takeAttendance()]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    Button(newWindow,text="View Attendance Sheet",bg="white",fg="black",width=30,bd=5,command=lambda:[viewAttendance()]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    
    Button(newWindow,text="Notify Students",bg="white",fg="black",width=30,bd=5,command=lambda:[notifyStudent()]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    Button(newWindow,text="Change Password",bg="white",fg="black",width=30,bd=5,command=lambda:[changePasswordWindow(facultyUser,newWindow)]).pack()
    Label(newWindow,text="",font=('Helvetica',1),bg="#B8E2FC").pack()
    
    Button(newWindow,text="LOGOUT",command=lambda:[startPage(newWindow)],width=50,bg="black",fg="white").pack()
    message.pack()
    Label(newWindow, text="",bg="black",fg="black",font = ('Helvetica',2)).pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',4),fg="red").pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',11,"bold"),fg="red").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',4),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    
    
def checkFacultyCredential(window,errorMessage,username,password):
    facultyUser=username.get()
    facultyPassword=password.get()
    #print(facultyUser)
    Query="SELECT * FROM faculty WHERE Name='%s' AND Password='%s'" %(str(facultyUser),str(facultyPassword))
    cursor.execute(Query)
    result=cursor.fetchall()
    #print(result)
    if len(result)==0:
        errorMessage.config(text="UserName or Password is Invalid!")
    else:
        facultyPage(window,facultyUser)    
    
def checkAdminCredential(window,errorMessage,username,password):
    adminUser=username.get()
    adminPassword=password.get()
    #print(adminUser)
    Query="SELECT * FROM admin WHERE UserName='%s' AND Password='%s'" %(str(adminUser),str(adminPassword))
    cursor.execute(Query)
    result=cursor.fetchall()
    #print(result)
    if len(result)==0:
        errorMessage.config(text="UserName or Password is Invalid!")
    else:
        adminPage(window)
    
    

def adminLogInWindow(application=None): 
      
    # Toplevel object which will  
    # be treated as a new window 
    if application!=None:
        application.destroy()
    
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("900x500+220+50") 
  
    # A Label widget to show in toplevel 
    newWindow['bg']='#B8E2FC'
    username = tk.StringVar()
    password=tk.StringVar()
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Administrator LogIn", bg="#B8E2FC", fg="#006400",font = ('Helvetica',25,"bold"))
    display.pack(fill=BOTH)
    #start
    Label(newWindow, text="Please enter login details",bg="#B8E2FC",font=("Times New Roman",15,"bold")).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    
    Label(newWindow, text="Username:", bg="#B8E2FC",font=(1),fg="red").pack()
    username_login_entry = Entry(newWindow, textvariable=username,font=(5))
    username_login_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Password:",bg="#B8E2FC",font=(1),fg="red").pack()
    password__login_entry = Entry(newWindow, textvariable=password, show= '*',font=(5))
    password__login_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack() 
    errorMessage=Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',15),fg="red")
    result= partial(checkAdminCredential,newWindow,errorMessage, username, password)
    
    Button(newWindow, text="Login", width=10, height=1,bg="black",fg="white", command=result).pack()
    errorMessage.pack()
    Label(newWindow, text="",bg="black",fg="black").pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    #end
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',10)).pack()
    Button(newWindow,text="BACK",command=lambda:[startPage(newWindow)],width=50,bg="black",fg="white").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',10,"bold"),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)



def facultyLogInWindow(application=None): 
      
    # Toplevel object which will  
    # be treated as a new window 
    if application!=None:
        application.destroy()
    newWindow = Tk() 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Face Recognition Attendance System") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("900x500+220+50") 
  
    # A Label widget to show in toplevel 
    newWindow['bg']='#B8E2FC'
    username = tk.StringVar()
    password=tk.StringVar()
    display = Label(newWindow, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(newWindow, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(newWindow, text="Faculty LogIn", bg="#B8E2FC", fg="#006400",font = ('Helvetica',25,"bold"))
    display.pack(fill=BOTH)
    #start
    Label(newWindow, text="Please enter login details",bg="#B8E2FC",font=("Times New Roman",15,"bold")).pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Username:", bg="#B8E2FC",font=(1),fg="red").pack()
    username_login_entry = Entry(newWindow, textvariable=username,font=(5))
    username_login_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Password:",bg="#B8E2FC",font=(1),fg="red").pack()
    password__login_entry = Entry(newWindow, textvariable=password, show= '*',font=(5))
    password__login_entry.pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    errorMessage=Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',15),fg="red")
    result= partial(checkFacultyCredential,newWindow,errorMessage, username, password)
    Button(newWindow, text="Login", width=10, height=1,bg="black",fg="white",command=result).pack()
    errorMessage.pack()
    Label(newWindow, text="",bg="black",fg="black").pack(fill=BOTH)
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    #end
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',10)).pack()
    Button(newWindow,text="BACK",command=lambda:[startPage(newWindow)],width=50,bg="black",fg="white").pack()
    Label(newWindow, text="",bg="#B8E2FC",font = ('Helvetica',1)).pack()
    Label(newWindow, text="Managed By:",bg="#B8E2FC",font = ('Helvetica',13)).pack()
    Label(newWindow, text="CEC & Canara High School Association",bg="#B8E2FC",font = ('Helvetica',10,"bold"),fg="red").pack()
    display = Label(newWindow, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    
    
  
  
    
    
    
def startPage(application=None):
    if application!=None:
        application.destroy()
    application = tk.Tk()
    application.title("Face Recognition Attendance System")
    application.geometry("900x500+220+50")
    #application.configure(bg='white')
    application['bg']='#B8E2FC'
    display = Label(application, text="CANARA ENGINEERING COLLEGE", bg="#0000A0", fg="white",font = ('Franklin Gothic Demi',30,"bold"))
    display.pack(fill=BOTH) 
    display = Label(application, text="Benjanapadav, Mangalore", bg="#0000A0", fg="white",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(application, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',3))
    display.pack(fill=BOTH)
    display = Label(application, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',10))
    display.pack(fill=BOTH)
    display = Label(application, text="Attendance System", bg="#B8E2FC", fg="black",font = ('Comic Sans MS',40))
    display.pack(fill=BOTH)
    display = Label(application, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',60))
    display.pack(fill=BOTH)
    button=Button(application,text="ADMIN",bg="black",fg="white",command=lambda:[adminLogInWindow(application)])
    button.pack(fill=BOTH)
    button=Button(application,text="FACULTY",bg="black",fg="white", command=lambda:[facultyLogInWindow(application)])
    button.pack(fill=BOTH)
    display = Label(application, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    display = Label(application, text="Quality Education At Affordable Cost", bg="#B8E2FC", fg="blue",font = ('Helvetica',20))
    display.pack(fill=BOTH)
    display = Label(application, text="www.canaraengineering.in", bg="#B8E2FC", fg="black",font = ('Helvetica',15))
    display.pack(fill=BOTH)
    display = Label(application, text="Ph:0824-2278666 | Fax:0824-2278675", bg="#B8E2FC", fg="black",font = ('Helvetica',15))
    display.pack(fill=BOTH)
    display = Label(application, text="", bg="#B8E2FC", fg="#B8E2FC",font = ('Comic Sans MS',2))
    display.pack(fill=BOTH)
    display = Label(application, text="", bg="#f81894", fg="#f81894",font = ('Helvetica',1))
    display.pack(fill=BOTH)
    #application.mainloop()
    

application=tk.Tk()
startPage(application)
application.mainloop()

#f81894