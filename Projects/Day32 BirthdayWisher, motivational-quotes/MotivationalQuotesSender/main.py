import datetime as dt
import smtplib
import random


MY_EMAIL = [YOUR_EMAIL]
MY_PASSWORD = [YOUR_PASSWORD]

now = dt.datetime.now()
if now.weekday() == 3:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Motivation\n\n{random.choice(all_quotes)}")
