import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()


class DataManager:
    def __init__(self):
        self.SHEETY_USER = os.environ.get("SHEETY_USERNAME")
        self.SHEETY_PASS = os.environ.get("SHEETY_PASSWORD")
        self.SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")

    def update_row(self, row_data):
        url = f"{self.SHEETY_PRICES_ENDPOINT}{row_data['id']}"
        params = {
            "price": row_data
        }
        response = requests.put(url, json=params, auth=HTTPBasicAuth(self.SHEETY_USER, self.SHEETY_PASS))
        response.raise_for_status()

    def get_customer_info(self):
        user_emails = []
        url = self.SHEETY_USERS_ENDPOINT
        response = requests.get(url=url, auth=HTTPBasicAuth(self.SHEETY_USER, self.SHEETY_PASS))
        users = response.json()

        for user in users['users']:
            user_emails.append(user['whatIsYourEmailAddress?'])

        return user_emails
