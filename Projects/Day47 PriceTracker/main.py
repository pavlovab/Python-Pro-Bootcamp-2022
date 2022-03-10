from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.com/HP-24mh-FHD-Monitor-Built/dp/B08BF4CZSV/ref=lp_16225007011_1_4"
MY_EMAIL = [YOUR_EMAIL]
MY_PASSWORD = [YOUR_PASS]

BUY_PRICE = 250

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Language": "bg"
}

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

title = soup.find(id="title").get_text().strip()

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}")
 