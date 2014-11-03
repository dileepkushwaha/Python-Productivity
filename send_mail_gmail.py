#!/usr/bin/python
import smtplib
import sys
import re
import getpass

From =raw_input("please enter Sender email address:")
if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{3,}$", From)!=None:
	print 'To address is', From

else:
	print 'Invalid To email.'
Recipient =raw_input("please enter Recievers email address:")
if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{3,}$", Recipient)!=None:
        print 'Reciepint mail is', Recipient

else:
        print 'Invalid reciepient mail.'

Subject=raw_input("please enter your Subject:")
print 'your Subject is', Subject

Mess = raw_input("please enter the message:")

Messege = """From: <%(fadd)s>
To: <%(tadd)s>
Subject: %(Sub)s

%(Mes)s
"""% {'fadd': From, 'tadd': Recipient, 'Sub': Subject, 'Mes': Mess}  
 
username = raw_input("please enter your username again:")
password = getpass.getpass('Enter your Password:')
  
try: 
	server = smtplib.SMTP('smtp.gmail.com:587')  
	server.ehlo() 
	server.starttls() 
	server.ehlo() 
	server.login(username,password)  
	server.sendmail(From, Recipient, Messege)  
	server.quit() 
	print 'mail sent'
except Exception:
   print "Error: unable to send email"

