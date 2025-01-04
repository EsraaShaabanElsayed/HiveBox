"""Module providing 2 end points to return the version of the app and the avg temperature."""

from datetime import datetime, timedelta, timezone

import requests
from flask import Flask, jsonify

app = Flask(__name__)

VERSION_NUMBER = "v1.3.7"
sensors_ids = [
    "5eba5fbad46fb8001b799786",
    "5e60cf5557703e001bdae7f8",
    "5eb99cacd46fb8001b2ce04c",
]


@app.route("/version")
def version_fun():
    """Function to  return the app version"""
    return jsonify(VERSION_NUMBER)


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
        return jsonify("error,there is no new data from 1 hour "), 404
    avg_tmp = total_temp / total_boxes
    return jsonify({"average_temperature": avg_tmp})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
