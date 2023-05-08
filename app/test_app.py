import pytest

from run import app as application


@pytest.fixture()
def app():
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture
def client(app):   
    return app.test_client()


def test_api(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask" in response.data
