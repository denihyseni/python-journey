import os
import requests
import smtplib
from datetime import datetime, timedelta

MY_EMAIL = "deni.hyseni@gmail.com"
PASSWORD = "ouzevaeyxzrqcpse"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

# Dates
today = datetime.today()
yesterday = today - timedelta(days=1)
day_before = today - timedelta(days=2)
yesterday_str = yesterday.strftime('%Y-%m-%d')
day_before_str = day_before.strftime('%Y-%m-%d')

# Stock data
stock_url = (
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
    f"&symbol={STOCK}&apikey={stock_api_key}"
)
stock_data = requests.get(stock_url).json()["Time Series (Daily)"]
y_price = float(stock_data[yesterday_str]["1. open"])
dby_price = float(stock_data[day_before_str]["1. open"])
percent_diff = abs((y_price - dby_price) / dby_price * 100)

# News data
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={news_api_key}"
articles = requests.get(news_url).json()["articles"][:3]
news_briefs = "\n\n".join(
    f"Headline: {a['title']} Brief: {a['description']}" for a in articles
)

# Message
if percent_diff >= 5:
    message = f"{STOCK}: {percent_diff:.2f}%\n\n{news_briefs}"
elif percent_diff <= -5:
    message = f"{STOCK}: {percent_diff:.2f}%\n\n{news_briefs}"
else:
    message = f"{STOCK}: {percent_diff:.2f}%\n\nNo massive changes"

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:STOCK NEWS\n\n{message}"
    )

# print(f"Most recent news about {COMPANY_NAME}: {first_news}\n"
#         f"Older news about {COMPANY_NAME}:{second_news}\n"
#         f"Oldest piece of news about {COMPANY_NAME}:{third_news}")

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

