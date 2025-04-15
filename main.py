import requests
import os
from sendemail import send_email
from dotenv import load_dotenv

load_dotenv()

source = "techcrunch"

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/top-headlines?sources={source}&apiKey={api_key}&language=en"

request = requests.get(url)
content = request.json()

news = "Subject: Today's Tech News\n\n"

for article in content["articles"][:20]:
    if article["title"] is not None:
        news = news + article["title"].upper() + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n"

news = news.encode("utf-8")
send_email(message=news)
