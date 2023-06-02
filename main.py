import requests
from datetime import date, timedelta
from twilio.rest import Client


stock = "Tesla"
# -----------------------------------Stock Price-------------------------------------------#
today = date.today()
yest = today - timedelta(days=1)
db_yest = today - timedelta(days=2)

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "LQQF5B7QRAYAPKPV"

}

stock_response = requests.get(url="https://www.alphavantage.co/query?", params=stock_parameters)
stock_response.raise_for_status()

yest_close = float(stock_response.json()["Time Series (Daily)"][f"{yest}"]["4. close"])
db_yest_close = float(stock_response.json()["Time Series (Daily)"][f"{db_yest}"]["4. close"])

difference = round(yest_close - db_yest_close, 2)
print(difference)

percentage = round((difference / db_yest_close) * 100, 2)
print(f"{percentage}%")

# ---------------------------------------------News-----------------------------------------------#


news_parameters = {
    "q": stock,
    "apiKey": "250b82e09d02495da8e45755ab10634e",
}

news_response = requests.get(url="https://newsapi.org/v2/everything?", params=news_parameters)
news_response.raise_for_status()
news_data_list = []
for i in range(0, 3):
    news_data = news_response.json()["articles"][i]["title"]
    news_data_list.append(news_data)
print(news_data_list)

# ----------------------------------------------SMS-------------------------------------------------#





# account_sid ="ACee9f9f6c39c9f2e87d0a3ce28bb965ea"

client = Client("ACee9f9f6c39c9f2e87d0a3ce28bb965ea", "68743d166d0729f406133d086e3ee578")

message = client.messages.create(
  body='Hi there',
  from_='+18647743890',
  to='+917025662944'
)

print(message.sid)
