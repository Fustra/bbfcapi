from pathlib import Path

import pytest
from aioresponses import aioresponses


@pytest.fixture
def data_search_interstellar():
    return (Path(__file__) / "../data/search_interstellar.html").resolve().read_bytes()


@pytest.fixture
def mock_aioresponses():
    with aioresponses() as m:
        yield m
