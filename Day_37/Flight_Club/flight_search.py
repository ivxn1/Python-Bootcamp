import datetime
import os
from datetime import timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = os.environ.get("AMADEUS_TOKEN_ENDPOINT")
CITY_CODE_SEARCH_ENDPOINT = os.environ.get("AMADEUS_CITY_CODE_SEARCH_ENDPOINT")
FLIGHT_SEARCH_ENDPOINT = os.environ.get("AMADEUS_FLIGHTS_SEARCH_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_token()

    def _get_token(self):
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        token_response = requests.post(url=TOKEN_ENDPOINT, data=data).json()
        access_token = token_response["access_token"]
        return access_token

    def add_city_code(self, city_name):
        params = {
            "keyword": city_name
        }
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(url=CITY_CODE_SEARCH_ENDPOINT, params=params, headers=header)

        try:
            country_code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"Index Error: No airport code found for {city_name}!")
            return "N/A"
        except KeyError:
            print(f"Key Error: No airport code found for {city_name}!")
            return "Not found"
        else:
            return country_code

    def search_flights(self, origin_city_code, destination_city_code, days_in_advance=20, is_direct=True):
        header = {
            "Authorization": "Bearer " + self._token
        }

        today = datetime.datetime.now()
        start_date = today + timedelta(days=1)
        end_date = today + timedelta(days=days_in_advance)

        all_flights = []
        for day_offset in range(0, days_in_advance):
            departure_date = (start_date + timedelta(days=day_offset)).strftime("%Y-%m-%d")
            return_date = (start_date + timedelta(days=day_offset + 7)).strftime("%Y-%m-%d")

            query = {
                "originLocationCode": origin_city_code,
                "destinationLocationCode": destination_city_code,
                "departureDate": departure_date,
                "returnDate": return_date,
                "adults": 1,
                "nonStop": "true" if is_direct else "false",
                "currencyCode": "CNY",
                "max": "5",
            }

            response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=header, params=query)

            if response.status_code == 200:
                flights = response.json().get('data', [])
                if flights:
                    all_flights.extend(flights)
            else:
                print(f"Error fetching flights for {departure_date}: {response.status_code}")
                print(response.text)

        return all_flights