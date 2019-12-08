import aiohttp
import pytest

from bbfcapi.client import search

pytestmark = pytest.mark.asyncio


async def test_search_is_mocked(data_search_interstellar, mock_aioresponses):
    with pytest.raises(aiohttp.client_exceptions.ClientConnectionError):
        await search(title="interstellar", year=2014)


async def test_search_ok(data_search_interstellar, mock_search_interstellar):
    result = await search(title="interstellar", year=2014)
    assert result == data_search_interstellar
