import os
from flask import Flask, jsonify

from api.function import get_current_weather, empty_weather, get_forecast_weather
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


@app.route("/")
def welcome():
    # return a json
    return jsonify({"status": "api working"})


@app.route("/current-weather")
def current_weather():

    with app.app_context():

        if get_current_weather():
            return jsonify({"status": "Success retrieve data"})

        # return a json
        return jsonify({"status": "Error retrieve data"})


@app.route("/forecast-weather")
def forecast_weather():

    with app.app_context():

        if get_forecast_weather():
            return jsonify({"status": "Success retrieve data"})

        # return a json
        return jsonify({"status": "Error retrieve data"})


@app.route("/delete-weather")
def delete_weather():

    with app.app_context():

        if empty_weather():
            return jsonify({"status": "Success retrieve data"})

        # return a json
        return jsonify({"status": "Error retrieve data"})


scheduler = BackgroundScheduler()  # Scheduler object
scheduler.add_job(
    current_weather, "interval", minutes=int(os.getenv("FLASK_CURRENT_WEATHER_DELAY"))
)
scheduler.add_job(
    forecast_weather, "interval", minutes=int(os.getenv("FLASK_FORECAST_WEATHER_DELAY"))
)
scheduler.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("FLASK_PORT"))
