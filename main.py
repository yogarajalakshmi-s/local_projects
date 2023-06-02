import requests
from datetime import datetime
import os

# https://pixe.la/
date = datetime.now().strftime('%Y%m%d')

# Create User
parameters = {
    "token": os.environ.get('HABIT_TRACKER_KEY'),
    "username": "ishwarya-07",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url="https://pixe.la/v1/users", json=parameters)
print(response)

# Create graph
graph_params = {
    "id": "graph1",
    "name": "Book Reading Tracker",
    "unit": "pages",
    "type": "int",
    "color": "momiji"
}

headers = {"X-USER-TOKEN": os.environ.get('HABIT_TRACKER_KEY')}
response = requests.post(url="https://pixe.la/v1/users/ishwarya-07/graphs", json=graph_params, headers=headers)
print(response.text)

# Post data
headers = {"X-USER-TOKEN": os.environ.get('HABIT_TRACKER_KEY')}
data_params = {
    "date": date,
    "quantity": str(input("How many pages did you read today?"))
}

response = requests.post(url="https://pixe.la/v1/users/ishwarya-07/graphs/graph1", json=data_params, headers=headers)
print(response.text)

# Update data
headers = {"X-USER-TOKEN": os.environ.get('HABIT_TRACKER_KEY')}
data_params = {
    "quantity": "25"
}

response = requests.put(url=f"https://pixe.la/v1/users/ishwarya-07/graphs/graph1/{date}", json=data_params, headers=headers)
print(response.text)

# Delete a pixel
headers = {"X-USER-TOKEN": os.environ.get('HABIT_TRACKER_KEY')}
response = requests.delete(url=f"https://pixe.la/v1/users/ishwarya-07/graphs/graph1/20230601", headers=headers)
print(response.text)
