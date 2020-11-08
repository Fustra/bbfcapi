import json
from pathlib import Path

import pytest
from aioresponses import aioresponses

from bbfcapi.client_common import graphql_url


def pytest_addoption(parser):
    parser.addoption(
        "--run-live",
        action="store_true",
        default=False,
        help="run live integration tests",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-live"):
        return

    skip_live = pytest.mark.skip(reason="need --run-live option to run")
    for item in items:
        if "live" in item.keywords:
            item.add_marker(skip_live)


@pytest.fixture
def search_a_silent_voice_json():
    return json.loads(
        (Path(__file__) / "../data/search_a_silent_voice.json").resolve().read_text()
    )


@pytest.fixture
def search_interstellar_json():
    return json.loads(
        (Path(__file__) / "../data/search_interstellar.json").resolve().read_text()
    )


@pytest.fixture
def search_no_film_json():
    return json.loads(
        (Path(__file__) / "../data/search_no_film.json").resolve().read_text()
    )


@pytest.fixture
def mock_aioresponses():
    with aioresponses() as m:
        yield m


@pytest.fixture
def mock_search_interstellar(search_interstellar_json, mock_aioresponses):
    mock_aioresponses.post(graphql_url, payload=search_interstellar_json)


@pytest.fixture
def mock_search_no_film(search_no_film_json, mock_aioresponses):
    mock_aioresponses.post(graphql_url, payload=search_no_film_json)
