# https://www.twilio.com/docs/sms/quickstart/python

import requests
from twilio.rest import Client
import os

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "q": "Coimbatore,India",
    "appid": os.environ.get('WEATHER_API_KEY')
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_condition = data['weather'][0]['main']

client = Client(os.environ.get('ACCOUNT_SID'), os.environ.get('AUTH_TOKEN'))
message = client.messages \
    .create(
        body=f"Weather Report - Today's weather - {weather_condition}!",
        from_=os.environ.get('FROM_NUMBER'),
        to=os.environ.get('TO_NUMBER')
    )

print(message.sid)
