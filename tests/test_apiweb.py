from starlette.testclient import TestClient

from bbfcapi.apiweb import app


def test_client():
    return TestClient(app)


def test_root_returns_http_200(mock_search_interstellar):
    response = test_client().get("/?title=interstellar&year=2014")
    assert response.status_code == 200
    assert response.json() == {
        "title": "INTERSTELLAR",
        "year": 2014,
        "age_rating": "12",
    }


def test_root_returns_cors_headers(mock_search_interstellar):
    # Client must sent Origin header in order for CORS to be considered
    response = test_client().get(
        "/?title=interstellar&year=2014", headers={"Origin": "null"}
    )
    assert response.status_code == 200
    assert response.headers.items() >= {"access-control-allow-origin": "*"}.items()


def test_healthz():
    response = test_client().get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
