from datetime import datetime

import requests

USERNAME = "ivxvn"
TOKEN = "hadoxcnocndnqwdo"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users/"
user_params = {
    "token": "hadoxcnocndnqwdo",
    "username": "ivxvn",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "kilometer",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": "hadoxcnocndnqwdo"
}

# graph_response = requests.post(url=f"{pixela_endpoint}ivxvn/graphs", json=graph_params, headers=headers)
today = datetime.now().strftime("%Y%m%d")

pixel_post_params = {
    "date": "20250818",
    "quantity": "20",
}

# pixel_post_response = requests.post(url=f"{pixela_endpoint}ivxvn/graphs/{GRAPH_ID}", headers=headers, json=pixel_post_params)
# print(pixel_response.text)

pixel_update_params = {
    "quantity": "1"
}

# pixel_update_response = requests.put(url=f"{pixela_endpoint}ivxvn/graphs/{GRAPH_ID}/20250818", headers=headers, json=pixel_update_params)
# print(pixel_update_response.text)

pixel_delete_response = requests.delete(url=f"{pixela_endpoint}ivxvn/graphs/{GRAPH_ID}/20250818", headers=headers)
print(pixel_delete_response.text)