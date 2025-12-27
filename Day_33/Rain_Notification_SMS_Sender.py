import os
import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": 13.756331,
    "lon": 100.501762,
    "appid": "d47ace0d9e83989651eccfaadbf22177",
    "cnt": 4
}

response = requests.get(url=endpoint, params=params)
response.raise_for_status()

data = response.json()
will_it_rain = False

for hour in data['list']:
    if hour['weather'][0]['id'] < 700:
        will_it_rain = True

if will_it_rain:
    account_id = ''
    api_key = os.environ.get("TWILIO_API_KEY")
    from_num = "+17019229062"
    to_num = "+359887870370"
    client = Client(account_id, api_key)

    message = client.messages.create(
        body="Bring an umbrella!",
        from_=from_num,
        to=to_num
    )

