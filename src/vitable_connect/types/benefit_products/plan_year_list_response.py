# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .plan_year import PlanYear
from ..pagination import Pagination

__all__ = ["PlanYearListResponse"]


class PlanYearListResponse(BaseModel):
    """Paginated list response containing plan year resources."""

    data: List[PlanYear]

    pagination: Pagination
    """Pagination metadata for list responses."""
