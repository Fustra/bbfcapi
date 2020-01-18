from bbfcapi.client import search
from bbfcapi.parser import top_search_result as parse_top_search_result
from bbfcapi.types import Film


async def top_search_result(title: str, year: int) -> Film:
    # TODO: Handle no films found for that year
    # TODO: Year optional?
    page = await search(title, year)
    return parse_top_search_result(page)
