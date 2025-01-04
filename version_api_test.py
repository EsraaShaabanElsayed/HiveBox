"""
This module contains tests for the Flask app's routes and endpoints.
It includes a test for the version endpoint.
"""
from main import VERSION_NUMBER, app

def test_version_route():
    """Function for test the version endpoint"""
    response = app.test_client().get("/version")
    if response.status_code != 200:
        raise ValueError(f"Expected status code 200, got {response.status_code}")

    if VERSION_NUMBER.encode() not in response.data:
        raise ValueError(f"Expected version number {VERSION_NUMBER} in response data")
    # assert response.status_code == 200
    # assert VERSION_NUMBER.encode() in response.data
