# OpenWeather-grafana-influxdb

Fetch weather data for latitude and longitude and store into InfluxDB database and show graph on Grafana.


# Result

![Dashboard Grafana](https://raw.githubusercontent.com/ophusdev/openweather-grafana-influxdb/master/dashboard.png)



# Install
1. Clone this repository
2. Copy .env.example into .env
3. Populate .env file with correct values
4. Run `docker-compose up`

# Example Configuration
    INFLUX_TOKEN=J3LzDXzoGw1n6BfglWbn
    INFLUX_ORGANIZATION=Contoso
    INFLUX_BUCKET=buchet_test
    INFLUX_HOST=http://influxdb:8086

    LATITUDE=41.8856733
    LONGITUDE=12.482275
    OWM_API_KEY=lgspvzk7sys1d7zxjijh

    FLASK_PORT=5000
    FLASK_DEBUG=1
    FLASK_CURRENT_WEATHER_DELAY=5
    FLASK_FORECAST_WEATHER_DELAY=30

# OpenWeather Map
Create new account on OpenWeather Map and generate a free Api key from [page](https://openweathermap.org/appid) and insert generated api key into .env file

Into .env change the latitude and longitude according to you location

# InfluxDB
After start docker containers go to http://influxdb:8086 and initialize InfluxDB.

Generate [token](https://docs.influxdata.com/influxdb/cloud/security/tokens/create-token/) and insert into .env file

# Grafana
Visit http://grafana:3000 and create new [Datasource](https://www.influxdata.com/blog/how-grafana-dashboard-influxdb-flux-influxql/) from InfluxDB

# Conclusion

Run `docker-compose down`.

Check if all variables into .env file are corrects.

Run again `docker-compose up`.

If you visit http://localhost:5000 a message like `api working` should me show