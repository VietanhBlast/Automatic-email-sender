import smtplib
import ssl
import time
import datetime as dt
from email.message import EmailMessage

subject ="email From python" #what will be sent
body = "this is a test email form python! lol wtf"
sender_email = "pythontester126@gmail.com"
receiver_email = "yan2020pham@gmail.com"
password = input("password here:") #google app key
send_time = dt.datetime(2023,9,30,20,40,0)#year,month,day,hour,min,sec
time.sleep(send_time.timestamp() - time.time())

message = EmailMessage()
message ["From"] = sender_email
message ["to"] = receiver_email
message ["Subject"] = subject

message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as sever:
    
    sever.login(sender_email,password)
    
    sever.sendmail(sender_email, receiver_email, message.as_string())
    