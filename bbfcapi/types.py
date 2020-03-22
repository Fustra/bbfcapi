from __future__ import annotations

from enum import Enum, unique

from pydantic import BaseModel

# FastAPI response serialisation - automatic camel-casing
try:
    from humps import camelize
except ImportError:
    camelize = lambda s: s


# TODO: Fix fastapi_camelcase dependencies and use that library instead
class _CamelModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class Film(_CamelModel):
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
