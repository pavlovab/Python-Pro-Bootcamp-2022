import requests
from datetime import datetime


USERNAME = [YOUR_USERNAME]
TOKEN = [YOUR_TOKEN]
GRAPH_ID = "graph1"
pixella_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN, 
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixella_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Training Graph",
    "unit": "sets",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many sets did you do today?: ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)




