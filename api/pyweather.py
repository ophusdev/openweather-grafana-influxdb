import requests
import json
from datetime import datetime
from api.url import BASE_URL, ONECALL_URL, AIRPOLLUTION_URL


class WeatherManager:
    def __init__(self, api_key):
        assert isinstance(api_key, str), "You must provide a valid API Key"
        self.api_key = api_key

    def get_weather(self, lat, lon):
        payload = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        r = requests.get(BASE_URL + ONECALL_URL, params=payload)

        if r.status_code != 200:
            raise Exception("Data not fetch {}".format(r))

        return r.json()

    def get_air_pollution(self, lat, lon):
        payload = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        r = requests.get(BASE_URL + AIRPOLLUTION_URL, params=payload)

        if r.status_code != 200:
            raise Exception("Air pollution Data not fetch")

        return r.json()

    def get_forecast_weather(self, lat, lon):
        payload = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
            "exclude": "hourly,minutely",
        }
        r = requests.get(BASE_URL + ONECALL_URL, params=payload)

        if r.status_code != 200:
            raise Exception("Data not fetch {}".format(r))

        return r.json()
