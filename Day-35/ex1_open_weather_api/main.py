import requests
import os
from dotenv import load_dotenv
load_dotenv()


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("API_KEY")
lat = os.environ.get("LAT")
lon = os.environ.get("LON")

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
if int(weather_data["weather"][0]["id"]) < 700:
    will_rain = True

if will_rain:
    print("Bring an umbrella.")
