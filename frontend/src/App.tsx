import './index.css'
import { useState } from 'react'

type Weather = {
  temperature: number
  description: string 
  weather_code: number
  precipitation: number
  humidity: number
  city: string
}

function App() {
  const [weather, setWeather] = useState<Weather | null>(null)
  const [city, setCity] = useState<string>('')
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [error, setError] = useState<string | null>(null)

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    
    if (isLoading || city.trim() === '') {
      return
    }
    setIsLoading(true)
    setError(null)

    try {
      const formData = new FormData(event.currentTarget)
      const city = formData.get('city') as string
      setCity('')
      setWeather(null)

      const response = await fetch(`http://localhost:8000/weather/${city}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      
      if (response.status === 404) {
        setWeather(null)
        setError(`Sorry, we couldn't find a city by that name. Please check your spelling and try again.`)
        return
      }

      if (response.status !== 200) {
        setWeather(null)
        setError(`Error: Weather API returned ${response.status} ${response.statusText}`)
        return
      }

      const weatherData = await response.json()
      setWeather(weatherData)
    } catch (err) {
      console.error(err)
      setWeather(null)
      setError('Sorry, there was an error fetching the weather data. Please try again later.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="content">
      <h1>Weather App</h1>
      <form onSubmit={handleSubmit}>
        <input 
          className="city-input"
          id="city" 
          name="city" 
          type="text" 
          placeholder="Enter city name or zip code" 
          value={city} 
          onChange={(e) => setCity(e.target.value)}
        />
        <button 
          type="submit" 
          disabled={isLoading}
          className="submit-button"
        >
            Get Weather
          </button>
      </form>

      {isLoading && (
          <span className="spinner" aria-hidden="true" />
      )}
      {error && <p className="error">{error}</p>}

      {weather && (
        <>
          <h2>{weather.city}</h2>
          <p>{weather.description}, {weather.temperature}°F with {weather.humidity}% humidity</p>
        </>
      )}
    </div>
  )
}

export default App
