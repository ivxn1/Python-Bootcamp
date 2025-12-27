import requests
from requests.auth import HTTPBasicAuth

user_emails = []
url = "https://api.sheety.co/8d13e767f4c12395e0b12333b04107e4/flightDeals/users"
response = requests.get(url=url, auth=HTTPBasicAuth(username="ivan", password="mypass"))
users = response.json()

print(users['users'])
for user in users['users']:
    print(user)
print(user_emails)


