from unittest.mock import patch
from main import app



def test_temperature_route():
    mock_data ={"sensors": [
         {
            "title": "Temperatur",
           
            "lastMeasurement": {
                "createdAt": "2025-01-03T22:11:35.066Z",
                "value": "0.03"
            }
         }
    ]
    }
    with patch('main.fetch_sensebox_data', return_value=mock_data):
        response= app.test_client().get("/temperature")
        json_response=response.get_json()
        assert json_response =={"average_temperature": 0.03}
        assert response.status_code==200

