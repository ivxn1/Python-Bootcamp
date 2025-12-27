import time

import requests
import datetime
import smtplib

def check_iss_proximity() -> bool:
    MY_LONG = 23.366144
    MY_LAT = 42.533688

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_long = float(iss_data['iss_position']['longitude'])
    iss_lat = float(iss_data['iss_position']['latitude'])

    if MY_LONG - 5 <= iss_long <= MY_LONG + 5 and MY_LAT - 5 <= iss_lat <= MY_LAT + 5:
        return True
    else:
        return False

def check_if_nighttime():
    parameters = {
        "lat": 42.533688,
        "lng": 23.366144,
        "formatted": 0,
        "tzid": "Europe/Sofia"
    }

    weather_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    weather_response.raise_for_status()
    data = weather_response.json()
    sunrise_hour = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset_hour = int(data['results']['sunset'].split("T")[1].split(":")[0])

    hour_now = datetime.datetime.now().hour
    if hour_now < sunrise_hour or hour_now > sunset_hour:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if check_iss_proximity() and check_if_nighttime():
            sender_email = 'ivxn.zhelev@gmail.com'
            recipient_email = 'ivanjelev2004@gmail.com'
            password = 'icrlgbgthmuwasrs'

            with smtplib.SMTP(host='smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=sender_email, password=password)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=recipient_email,
                    msg="Subject: The ISS is above you right now!\n\nYou can go outside and look up to find the ISS orbiting the Earth!"
                )
