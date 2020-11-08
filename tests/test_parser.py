from bbfcapi.parser import best_autocomplete_match
from bbfcapi.types import AgeRating, Film


def test_best_autocomplete_match_with_multiple_results(search_interstellar_json):
    result = best_autocomplete_match(search_interstellar_json, title="Interstellar")
    assert result == Film(title="Interstellar", age_rating=AgeRating.AGE_12)


def test_best_autocomplete_match_with_one_result(search_a_silent_voice_json):
    result = best_autocomplete_match(search_a_silent_voice_json, title="A Silent Voice")
    assert result == Film(title="A Silent Voice", age_rating=AgeRating.AGE_12)


def test_best_autocomplete_match_with_no_results(search_no_film_json):
    result = best_autocomplete_match(search_no_film_json, "no-film")
    assert result is None
