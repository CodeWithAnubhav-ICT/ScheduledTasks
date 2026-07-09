# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import requests
from twilio.rest import Client

# 1. Fetch environment variables
API_KEY = os.environ.get("API_KEY")
PROXY = os.environ.get("PROXY")
PHONE = os.environ.get("PHONE")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

# Quick debug check: This will print a helpful error in your GitHub logs if a secret is missing
if not ACCOUNT_SID or not AUTH_TOKEN:
    raise ValueError("CRITICAL ERROR: Twilio ACCOUNT_SID or AUTH_TOKEN is missing from environment variables!")

lat = 29.7500
lon = 77.7166

# 2. Fetch Weather Data
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&cnt=4"
response = requests.get(url)
response.raise_for_status()
data = response.json()

# 3. Check for Rain
Rain = False
for item in data["list"][:4]:  # Cleaner and safer loop approach
    if item["weather"][0]["id"] < 700:
        Rain = True
        break

# 4. Set the message text based on the weather
if Rain:
    sms_body = "It is going to rain today ⛈, Make sure to bring an Umbrella☔"
else:
    sms_body = "Weather is all clear today, Have fun!!!"

# 5. Initialize client once and send the message
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    body=sms_body,
    from_=PROXY,
    to=PHONE
)

print(f"Message sent successfully! Status: {message.status}")

