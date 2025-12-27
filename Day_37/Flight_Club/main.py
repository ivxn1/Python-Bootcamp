#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import time
from datetime import datetime, timedelta
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv()
SHEETY_USER = os.environ.get("SHEETY_USERNAME")
SHEETY_PASS = os.environ.get("SHEETY_PASSWORD")
DEPARTURE_CODE = "LON"
flight_search = FlightSearch()
data_man = DataManager()
notif_man = NotificationManager()

sheety_get_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")

response = requests.get(url=sheety_get_endpoint, auth=HTTPBasicAuth(SHEETY_USER, SHEETY_PASS))
sheet_data = response.json()

for price in sheet_data['prices']:
    if price['iata'] == '':
        price['iata'] = flight_search.add_city_code(price['city'])
        data_man.update_row(price)

tomorrow = datetime.now() + timedelta(days=1)
to_date = datetime.now() + timedelta(days=6*30)

user_emails = data_man.get_customer_info()

for dest in sheet_data['prices']:
    print(f"Getting flights to {dest['city']}...")
    flights = flight_search.search_flights(origin_city_code=DEPARTURE_CODE,
                                           destination_city_code=dest['iata'])

    cheapest_flight = find_cheapest_flight(flights)
    print(f"Destination: {dest['city']}: {cheapest_flight.price} GBP")
    time.sleep(2)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {dest['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.search_flights(
            DEPARTURE_CODE,
            dest['iata'],
            is_direct=False
        )

        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Destination: {dest['city']}: {cheapest_flight.price} GBP")

    if cheapest_flight.price != "N/A":
        if cheapest_flight.stops == 0:
            message = (f"Low price alert! Only {cheapest_flight.price} GBP to fly direct from {cheapest_flight.departure_airport_code} to "
                       f"{cheapest_flight.destination_airport_code} on {cheapest_flight.from_date} until {cheapest_flight.return_date}")

        else:
            message = (f"Low price alert! Only {cheapest_flight.price} GBP to fly from {cheapest_flight.departure_airport_code} to"
                       f"{cheapest_flight.destination_airport_code} with {cheapest_flight.stops} stops on {cheapest_flight.from_date}"
                       f"until {cheapest_flight.return_date}")

        notif_man.send_emails(user_emails, message)