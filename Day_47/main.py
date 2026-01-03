import dotenv
from bs4 import BeautifulSoup
from requests import request
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
URL = "https://appbrewery.github.io/instant_pot/"
MIN_PRICE = 100.00

data = request(url=URL, method='get').text

soup = BeautifulSoup(data, 'html.parser')
price_element = soup.select_one('#corePriceDisplay_desktop_feature_div >'
                      ' div.a-section.a-spacing-none.aok-align-center.aok-relative >'
                      ' span.aok-offscreen')

price_value = float(price_element.text.split('$')[1].strip())
product_title = soup.select_one('#productTitle').get_text().strip()
print(product_title)

EMAIL = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

if price_value < MIN_PRICE:

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()           # Secure the connection
        server.login(EMAIL, PASSWORD)

        subject = "Low Price Notification"
        body = f"{product_title} is currently on the price of {str(price_value)}!"

        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            from_addr=EMAIL,
            to_addrs="ivanjelev2004@gmail.com",
            msg=message.encode('utf8')
        )