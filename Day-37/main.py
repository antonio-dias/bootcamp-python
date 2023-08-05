import requests
from datetime import datetime


USERNAME = ""
TOKEN = ""
GRAPH_NAME = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# CREATE USER
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_NAME,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
"X-USER-TOKEN": TOKEN
}

# CREATE GRAPH
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.today()
today = datetime(year=2023, month=8, day=3)
print(today)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}

# CREATE PIXEL
# response = requests.post(f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_NAME}", json=pixel_config, headers=headers)
# print(response.text)

pixel_update_config = {
    "quantity": "7"
}

# UPDATE PIXEL
# response = requests.put(
#     url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_NAME}/{today.strftime('%Y%m%d')}",
#     json=pixel_update_config,
#     headers=headers
# )
# print(response.text)

# DELETE PIXEL
# response = requests.delete(
#     url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_NAME}/{today.strftime('%Y%m%d')}",
#     headers=headers
# )
# print(response.text)
