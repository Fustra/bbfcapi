"""Parser for BBFC webpages."""
from typing import Optional

from bs4 import BeautifulSoup

from bbfcapi.types import AgeRating, Film


def top_search_result(content: bytes) -> Optional[Film]:
    soup = BeautifulSoup(content, "html.parser")
    return Film(
        title=soup.select_one("h3.title > a").string.strip(),
        year=int(
            soup.select_one("span.title-additional-info").string.strip().strip("()")
        ),
        age_rating=AgeRating(
            soup.select_one("p.symbol img")
            .attrs["src"]
            .partition("BBFC%20")[2]
            .partition("_")[0]
        ),
    )
