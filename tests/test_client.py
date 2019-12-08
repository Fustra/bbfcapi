import pytest

from bbfcapi.client import search, search_url

pytestmark = pytest.mark.asyncio


async def test_search_ok(data_search_interstellar, mock_aioresponses):
    mock_aioresponses.get(
        search_url("interstellar", 2014), body=data_search_interstellar
    )
    result = await search(title="interstellar", year=2014)
    assert result == data_search_interstellar
