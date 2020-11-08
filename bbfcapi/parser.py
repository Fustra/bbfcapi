"""JSON Parser for the BBFC GraphQL API."""
from typing import Any, Dict, Optional

from bbfcapi.types import AgeRating, Film


def best_autocomplete_match(
    response_json: Dict[str, Any], title: str
) -> Optional[Film]:
    results = response_json["data"]["autocomplete"]["results"]
    return _exact_match(results, title) or _first_match(results, title)


def _exact_match(results: Dict[str, Any], title: str) -> Optional[Film]:
    results_by_title = {result["title"].casefold(): result for result in results}
    maybe_result = results_by_title.get(title.casefold())
    if maybe_result is None:
        return None

    return _result_to_film(maybe_result)


def _first_match(results: Dict[str, Any], title: str) -> Optional[Film]:
    if not results:
        return None

    return _result_to_film(results[0])


def _result_to_film(result: Dict[str, Any]) -> Film:
    return Film(
        title=result["title"],
        age_rating=_classification_to_age_rating(result["classification"]),
    )


def _classification_to_age_rating(classification: str) -> AgeRating:
    return AgeRating(classification.rstrip("A"))  # Remove suffix from "12A"
