import httpx

from .models import Coordinates, CurrentWeather

GEOCODING_API = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city: str) -> Coordinates:
    response = httpx.get(GEOCODING_API, params={'name': city, 'count': 1})

    data = response.json()
    if data.get("results"):
        result = data["results"][0]
        return Coordinates(
            latitude=result["latitude"],
            longitude=result["longitude"],
            city=result["name"]
        )
    raise ValueError("City not found")

def get_current_weather(coords: Coordinates) -> CurrentWeather:
    response = httpx.get(WEATHER_API, params={
        "latitude": coords.latitude, 
        "longitude": coords.longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m", 
            "precipitation", 
            "weather_code"
        ],
        "wind_speed_unit": "mph",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch",
    })

    data = response.json()
    if "current" not in data:
        raise ValueError('There was an issue fetching the weather, please try again later.')

    current = data["current"]

    return CurrentWeather(
            temperature=current['temperature_2m'],
            humidity=current['relative_humidity_2m'],
            precipitation=current['precipitation'],
            weather_code=current['weather_code'],
            city=coords.city
        )