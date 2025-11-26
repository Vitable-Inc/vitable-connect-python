# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PlanContributionClass"]


class PlanContributionClass(BaseModel):
    compensation: Literal["UNSPECIFIED", "SALARY", "HOURLY"]

    employer_contribution_in_cents: int

    employment: Literal["UNSPECIFIED", "FULL_TIME", "PART_TIME", "TEMPORARY", "SEASONAL"]

    family_status: Literal["UNSPECIFIED", "EE", "ES", "EC", "EF"]

    location: Literal["UNSPECIFIED", "STATE"]

    plan_year_id: str

    location_value: Optional[str] = None

    max_age: Optional[int] = None

    min_age: Optional[int] = None

    plan_id: Optional[str] = None
