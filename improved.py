import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd
import schedule
import time


subject ="email From python" #what will be sent

sender_email = "pythontester126@gmail.com"
password = input("password here:") #google app key

email_list = pd.read_excel('C:/Users/vieta/PycharmProjects/pythonProject for fun/email.xlsx')
names = email_list['NAME']
emails = email_list['EMAIL']

context = ssl.create_default_context()

def send_mail(): # function that sends an email 
    print("Sending Email!")
    for i in range(len(emails)):
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as sever:
            name = names[i]
            receiver_emails = emails[i]
        
            body = "this is a test email form python! lol "+ name
        
            message = EmailMessage()
            message ["From"] = sender_email
            message ["to"] = receiver_emails
            message ["Subject"] = subject
            message.set_content(body)
        
            sever.login(sender_email,password)
            sever.sendmail(sender_email, [receiver_emails], message.as_string())
            
def job(t):
    send_mail(), t
    return

schedule.every(1).day.at("15:15").do(job,'It is time')

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
    
    