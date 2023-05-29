import requests
from datetime import datetime

latitude = 11.001812
longitude = 76.962843

parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0  # 24-hour format
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
# print(sunrise, sunset)
print(sunrise_hour, sunset_hour)

now = datetime.now()
print(now.hour)
