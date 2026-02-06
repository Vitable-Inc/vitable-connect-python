# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .plan_year import PlanYear

__all__ = ["PlanYearListResponse", "Pagination"]


class Pagination(BaseModel):
    """Pagination metadata for list responses."""

    limit: int
    """Items per page"""

    page: int
    """Current page number"""

    total: int
    """Total number of items"""

    total_pages: int
    """Total number of pages"""


class PlanYearListResponse(BaseModel):
    """Paginated list response containing plan year resources."""

    data: List[PlanYear]

    pagination: Pagination
    """Pagination metadata for list responses."""
