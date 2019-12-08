from bbfcapi.parser import top_search_result
from bbfcapi.types import AgeRating, Film


async def test_top_search_result(data_search_interstellar):
    result = top_search_result(data_search_interstellar)
    assert result == Film(title="INTERSTELLAR", year=2014, age_rating=AgeRating.AGE_12)
