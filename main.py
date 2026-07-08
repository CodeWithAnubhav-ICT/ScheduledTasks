# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
API_KEY = os.environ.get("API_KEY")
lat=42.5
lon=0.00

proxy = os.environ.get("proxy")
phone= os.environ.get("phone")
from twilio.rest import Client
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

import requests
response = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&cnt=4")
response.raise_for_status()
data = response.json()
Rain = False
for i in range (0,4):
    if data["list"][i]["weather"][0]["id"] < 700 :
        Rain = True

if Rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today ⛈, Make sure to bring an Umbrella☔",
        from_=proxy,
        to=phone
    )
    print(message.status)
