import requests

class WeatherFetcher:

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def fetch_rain_data(self, lat: float, lon: float):
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "precipitation",
            "past_days": 1,
            "forecast_days": 1
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code}")

        data = response.json()

        return data["hourly"]["precipitation"]
