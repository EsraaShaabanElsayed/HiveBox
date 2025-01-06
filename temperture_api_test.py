"""
This module contains tests for the Flask app's routes and endpoints.
It includes a test for the temperature endpoint.
"""

import os
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from main import app


class TestTemperatureRoute(unittest.TestCase):
    """Test case for the /temperature endpoint"""

    @patch.dict(
        os.environ,
        {
           "SENSOR_IDS": '["5eba5fbad46fb8001b799786", "5e60cf5557703e001bdae7f8", "5eb99cacd46fb8001b2ce04c"]'
        },
    )
    def test_temperature_route(self):
        """Test the temperature endpoint"""
        #current_time = datetime.now(timezone.utc).isoformat()
        mock_data = {
            "sensors": [
                {
                    "title": "Temperatur",
                    "lastMeasurement": {
                        "createdAt": (datetime.now(timezone.utc) - timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
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


# # pylint: disable=import-error
# """
# This module contains tests for the Flask app's routes and endpoints.
# It includes a test for the temperature endpoint.
# """
# import os
# import sys
# from unittest.mock import patch

# from main import app

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# def test_temperature_route():
#     """Function for test the  temperature endpoint"""
#     mock_data = {
#         "sensors": [
#             {
#                 "title": "Temperatur",
#                 "lastMeasurement": {
#                     "createdAt": "2025-01-03T22:11:35.066Z",
#                     "value": "0.03",
#                 },
#             }
#         ]
#     }
#     with patch("main.fetch_sensebox_data", return_value=mock_data):
#         response = app.test_client().get("/temperature")
#         json_response = response.get_json()
#         assert json_response == {"average_temperature": 0.03}
#         assert response.status_code == 200
