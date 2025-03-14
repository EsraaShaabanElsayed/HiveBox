""" This module contains tests for the Flask app's routes and endpoints.
It includes a test for the temperature endpoint."""

import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from main import app


class TestTemperatureRoute(unittest.TestCase):
    """Test case for the /temperature endpoint"""

    def test_temperature_route(self):
        """Test the temperature endpoint"""
        mock_data = {
            "sensors": [
                {
                    "title": "Temperatur",
                    "lastMeasurement": {
                        "createdAt": (
                            datetime.now(timezone.utc) - timedelta(minutes=30)
                        ).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                        "value": "0.03",
                    },
                }
            ]
        }
        with patch("main.fetch_sensebox_data", return_value=mock_data):
            response = app.test_client().get("/temperature")
            json_response = response.get_json()

            # Use unittest assertions
            self.assertEqual(
                json_response, {"average_temperature": 0.03, "status ": "Too Cold"}
            )
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
