# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .employer import Employer

__all__ = ["EmployerListResponse", "Pagination"]


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


class EmployerListResponse(BaseModel):
    """Paginated list response containing employer resources."""

    data: List[Employer]

    pagination: Pagination
    """Pagination metadata for list responses."""
