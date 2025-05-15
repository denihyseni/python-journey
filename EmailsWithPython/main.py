import smtplib
import datetime as dt
import random

my_email = "deni.hyseni@gmail.com"
password = "ouzevaeyxzrqcpse"
now = dt.datetime.now()
day_of_week = now.weekday()

day = now.day
print(day)
# with open("quotes.txt") as quotes:
#     data = quotes.readlines()
#     clean_list = [_.strip().encode("ascii","ignore").decode() for _ in data]
#
#
# if day_of_week == 2:
#     motivational_quote = random.choice(clean_list)
#     with smtplib.SMTP("smtp.gmail.com",587) as connection:
#          connection.starttls()
#          connection.login(user=my_email,password=password)
#          connection.sendmail(from_addr=my_email, to_addrs="",
#                             msg=f"Subject:Quote\n\n{motivational_quote}")







