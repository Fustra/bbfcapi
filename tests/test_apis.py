import os
import socket
import subprocess
from pathlib import Path

import pytest
import requests
import responses

from bbfcapi import apis
from bbfcapi.types import AgeRating, Film


@pytest.fixture(scope="class")
def app_url(fake_bbfc_url):
    """Start the actual web app in a separate process."""
    port = _free_port()
    url = f"http://127.0.0.1:{port}"
    with subprocess.Popen(
        ["uvicorn", "bbfcapi.app:app", "--port", str(port)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
        env={
            "PATH": os.environ["PATH"],
            "BBFC_URL": fake_bbfc_url,
            "PYTHONUNBUFFERED": "1",  # So readline() actually works
        },
    ) as proc:
        proc.stderr.readline()
        proc.stderr.readline()
        proc.stderr.readline()
        assert url in proc.stderr.readline()  # Sense check it's working
        yield url
        proc.terminate()


@pytest.fixture(scope="class")
def fake_bbfc_url():
    """Start a mock BBFC server that always returns the same response."""
    exe = str(Path(__file__).parent / "fake_bbfc.py")
    port = _free_port()
    filename = "search_interstellar.html"
    url = f"http://127.0.0.1:{port}"
    with subprocess.Popen(
        [exe, str(port), filename],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        text=True,
        env={
            "PATH": os.environ["PATH"],
            "PYTHONUNBUFFERED": "1",  # So readline() actually works
        },
    ) as proc:
        abc = proc.stdout.readline()
        assert "ONLINE-ISH" in abc
        actual = requests.get(url).content
        expected = (Path(__file__).parent / "data" / filename).read_bytes()
        assert actual == expected  # Sense check it's working
        yield url
        proc.terminate()


@pytest.fixture
def mock_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


def _free_port():
    """Return a port number that is free to be used."""
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def test_integration_healthz_okay(app_url):
    assert apis.healthz(base_url=app_url)


def test_integration_top_search_result(app_url):
    actual = apis.top_search_result("Interstellar", 2014, base_url=app_url)
    assert actual == Film(title="INTERSTELLAR", year=2014, age_rating=AgeRating.AGE_12)


def test_top_search_result_404_response_returns_no_film(mock_responses):
    mock_responses.add(
        responses.GET,
        apis.DEFAULT_BASE_URL,
        body="{}",
        status=404,
        content_type="application/json",
    )

    assert apis.top_search_result("interstellar", 2014) is None


def test_top_search_result_raises_request_exceptions(mock_responses):
    mock_responses.add(
        responses.GET,
        apis.DEFAULT_BASE_URL,
        body="{}",
        status=500,
        content_type="application/json",
    )

    with pytest.raises(requests.HTTPError) as err:
        apis.top_search_result("interstellar", 2014)

    assert err.value.response.status_code == 500


def test_healthz_500_error(mock_responses):
    mock_responses.add(
        responses.GET,
        f"{apis.DEFAULT_BASE_URL}/healthz",
        body="{}",
        status=500,
        content_type="application/json",
    )
    assert not apis.healthz()
