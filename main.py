# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
API_KEY = "f500a7e58d36e1391083b33be63a4bc7"
lat=42.5
lon=0.00
from twilio.rest import Client
account_sid = "AC0b69f3b0bd0e50ffaf68650bee82b4d9"
auth_token = "014fd195dda91166c1d6cc628d2243df"

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
        from_='+16592745718',
        to='+917979011500'
    )
    print(message.status)
