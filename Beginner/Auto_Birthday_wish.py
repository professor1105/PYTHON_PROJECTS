import smtplib 
import time
import datetime as dt


def BirthDay_wish(name,email): 
    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.starttls()
    server.login("sender_email","password")
    subject="Happy Birthday Bro"
    Body=f"Happy Birthday {name} , Many many happy returns of the day."
    msg=f"Subject:{subject}\n\n{Body}\n\nRegards,\nSender_name".encode('utf-8')
    server.sendmail("sender_email",email,msg)
    server.quit()

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    BirthDay_wish(name,email)
    print('email sent')


name=input("name: ")
email=input("email: ").lower()
first_email_time = dt.datetime(2024,4,4,20,57,0)     #format(YYYY,MM,DD,H,M,S) & H=24 hour format
interval = dt.timedelta(minutes=2*60) 

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval