# pylint: disable=missing-module-docstring
from main import VERSION_NUMBER, app


def test_version_route():
    """Function for test the version endpoint"""
    response = app.test_client().get("/version")
    assert response.status_code == 200
    assert VERSION_NUMBER.encode() in response.data
