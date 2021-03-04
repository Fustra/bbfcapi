"""Synchronous high-level Python client for a hosted BBFCAPI app.

By default it will query bbfcapi.fustra.uk, but you can self-host the app.

This will raise exceptions from the requests library.
"""

from typing import Optional

import requests

from bbfcapi.types import Film

DEFAULT_BASE_URL = "https://bbfcapi.fustra.uk"


def best_match(title: str, base_url: str = DEFAULT_BASE_URL) -> Optional[Film]:
    response = requests.get(f"{base_url}/", params={"title": title})
    if response.ok:
        return Film.parse_raw(
            response.content, content_type=response.headers["Content-Type"]
        )

    if response.status_code == 404:
        return None

    response.raise_for_status()


def healthz(base_url: str = DEFAULT_BASE_URL) -> bool:
    """Return whether the client <-> server connection is good.

    We will not raise exceptions from the requests library."""
    try:
        response = requests.get(f"{base_url}/healthz")
        response.raise_for_status()
    except requests.RequestException:
        return False

    return True
