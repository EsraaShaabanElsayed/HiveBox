# pylint: disable=redefined-outer-name
""" This module contains  integration testing for the Flask app"""

import pytest
from flask.testing import FlaskClient

from main import VERSION_NUMBER, app


@pytest.fixture
def test_client():
    """Fixture to set up the test client for Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_version_endpoint(test_client: FlaskClient):
    """Test the version endpoint."""
    response = test_client.get("/version")
    if response.status_code != 200:
        raise AssertionError(f"Expected status code 200, got {response.status_code}")
    data = response.get_json()
    if "version" not in data:
        raise KeyError("Missing 'version' key in response data")
    if data["version"] != VERSION_NUMBER:
        raise AssertionError(
            f"Expected version '{VERSION_NUMBER}', got '{data['version']}'"
        )


def test_temperature_endpoint(test_client: FlaskClient):
    """
    Test the /temperature endpoint with real sensor data."""
    response = test_client.get("/temperature")
    if response.status_code != 200:
        raise AssertionError(f"Expected status code 200, got {response.status_code}")

    data = response.get_json()
    if "average_temperature" not in data:
        raise KeyError("Missing 'average_temperature' key in response data")
    if "status " not in data:
        raise KeyError("Missing 'status ' key in response data")
    if not isinstance(data["average_temperature"], (int, float)):
        raise TypeError("Expected 'average_temperature' to be a number")
    if data["status "] not in ["Too Cold", "Good", "Too Hot"]:
        raise ValueError(
            f"Unexpected 'status ': {data['status ']}. Expected 'Too Cold', 'Good', or 'Too Hot'"
        )
