"""Asynchronous low-level network client for the BBFC website.

You probably want lib.py.
"""
import logging
from typing import Any, Dict

import aiohttp

from bbfcapi.client_common import build_search_request, graphql_url

logger = logging.getLogger(__name__)


async def search(title: str) -> Dict[str, Any]:
    async with aiohttp.ClientSession(
        raise_for_status=True, timeout=aiohttp.ClientTimeout(total=10)
    ) as session:
        request_dict = build_search_request(title)
        async with session.post(graphql_url, json=request_dict) as response:
            return await response.json()
