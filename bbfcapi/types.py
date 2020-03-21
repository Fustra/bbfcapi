from __future__ import annotations

from enum import Enum, unique

from fastapi_camelcase import CamelModel


class Film(CamelModel):
    title: str
    year: int
    age_rating: AgeRating


@unique
class AgeRating(str, Enum):
    UNIVERSAL = "U"
    PARENTAL_GUIDANCE = "PG"
    AGE_12 = "12"  # Including 12A
    AGE_15 = "15"
    AGE_18 = "18"  # Including R18


Film.update_forward_refs()
