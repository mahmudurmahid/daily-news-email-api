import requests
import os
from sendemail import send_email
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

request = requests.get(url)
content = request.json()

news = ""

for article in content["articles"]:
    if article["title"] is not None:
        news = news + article["title"].upper() + "\n" + str(article["description"]) + 2*"\n"

news = news.encode("utf-8")
send_email(message=news)