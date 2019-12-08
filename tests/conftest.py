from pathlib import Path

import pytest
from aioresponses import aioresponses

from bbfcapi.client import search_url


@pytest.fixture
def data_search_interstellar():
    return (Path(__file__) / "../data/search_interstellar.html").resolve().read_bytes()


@pytest.fixture
def mock_aioresponses():
    with aioresponses() as m:
        yield m


@pytest.fixture
def mock_search_interstellar(data_search_interstellar, mock_aioresponses):
    mock_aioresponses.get(
        search_url("interstellar", 2014), body=data_search_interstellar
    )
