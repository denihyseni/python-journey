import requests
from twilio.rest import Client
import os

OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"
api_key= os.environ.get("OMW_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat" :41.926407,
    "lon" : 13.095000,
    "appid": api_key,
    "cnt":4,
}

response = requests.get(OMW_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
list_weather = weather_data["list"]

# cod = data["cod"]
# print(cod)
# print(data["list"])
# #
# # print(weather_id)
# # print(description)
will_rain = False
for n in list_weather:
    weather_id = n["weather"][0]["id"]
    if weather_id < 700:
           will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today bring an ☔️",
        from_="+12314402292",
        to="+15558675310",
    )
