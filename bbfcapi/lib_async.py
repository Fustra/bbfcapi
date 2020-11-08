"""Asynchronous Python client library for the BBFC website."""

from bbfcapi.client_async import search
from bbfcapi.parser import best_autocomplete_match
from bbfcapi.types import Film


async def best_match(title: str) -> Film:
    response_json = await search(title)
    return best_autocomplete_match(response_json, title)
