"""Asynchronous low-level network client for the BBFC website.

You probably want lib.py.
"""
import logging

import aiohttp

from bbfcapi.urls import search_url

logger = logging.getLogger(__name__)


async def search(title: str, year: int) -> bytes:
    url = search_url(title, year)
    logger.debug("Request to '%s'", url)
    async with aiohttp.ClientSession(
        raise_for_status=True, timeout=aiohttp.ClientTimeout(total=10)
    ) as session:
        async with session.get(url) as response:
            return await response.read()
