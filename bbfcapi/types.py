from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, unique


@dataclass(frozen=True)
class Film:
    title: str
    year: int
    age_rating: AgeRating


@unique
class AgeRating(Enum):
    UNIVERSAL = "U"
    PARENTAL_GUIDANCE = "PG"
    AGE_12 = "12"  # Including 12A
    AGE_15 = "15"
    AGE_18 = "18"  # Including R18
