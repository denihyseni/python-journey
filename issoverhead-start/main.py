import requests
from datetime import datetime
import smtplib
import schedule
import time


MY_EMAIL = "deni.hyseni@gmail.com"
PASSWORD = "ouzevaeyxzrqcpse"
MY_LAT = 42.6638771 # Your latitude
MY_LONG = 21.1640849 # Your longitude
def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if ((MY_LAT + 5 >= iss_latitude >= MY_LAT - 5) and
            (MY_LONG + 5 >= iss_longitude >= MY_LONG - 5)):
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def iss_email():
    if check_position() and time_now.hour > sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,
                                msg="Subject:Look Up!\n\nLook Up the ISS is above you")

schedule.every(60).seconds.do(check_position)
schedule.every(60).seconds.do(iss_email)
while True:
    schedule.run_pending()
    time.sleep(1)

