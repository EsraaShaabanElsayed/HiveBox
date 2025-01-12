"""Module providing 3 end points to return the version of the app and the avg temperature and
prometheus metrics about the app """

import json
import os
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

load_dotenv()
app = Flask(__name__)
metrics = PrometheusMetrics(app)

VERSION_NUMBER = "v2.4.8"


def load_sensor_ids():
    """This Function for retrieving the sensor ids from env"""
    sensor_ids_env = os.getenv("SENSOR_IDS")

    if sensor_ids_env:
        try:
            # If SENSOR_IDS is set as an environment variable, parse it
            sensor_ids = json.loads(sensor_ids_env)
            if not isinstance(sensor_ids, list):
                raise ValueError("SENSOR_IDS should be a list.")
            return sensor_ids
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Invalid SENSOR_IDS format: {e}")
            return []

    print("SENSOR_IDS environment variable not set.")
    return []


sensors_ids = load_sensor_ids()


@app.route("/version")
def version_fun():
    """Function to  return the app version"""
    return jsonify({"version": VERSION_NUMBER})


def fetch_sensebox_data(sensebox_id):
    """Function to fetch data from the openSenseMap API"""
    url = f"https://api.opensensemap.org/boxes/{sensebox_id}"
    try:
        response = requests.get(url, timeout=2000)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return None


def temp_status(avg_tmp):
    """function to evaluate the temp status"""
    if avg_tmp < 10:
        status = "Too Cold"
    elif 11 < avg_tmp < 36:
        status = "Good"
    else:
        status = "Too Hot"
    return status


@app.route("/temperature", methods=["GET"])
def get_average_temperature():
    """This function to return the avg temperature based on 3 boxes"""
    total_temp = 0
    total_boxes = 0
    hour_ago = datetime.now(timezone.utc) - timedelta(hours=1)

    for sensor_id in sensors_ids:
        data = fetch_sensebox_data(sensor_id)
        if not data:
            continue
        sensors = data.get("sensors", [])
        for sensor in sensors:
            if sensor["title"].lower() == "temperatur":
                last_measurement = sensor.get("lastMeasurement", {})
                measurement_time = last_measurement.get("createdAt")
                value = last_measurement.get("value")
                if measurement_time and value:
                    measurement_time = datetime.strptime(
                        measurement_time, "%Y-%m-%dT%H:%M:%S.%fZ"
                    ).replace(tzinfo=timezone.utc)
                    if measurement_time >= hour_ago:
                        total_boxes += 1
                        total_temp += float(value)
    if total_boxes == 0:
        return jsonify({"error": "there is no new data from 1 hour"}), 404
    avg_tmp = total_temp / total_boxes

    return jsonify({"average_temperature": avg_tmp, "status ": temp_status(avg_tmp)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
