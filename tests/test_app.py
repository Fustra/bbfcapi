from starlette.testclient import TestClient

from bbfcapi.app import app


def test_client():
    return TestClient(app)


def test_root_returns_http_200_with_a_result(mock_search_interstellar):
    response = test_client().get("/?title=interstellar")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Interstellar",
        "ageRating": "12",
    }


def test_root_returns_http_204_with_no_results(mock_search_no_film):
    response = test_client().get("/?title=no-film&year=1900")
    assert response.status_code == 404
    assert response.json() == {"detail": "Film not found"}


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
