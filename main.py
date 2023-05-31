# https://www.twilio.com/docs/sms/quickstart/python

import requests
import keys
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "q": "Coimbatore,India",
    "appid": keys.weather_api_key
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_condition = data['weather'][0]['main']

client = Client(keys.account_sid, keys.auth_token)
message = client.messages \
    .create(
        body=f"Weather Report - Today's weather - {weather_condition}!",
        from_=keys.from_number,
        to=keys.to_number
    )

print(message.sid)
