"""Synchronous high-level Python client for a hosted BBFCAPI app.

By default it will query bbfcapi.fustra.co.uk, but you can self-host the app.
"""

from typing import Optional

import requests

from bbfcapi.types import AgeRating, Film

DEFAULT_BASE_URL = "https://bbfcapi.fustra.co.uk"


def top_search_result(
    title: str, year: int, base_url: str = DEFAULT_BASE_URL
) -> Optional[Film]:
    response = requests.get(f"{base_url}/", params={"title": title, "year": year})
    response.raise_for_status()
    json = response.json()
    return Film(
        title=json["title"], year=json["year"], age_rating=AgeRating(json["ageRating"]),
    )


def healthz(base_url: str = DEFAULT_BASE_URL) -> Optional[bool]:
    response = requests.get(f"{base_url}/healthz")
    if response.ok:
        return response.json()["status"] == "OK"

    if response.status_code >= 500:
        return False

    if 300 <= response.status_code < 500:
        return None
