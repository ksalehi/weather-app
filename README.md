# Weather App

A weather lookup app with a CLI, REST API, and React frontend. Built with Python and TypeScript.

## Stack

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) — REST API
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [httpx](https://www.python-httpx.org/) — HTTP client
- [Typer](https://typer.tiangolo.com/) — CLI
- [uv](https://docs.astral.sh/uv/) — package management

**Frontend**
- [React](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vitejs.dev/)

**Data**
- [Open-Meteo](https://open-meteo.com/) — free weather API, no key required

## Getting started

### Prerequisites

- Python 3.12+
- Node 18+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Backend

```bash
uv pip install -e .
```

Start the API server:

```bash
uv run fastapi dev weather/api.py
```

Or use the CLI:

```bash
uv run weather London
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Then visit `http://localhost:5173`. The API must also be running.

## API

```
GET /weather/{city}
```

Example response:

```json
{
  "city": "London",
  "temperature": 10.9,
  "humidity": 67,
  "precipitation": 0.0,
  "weather_code": 3,
  "description": "☁️ Overcast"
}
```

Interactive docs available at `http://localhost:8000/docs` when the server is running.
