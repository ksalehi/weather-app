import typer
from weather.client import get_current_weather, get_coordinates

app = typer.Typer()

@app.command()
def weather(city: str):
    coords = get_coordinates(city)
    weather = get_current_weather(coords)

    print(f"The weather in {city} is {weather.description}")
    print(f"It is {weather.temperature}°F with {weather.humidity}% humidity")

if __name__ == "__main__": 
    app()