import os
from dotenv import load_dotenv
from datetime import datetime, timezone

from influxdb_client import Point, WritePrecision
from api.pyweather import WeatherManager
from api.store_data import StoreData

load_dotenv()

store = StoreData(os.getenv('INFLUX_HOST'), os.getenv('INFLUX_ORGANIZATION'), os.getenv('INFLUX_TOKEN'))
latitude = os.getenv('LATITUDE')
longitude = os.getenv('LONGITUDE')
bucket = os.getenv('INFLUX_BUCKET')


def get_current_weather():

    owm = WeatherManager(os.getenv('OWM_API_KEY'))
    weather = owm.get_weather(lat=latitude, lon=longitude)
    air = owm.get_air_pollution(lat=latitude, lon=longitude)

    date_current = datetime.fromtimestamp(weather['current']['dt'], tz=timezone.utc)
    date_current = date_current.strftime("%Y-%m-%dT%H:%M:%SZ")

    temperature = weather['current']['temp']
    pressure = weather['current']['pressure']
    humidity = weather['current']['humidity']
    uvi = weather['current']['uvi']
    clouds = weather['current']['clouds']
    wind_speed = weather['current']['wind_speed']

    date_sunrise = weather['current']['sunrise']
    date_sunset = weather['current']['sunset']

    date_sunrise = datetime.fromtimestamp(weather['current']['dt'], tz=timezone.utc)
    date_sunrise = date_sunrise.strftime("%Y-%m-%dT%H:%M:%SZ")

    date_sunset = datetime.fromtimestamp(weather['current']['dt'], tz=timezone.utc)
    date_sunset = date_sunset.strftime("%Y-%m-%dT%H:%M:%SZ")

    pm25 = 0
    pm10 = 0
    if air is not None:
        pm25 = air['list'][0]['components']['pm2_5']
        pm10 = air['list'][0]['components']['pm10']

    point = Point("weather") \
    .tag("type", "current") \
    .field("temperature", float(temperature)) \
    .field("pressure", float(pressure)) \
    .field("humidity", float(humidity)) \
    .field("uvi", float(uvi)) \
    .field("clouds", float(clouds)) \
    .field("wind_speed", float(wind_speed)) \
    .field("sunrise", date_sunrise) \
    .field("sunset", date_sunset) \
    .field("pm10", float(pm10)) \
    .field("pm25", float(pm25)) \
    .time(date_current, WritePrecision.NS)
              
    store.insert_data(bucket, point)
    return True

def empty_weather():
    store.delete_data(None, None, type_tag='current', measurement='weather', bucket=bucket)
    store.delete_data(None, None, type_tag='forecast', measurement='weather', bucket=bucket)
    return True

def get_forecast_weather():

    store.delete_data(None, None, type_tag='forecast', measurement='weather', bucket=bucket)
    owm = WeatherManager(os.getenv('OWM_API_KEY'))
    weather = owm.get_forecast_weather(lat=latitude, lon=longitude)

    for w in weather['daily']:
        date_current = datetime.fromtimestamp(w['dt'], tz=timezone.utc)
        date_current = date_current.strftime("%Y-%m-%dT%H:%M:%SZ")
        temperature = w['temp']['day']
        pressure = w['pressure']
        humidity = w['humidity']
        uvi = w['uvi']
        clouds = w['clouds']
        wind_speed = w['wind_speed']
        date_sunrise = datetime.fromtimestamp(w['sunrise'], tz=timezone.utc)
        date_sunrise = date_sunrise.strftime("%Y-%m-%dT%H:%M:%SZ")
        date_sunset = datetime.fromtimestamp(w['sunset'], tz=timezone.utc)
        date_sunset = date_sunset.strftime("%Y-%m-%dT%H:%M:%SZ")

        point = Point("weather") \
        .tag("type", "forecast") \
        .field("temperature", float(temperature)) \
        .field("pressure", float(pressure)) \
        .field("humidity", float(humidity)) \
        .field("uvi", float(uvi)) \
        .field("clouds", float(clouds)) \
        .field("wind_speed", float(wind_speed)) \
        .field("sunrise", date_sunrise) \
        .field("sunset", date_sunset) \
        .time(date_current, WritePrecision.NS)
                
        store.insert_data(bucket, point)

    return True
        
        