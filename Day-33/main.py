import smtplib
import requests
from datetime import datetime
import time

MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "my_password"
MY_LAT = 51.507351
MY_LONG = -0.127758

# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # if response.status_code != 200:
    #     raise Exception("Bad response from ISS API")
    # if response.status_code == 404:
    #     raise Exception("That resource does not exist.")
    # else:
    #     raise Exception("You are not authorised to access this data.")
    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    print(iss_position)

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    # if is_iss_overhead() and is_night():
    #     connection = smtplib.SMTP("smtp.gmail.com")
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=MY_EMAIL,
    #         msg="Subject:Look Up \n\nThe ISS is above you in the sky."
    #     )
