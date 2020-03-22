"""Asynchronous low-level network client for the BBFC website.

You probably want lib.py.
"""
import logging
import os

import aiohttp

logger = logging.getLogger(__name__)


DEFAULT_BASE_URL = "https://bbfc.co.uk"

SEARCH_URL = "{base_url}/search/releases/{title}/any/any/any/any/0/any/any/any/any/{year}/any/any?advanced=true"


async def search(title: str, year: int) -> bytes:
    url = search_url(title, year)
    logger.debug("Request to '%s'", url)
    async with aiohttp.ClientSession(
        raise_for_status=True, timeout=aiohttp.ClientTimeout(total=10)
    ) as session:
        async with session.get(url) as response:
            return await response.read()


def search_url(title: str, year: int) -> str:
    base_url = os.environ.get("BBFC_URL", DEFAULT_BASE_URL)
    return SEARCH_URL.format(base_url=base_url, title=title, year=year)
