import os

DEFAULT_BASE_URL = "https://bbfc.co.uk"

SEARCH_URL = "{base_url}/search/releases/{title}/any/any/any/any/0/any/any/any/any/{year}/any/any?advanced=true"


def search_url(title: str, year: int) -> str:
    base_url = os.environ.get("BBFC_URL", DEFAULT_BASE_URL)
    return SEARCH_URL.format(base_url=base_url, title=title, year=year)
