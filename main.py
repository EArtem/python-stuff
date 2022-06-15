import requests
from twilio.rest import Client
from datetime import date
import calendar


API_KEY = 'OPEN_WEATHER_MAP_API_KEY'
SERVER = 'https://api.openweathermap.org/data/2.5/onecall'
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'

month = calendar.month_abbr[date.today().month]
day = date.today().day


parameters = {
    'lat': 50.450001,
    'lon': 30.523333,
    'exclude': 'current,minutely,daily,alerts',
    'units': 'metric',
    'appid': API_KEY
}

response = requests.get(SERVER, params=parameters)
response.raise_for_status()
weather_data = response.json()
person_work_hours = weather_data['hourly'][:11]

hourly_weather_status_codes = []
for hourly_weather in weather_data['hourly'][:12]:
    hourly_weather_status_codes.append(hourly_weather['weather'][0]['id'])
print(hourly_weather_status_codes)

if any(status_code > 700 for status_code in hourly_weather_status_codes):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to='whatsapp:receiver',
        body=f'Today is {month}, {day} and its gonna be rain in Kyiv, take an ☔️'
    )
    print(message.status)
