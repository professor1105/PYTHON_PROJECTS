import schedule 
import smtplib 
import requests 
from bs4 import BeautifulSoup 

def umbrellaReminder(): 
    city = "Kolkata"
    url = "https://www.google.com/search?q=weather+" + city 
    try:
        html = requests.get(url).content 
        soup = BeautifulSoup(html, 'html.parser') 
        temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
        time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
        sky = time_sky.split('\n')[1] 
        print(sky)
        if sky==["Rainy","Haze","Cloudy","Thunderstom","heavy rains"]: 
            smtp_object = smtplib.SMTP('smtp.gmail.com', 587)  
            smtp_object.starttls() 
            smtp_object.login("Your_email", "Your_password") 
            subject = "Umbrella Reminder"
            body = f"Take an umbrella before leaving the house. Weather condition for today is {sky} and temperature is {temperature} in {city}." 
            msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nYour_name".encode('utf-8') 
            smtp_object.sendmail("sender_email", "Receiver_email", msg) 
            smtp_object.quit() 
            print("Email Sent!")
    except Exception as e:
        print("An error occurred:", e)
        
schedule.every().day.at("10:00").do(umbrellaReminder)
while True: 
    schedule.run_pending()

#if These code is't working:
    #(https://www.youtube.com/watch?v=g_j6ILT-X0k&list=WL&index=1&t=121s)
    #try this YOUTUBE video.Thank You
