import requests
from datetime import datetime
import smtplib
from time import time, sleep

MY_LAT = 50.361805
MY_LONG = 30.465835
MY_EMAIL = 'yartemtest@gmail.com'
PASSWORD = 'youdontneedit;'
RECIPIENT = 'yartemtest@yahoo.com'


def is_iss_overhead(user_lat, user_long, iss_lat, iss_long):
    if (iss_lat - 5) <= user_lat <= (iss_lat + 5) and (iss_long - 5) <= user_long <= (iss_long + 5):
        return True
    else:
        return False


def is_dark(sunrise_time, sunset_time):
    now_time = datetime.now().utcnow().hour
    if sunrise_time <= now_time <= sunset_time:
        return False
    else:
        return True


while True:
    sleep(60 - time() % 60)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    is_iss_visible = is_iss_overhead(MY_LAT, MY_LONG, iss_latitude, iss_longitude)
    is_dark_now = is_dark(sunrise, sunset)

    if is_iss_visible and is_dark_now:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT,
                                msg='Hey, look! Its dark and ISS is somewhere close!')
            connection.close()
            print('email sent')
    else:
        print(f'Requirements were not meet, email not sent! is_dark: {is_dark_now}\niss_visible: {is_iss_visible}')


