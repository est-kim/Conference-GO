import requests
import json
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": city + " " + state,
        "per_page": 1
    }
    url = "https://api.pexels.com/v1/search"
    response = requests.get(url, params=params, headers=headers)
    content = json.loads(response.content)
    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except:
        return {"picture_url": None}


def get_weather_data(city, state):
    params = {
        "q": f"{city}, {state}, US",
        "appid": OPEN_WEATHER_API_KEY,
        "limit": 1
    }
    url = "http://api.openweathermap.org/geo/1.0/direct"
    response = requests.get(url, params=params)
    content = json.loads(response.content)
    try:
        lat = content[0]["lat"]
        lon = content[0]["lon"]
    except (IndexError, KeyError):
        return "Invalid location name"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial"
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=params)
    content = json.loads(response.content)
    try:
        return {
                "temp": content["main"]["temp"],
                "description": content["weather"][0]["description"]
            }
    except (IndexError, KeyError):
        return "No data here"
