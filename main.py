import requests
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from twilio.rest import Client
import os

# https://www.alphavantage.co/documentation/

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": os.environ.get('STOCK_API_KEY')
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']

today = datetime.now().date()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))
yesterday_close = float(stock_data[yesterday]['4. close'])
day_before_yesterday_close = float(stock_data[day_before_yesterday]['4. close'])

close_diff = round(((yesterday_close - day_before_yesterday_close)/day_before_yesterday_close) * 100)

movement = "🔺" if close_diff > 0 else "🔻"
msg_content = f"{STOCK}: {movement}{abs(close_diff)}%\n\n"

# https://newsapi.org/docs/client-libraries/python
newsapi = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))
all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      from_param=yesterday,
                                      to=day_before_yesterday,
                                      language='en',
                                      sort_by='popularity',
                                      page=1)

articles = all_articles['articles']
for article in articles[:3]:
    msg_content += f"Headline: {article['title']}\nBriefing: {article['description']}\n\n"

# https://www.twilio.com/docs/sms/send-messages
client = Client(os.environ.get('ACCOUNT_SID'), os.environ.get('AUTH_TOKEN'))
message = client.messages \
    .create(
        body=msg_content,
        from_=os.environ.get('FROM_NUMBER'),
        to=os.environ.get('TO_NUMBER')
    )

print(message.sid)
