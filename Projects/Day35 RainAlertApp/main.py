import email
from email import message
import requests
import smtplib


OpenWeatherMap_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = [YOUR_API_KEY]
MY_EMAIL = [YOUR_EMAIL]
MY_PASSWORD = [YOUR_PASSWORD]

weather_params = {
    "lat": 42.190979,
    "lon": 24.332279,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(url=OpenWeatherMap_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:It is going to rain!\n\nBring an umbrella.")
