# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:05:28 2020

@author: VINAYAKA MUDRADI
"""

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import MySQLdb as msd
try:
    db= msd.connect('localhost','root','vinayaka','attendancesystem')
    print("\n [INFO] Database Connection Successful..!\n Connected to LocalHost")
    #messagebox.showinfo("Success", "Connection to LocalHost is Successful")
    
except msd.Error as e:
    print("\n [INFO] We got this error Specified below: "+e)
    #messagebox.showinfo("Failure", "Connection to LocalHost is Unsuccessful")
    exit(0)
    
print("\n [INFO] Collecting Email addresses.")
cursor=db.cursor()
receiver_email=[]
receiver_name={}
Query="SELECT Email,Name FROM student"
cursor.execute(Query)
result=cursor.fetchall()
for emailId,name in result:
        receiver_email.append(emailId)
        receiver_name[emailId]=name
subject = "Attendance Details"

sender_email = "email-id-of-sender"
password = 'your-password'



# Log in to server using secure context and send email
print("\n [INFO] Sending Emails...")


for email in receiver_email:
    message=None
    message = MIMEMultipart()
    message["From"] = sender_email
    #message["To"] = ", ".join(receiver_email)
    message["Subject"] = subject
    #message["Bcc"] = ", ".join(receiver_email)  # Recommended for mass emails
    
    # Add body to email



    filename = "Attendance_sheet.xlsx"  # In same directory as script
    
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
        )

    print(email)
    context = ssl.create_default_context()
    body = """\
<!DOCTYPE html>
<html>
<head>
<style>
.header{
	background-color:slateblue;
	border-radius:10px;
	}
.monospace {
  font-family: "Lucida Console", Courier, monospace;
}
.heading{
	text-align:center;
	color:white;
	}
.image{
	text-align:center;
	}
.body{
	background-color:white;
	height:500px;
	}
button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
.button3 {background-color: #f44336;} /* Red */ 
</style>
</head>
<body>
	<div class="header">
	<div class="image"><img src="https://www.canaraengineering.in//assets/images/logo.png" style="height:150px;width:140px;" ></div>
	<br/>
	<h1 style="color:black;text-align:center;">Canara Engineering College</h1>
	<h1 class="heading monospace">Attendance Notification</h1>
	<br/>
	
	<div class="body">
    <br/>
	<h1 style="color:#0000ff;">Hello, """+str(receiver_name[email])+"""</h1>
	<h3>Greetings,<h3>
	<h3 style="color:#000000;">Below is the attachment of your attendance status.
Please checkout your status and try to maintain 85% attendance if not maintained.Any corrections need to be made is intimated at the earliest to the respected faculty.<br/>
<span style="color:green;">If you have attended/organized any event and want to get the attendance for that day, please submit any proof for the same to the respected faculty at the earliest.</span></h3><br/>

<h3><span style="color:red;">Please make a note: </span>Maintaining 85% throughout the semister is mandatory to attend the final examination.</h3>
<h3>Thank you!</h3>

	</div>
	
	
	</div>
	<br/>
	
</body>
</html>
"""
    message.attach(MIMEText(body, "html"))
    message.attach(part)
    text = message.as_string()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, email, text)
    
print("\n [INFO] Email sent to the respected students mentioning their attendance status.")
wait_key=input()
