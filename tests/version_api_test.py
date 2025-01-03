from main import app
from main import VERSION_NUMBER


def test_version_route():
    response= app.test_client().get('/version')
    assert response.status_code==200
    assert VERSION_NUMBER.encode() in response.data