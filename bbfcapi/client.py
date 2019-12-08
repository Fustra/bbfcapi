"""Async client for BBFC website."""
import logging

import aiohttp

logger = logging.getLogger(__name__)

SEARCH_URL = "https://bbfc.co.uk/search/releases/{title}/any/any/any/any/0/any/any/any/any/{year}/any/any?advanced=true"


async def search(title: str, year: int) -> bytes:
    url = search_url(title, year)
    logger.debug("Request to '%s'", url)
    async with aiohttp.ClientSession(
        raise_for_status=True, timeout=aiohttp.ClientTimeout(total=10)
    ) as session:
        async with session.get(url) as response:
            return await response.read()


def search_url(title: str, year: int) -> str:
    return SEARCH_URL.format(title=title, year=year)
