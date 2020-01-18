import pytest

from bbfcapi.lib import top_search_result
from bbfcapi.types import AgeRating, Film


@pytest.mark.live
@pytest.mark.asyncio
async def test_top_search_result_integration(data_search_interstellar):
    result = await top_search_result(title="interstellar", year=2014)
    assert result == Film(title="INTERSTELLAR", year=2014, age_rating=AgeRating.AGE_12)
