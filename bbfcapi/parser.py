"""HTML Parser for the BBFC web-pages."""
from typing import Optional

from bs4 import BeautifulSoup

from bbfcapi.types import AgeRating, Film


def parse_top_search_result(content: bytes) -> Optional[Film]:
    soup = BeautifulSoup(content, "html.parser")

    film_title = soup.select_one("h3.title > a")
    if film_title is None:
        return None

    return Film(
        title=film_title.string.strip(),
        year=int(
            soup.select_one("span.title-additional-info").string.strip().strip("()")
        ),
        age_rating=AgeRating(
            soup.select_one("p.symbol img")
            .attrs["src"]
            .partition("BBFC%20")[2]
            .partition("_")[0]
            .rstrip("A")  # Remove suffix from "12A"
        ),
    )
