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

