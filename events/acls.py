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


def get_coordinates(lat, lon):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&limit=3&appid={OPEN_WEATHER_API_KEY}"
    response = requests.get(url)
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]
    return {
        "lat": lat,
        "lon": lon
    }


def get_weather_data(city, state):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&limit=3&appid={OPEN_WEATHER_API_KEY}"
    response = requests.get(url)
    return
