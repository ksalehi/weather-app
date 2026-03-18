from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from weather.client import get_current_weather, get_coordinates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
)

@app.get('/weather/{city}')
def get_weather(city: str):
    try:
        coords = get_coordinates(city)
    except ValueError as e:
       raise HTTPException(status_code=404, detail=str(e)) 

    return get_current_weather(coords)
