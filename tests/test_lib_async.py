import pytest

from bbfcapi.lib_async import best_match
from bbfcapi.types import AgeRating, Film


@pytest.mark.asyncio
async def test_best_match(mock_search_interstellar):
    result = await best_match(title="interstellar")
    assert result == Film(title="Interstellar", age_rating=AgeRating.AGE_12)


@pytest.mark.live
@pytest.mark.asyncio
async def test_best_match_integration():
    result = await best_match(title="interstellar")
    assert result == Film(title="Interstellar", age_rating=AgeRating.AGE_12)


@pytest.mark.asyncio
async def test_best_match_with_no_results(mock_search_no_film):
    result = await best_match(title="no-film")
    assert result is None


@pytest.mark.live
@pytest.mark.asyncio
async def test_best_match_no_results_integration():
    result = await best_match(title="no-film")
    assert result is None
