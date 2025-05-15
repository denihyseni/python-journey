##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
import random
import pandas
import os

datetime = dt.datetime
my_email = "deni.hyseni@gmail.com"
password = "ouzevaeyxzrqcpse"
today_day = datetime.now().day
today_month = datetime.now().month
letter_files = [f for f in os.listdir("letter_templates") if f.endswith(".txt")]
# 2. Check if today matches a birthday in the birthdays.csv

data = pandas.read_csv("birthdays.csv")
dict_data = {(row.month,row.day): row for (index,row) in data.iterrows()}


random_letter = random.choice(letter_files)

if (today_month,today_day) in dict_data:
    birthday_person = dict_data[(today_month, today_day)]
    with open("letter_templates/"+random_letter) as letter:
        file = letter.readlines()
        whole_letter = "".join(file).replace("[NAME]", birthday_person["name"])
        print(whole_letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{whole_letter}")







