import requests
from datetime import datetime


MY_LAT = 42.6638771
MY_LNG = 21.1640849
# stock_response = requests.get(url="http://api.open-notify.org/iss-now.json")
# stock_response.raise_for_status()
#
# data =stock_response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_pos = (longitude,latitude)
# print(iss_pos)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)