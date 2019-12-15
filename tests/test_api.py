import pytest
from starlette.testclient import TestClient

from bbfcapi.api import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_with_interstellar(client, mock_search_interstellar):
    response = client.get("/?title=interstellar&year=2014")
    assert response.status_code == 200
    assert response.json() == {
        "title": "INTERSTELLAR",
        "year": 2014,
        "age_rating": "12",
    }


def test_root_returns_cors_headers(client, mock_search_interstellar):
    # Client must sent Origin header in order for CORS to be considered
    response = client.get("/?title=interstellar&year=2014", headers={"Origin": "null"})
    assert response.status_code == 200
    assert response.headers.items() >= {"access-control-allow-origin": "*"}.items()


def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
