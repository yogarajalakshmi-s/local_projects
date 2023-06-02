# DAY - 33: API Calls and Endpoints

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raises exception when there is no successful response

print(response)
print(response.status_code)
print(response.content)

data = response.json()["iss_position"]
latitude = data['latitude']
longitude = data['longitude']
ll = (latitude, longitude)
print(ll)

# --------------------------------------------------------------------------------------------------------------------

# DAY - 35: API Authentication

# openweathermap.org
# https://openweathermap.org/current
import requests

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "test1234"

parameters = {
    "q": "Coimbatore",
    "appid": api_key
}

response = requests.get(url=owm_endpoint, params=parameters)
print(response.json())

# https://openweathermap.org/api/one-call-3

# parameters = {
#     "lat": 11.016010,
#     "lon": 76.970306,
#     "appid": api_key
# }
# response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
# print(response.json())

# post - requests.post(url=<url>, json=<parameters>, headers=<headers>)
# put  - requests.put(url=<url>, json=<parameters>, headers=<headers>)
# delete - requests.delete(url=<url>)
