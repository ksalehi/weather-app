from pydantic import BaseModel, computed_field

class Coordinates(BaseModel):
    latitude: float
    longitude: float
    city: str

class CurrentWeather(BaseModel):
    temperature: float
    humidity: float
    precipitation: float
    weather_code: int
    city: str

    @computed_field
    def description(self) -> str:
        weather_descriptions = {
            0: "☀️ Clear sky",
            1: "🌤️ Mainly clear",
            2: "⛅ Partly cloudy",
            3: "☁️ Overcast",
            45: "🌫️ Foggy",
            48: "🌫️ Icy fog",
            51: "🌦️ Light drizzle",
            53: "🌦️ Moderate drizzle",
            55: "🌧️ Dense drizzle",
            61: "🌧️ Slight rain",
            63: "🌧️ Moderate rain",
            65: "⛈️ Heavy rain",
            71: "🌨️ Slight snow",
            73: "❄️ Moderate snow",
            75: "❄️ Heavy snow",
            80: "🌦️ Slight showers",
            81: "🌧️ Moderate showers",
            82: "⛈️ Violent showers",
            95: "⛈️ Thunderstorm",
        }
        return weather_descriptions.get(self.weather_code, "🌡️ Unknown weather code")