"""Asynchronous Python client library for the BBFC website."""

from bbfcapi.client import search
from bbfcapi.parser import parse_top_search_result
from bbfcapi.types import Film


async def top_search_result(title: str, year: int) -> Film:
    # TODO: Year optional?
    page = await search(title, year)
    return parse_top_search_result(page)
