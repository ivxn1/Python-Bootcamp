import requests
from twilio.rest import Client

# -------------------- NEWS FETCHING -------------------- #
def get_news():
    # Fetch the latest Tesla-related news articles using the News API
    # API query parameters:
    #   - q=Tesla (search keyword)
    #   - from=2025-08-18 (date filter for recent news)
    #   - sortBy=popularity (order results by popularity)
    #   - apiKey=... (authentication key)
    news_response = requests.get(url='https://newsapi.org/v2/everything?'
                                     'q=Tesla&'
                                     'from=2025-08-18&'
                                     'sortBy=popularity&'
                                     'apiKey=')

    # Parse the JSON response from the API
    news_data = news_response.json()

    # Select the top 3 news articles from the API response
    articles = news_data[:3]
    return articles


# -------------------- SMS SENDING -------------------- #
def send_message(articles):
    # Builds and sends a stock alert SMS using Twilio.
    # Includes Tesla stock movement (with % change) and top news headlines.
    global complete_message, stock_msg

    # Format stock message with arrow indicators depending on change
    if percent_change >= 5:
        stock_msg = f"{STOCK} 🔺{percent_change:.1f}%\n"
    elif percent_change <= -5:
        stock_msg = f"{STOCK} 🔻{percent_change:.1f}%\n"

    complete_message += stock_msg

    # Twilio API credentials (used for authentication)
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    # Loop through 3 articles and send separate SMS messages
    for i in range(3):
        complete_message += f"Heading: {articles[i]["title"]}"
        message = client.messages.create(
            from_='+',   # Twilio number
            to='+',     # Recipient number
            body=complete_message   # Message body text
        )
        # Reset message to only the stock alert before next article is added
        complete_message = stock_msg
        print(message.body)


# -------------------- GLOBAL SETTINGS -------------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
complete_message = ''   # Holds the combined stock + news message
stock_msg = ''          # Holds only the stock movement message


# -------------------- STOCK DATA FETCHING -------------------- #
stocks_api_key = ""

# API parameters for Alpha Vantage stock data
stocks_params = {
    "function": "TIME_SERIES_DAILY",  # Daily stock prices
    "symbol": STOCK,                  # Target stock ticker
    "apikey": stocks_api_key
}

# Call the stock API and parse the response
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stocks_params)
stock_data = stock_response.json()["Time Series (Daily)"]

# Extract stock closing prices for yesterday and the day before
days_stocks = [value for (key, value) in stock_data.items()]
yesterday_close = 100               # float(days_stocks[0]['4. close'])  <- test value
day_before_yest_close = 200         # float(days_stocks[1]['4. close'])  <- test value

# Calculate percentage change between two days
percent_change = ((yesterday_close - day_before_yest_close) / day_before_yest_close) * 100


# -------------------- MAIN LOGIC -------------------- #
# If the stock movement exceeds ±5%, fetch the latest news and send SMS alerts
if abs(percent_change) >= 5:
    articles_list = get_news()
    send_message(articles_list)