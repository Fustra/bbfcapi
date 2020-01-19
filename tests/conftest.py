from pathlib import Path

import pytest
from aioresponses import aioresponses

from bbfcapi.client import search_url


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
def data_search_interstellar():
    return (Path(__file__) / "../data/search_interstellar.html").resolve().read_bytes()


@pytest.fixture
def data_search_12a():
    return (Path(__file__) / "../data/search_12a.html").resolve().read_bytes()


@pytest.fixture
def data_search_no_results():
    return (Path(__file__) / "../data/search_no_results.html").resolve().read_bytes()


@pytest.fixture
def mock_aioresponses():
    with aioresponses() as m:
        yield m


@pytest.fixture
def mock_search_interstellar(data_search_interstellar, mock_aioresponses):
    mock_aioresponses.get(
        search_url("interstellar", 2014), body=data_search_interstellar
    )


@pytest.fixture
def mock_search_no_results(data_search_no_results, mock_aioresponses):
    mock_aioresponses.get(search_url("no-film", 1900), body=data_search_no_results)
