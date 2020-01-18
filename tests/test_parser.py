from bbfcapi.parser import parse_top_search_result
from bbfcapi.types import AgeRating, Film


def test_parse_top_search_result(data_search_interstellar):
    result = parse_top_search_result(data_search_interstellar)
    assert result == Film(title="INTERSTELLAR", year=2014, age_rating=AgeRating.AGE_12)


def test_parse_top_search_result_with_no_results(data_search_no_results):
    result = parse_top_search_result(data_search_no_results)
    assert result is None
