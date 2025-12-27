import datetime
import os
import requests

HOST = os.environ.get("HOST")
EXERCISE_ENDPOINT = os.environ.get("EXERCISE_ENDPOINT")

app_key = os.environ.get("APP_KEY")
app_id = os.environ.get("APP_ID")

sheety_api_url = os.environ.get("SHEET_API_URL")

http_header = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

query = {
    "query": input("Tell me what exercise you did today: ")
}

response_data = requests.post(url=f"{HOST}{EXERCISE_ENDPOINT}", json=query, headers=http_header).json()

print(response_data)

print(response_data['exercises'][0]['name'].title())

exercise = response_data['exercises'][0]['name'].title()
duration = float(response_data['exercises'][0]['duration_min'])
calories = float(response_data['exercises'][0]['nf_calories'])

sheety_params = {
    "workout": {
        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_header = {
    "Authorization": os.environ.get("SHEETY_HEADER")
}
sheety_response = requests.post(url=sheety_api_url, json=sheety_params, headers=sheety_header)
sheety_response.raise_for_status()
