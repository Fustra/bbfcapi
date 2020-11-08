import aiohttp
import pytest

from bbfcapi.client_async import search

pytestmark = pytest.mark.asyncio


async def test_search_is_mocked(search_interstellar_json, mock_aioresponses):
    with pytest.raises(aiohttp.client_exceptions.ClientConnectionError):
        await search(title="interstellar")


async def test_search_ok(search_interstellar_json, mock_search_interstellar):
    result = await search(title="interstellar")
    assert result == search_interstellar_json
