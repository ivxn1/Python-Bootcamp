import dotenv
from bs4 import BeautifulSoup
from requests import request
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
URL = "https://www.amazon.fr/Cuiseur-riz-Tristar-RK-6127-Fonction/dp/B00RXQJE5G?ref_=Oct_d_obs_d_3457200031_0&pd_rd_w=dePtP&content-id=amzn1.sym.a4727bbc-c591-4595-8007-dd0652e02b4b&pf_rd_p=a4727bbc-c591-4595-8007-dd0652e02b4b&pf_rd_r=R5C00WY8GTXCK0QM67T0&pd_rd_wg=pnsjy&pd_rd_r=11b51fd5-36d0-4aff-8096-f39505cad365&pd_rd_i=B00RXQJE5G&th=1"
MIN_PRICE = 100.00

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "bg-BG,bg;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

COOKIES = {
    "lc-acbfr": "fr_FR",
    "lc-main": "en_US",
    "rxc": "AOytNS0FMnddUfGvgi0",

    # amazon.com
    "session-id": "145-8309940-4499056",
    "session-id-time": "2082787201l",
    "session-token": "+2ZfckaN2xv96gKdaIintsA2GyAKvMzKcOcvXt/gGs2BDlXKUi9axE+fhDhpiKt/INW3Dwhw3mEqSaIuNePmIdWZeYTtLS8PXvdM+cdcvyEx0LIP06DHb7Ns47uPAT+iCGa/UbrvycRU0BaWXS7e1FEkXK6mwAwXDToqBCD17b6stUTkg0OBKGxhGz0axPcmStaI7f0znTSa3e11RjSwJ5TqNsXNakHIGfXiZkcVuHOZVegmVTq8vKrZv9xJmUjrRqV9V1NLCE9W2MPIpZomzIFz4ae+7UNCbGhKHQx6V55vrwYsho/wqWLoXC1NoEHHKMHYbngXJxZwF5pgRFxzth+Whup3J6Tb",

    # amazon.fr (same cookie names overwrite if combined)
    "session-id-fr": "521-2682378-7201248",
    "session-id-time-fr": "2082787201l",
    "session-token-fr": "iwgPqBsQ9zfDWiO4BxhxgCp3iFhyQTB5Vbm8j5EJct85e/cOKLqrGPE6Is6dgYmmXMUjm9vpJPiPHrwdI/gAI43TmHJGsrWeGO6PiEreF7KN8UKA+I7YzOKnvXURlbMm3SuaFJMRbmtNGf6DE2CNa9r56Hvd0TWDUTFxWSinORuguLQG+LCL3o2al8LJJr/m14dJxlFlre9cZFXT0bg7B7No6nf/F1hCYj8OfhYgjUD85czBvr/9mzKmHIJulQF2E+F/e0x+vEzv0h77mamAT37ZrprHBqQeB0EErgJon9+4dsiuZNVeeh089p7WKmsPabhRYscvGQ/YG0ZzwB1syWQcMSc6+6TS",

    "skin": "noskin",
    "sp-cdn": "L5Z9:BG",
    "ubid-acbfr": "520-5201293-7803719",
    "ubid-main": "134-7786473-7014142"
}

data = request(url=URL, method='get', headers=HEADERS, cookies=COOKIES).text


soup = BeautifulSoup(data, 'html.parser')

whole_price_element = soup.select_one('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole')
whole_price_value = whole_price_element.text.strip(',')

price_fraction_value = soup.select_one('#corePriceDisplay_desktop_feature_div >'
                                       ' div.a-section.a-spacing-none.aok-align-center.aok-relative > '
                                       'span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay >'
                                       ' span:nth-child(2) > span.a-price-fraction').text

currency_symb = soup.select_one('#corePriceDisplay_desktop_feature_div > '
                                'div.a-section.a-spacing-none.aok-align-center.aok-relative >'
                                ' span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > '
                                'span:nth-child(2) > '
                                'span.a-price-symbol').text

total_price = float(f"{whole_price_value}.{price_fraction_value}")

product_title = soup.select_one('#productTitle').get_text().strip()

EMAIL = os.getenv("GMAIL_ADDRESS")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

if total_price < MIN_PRICE:

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()           # Secure the connection
        server.login(EMAIL, PASSWORD)

        subject = "Low Price Notification"
        body = f"{product_title} is currently on the price of {total_price}{currency_symb}!"

        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            from_addr=EMAIL,
            to_addrs="ivanjelev2004@gmail.com",
            msg=message.encode('utf8')
        )

    print('Successfully sent an email notification. Better start shopping!')