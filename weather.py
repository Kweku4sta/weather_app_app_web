from pprint import pprint
from dotenv import load_dotenv
import os
import requests
load_dotenv()


def get_weather_conditions(city= "'Accra"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    pprint('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")
    if not bool(city.strip()):
        city = 'Accra'

    weather_data = get_weather_conditions(city)
    pprint("\n")
    pprint(weather_data)