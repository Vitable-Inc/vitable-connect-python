# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..dependent import Dependent

__all__ = ["DependentListResponse", "Pagination"]


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


class DependentListResponse(BaseModel):
    """Paginated list response containing dependent resources."""

    data: List[Dependent]

    pagination: Pagination
    """Pagination metadata for list responses."""
