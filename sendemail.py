import smtplib, ssl
import os
from dotenv import load_dotenv

def send_email(message):
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("RECEIVER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        