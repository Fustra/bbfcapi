import pytest

from bbfcapi.apilib import top_search_result
from bbfcapi.types import AgeRating, Film


@pytest.mark.asyncio
async def test_top_search_result(mock_search_interstellar):
    result = await top_search_result(title="interstellar", year=2014)
    assert result == Film(title="INTERSTELLAR", year=2014, age_rating=AgeRating.AGE_12)


@pytest.mark.live
@pytest.mark.asyncio
async def test_top_search_result_integration():
    result = await top_search_result(title="interstellar", year=2014)
    assert result == Film(title="INTERSTELLAR", year=2014, age_rating=AgeRating.AGE_12)


@pytest.mark.asyncio
async def test_top_search_result_with_no_results(mock_search_no_results):
    result = await top_search_result(title="no-film", year=1900)
    assert result is None


@pytest.mark.live
@pytest.mark.asyncio
async def test_top_search_result_no_results_integration():
    result = await top_search_result(title="no-film", year=1900)
    assert result is None
