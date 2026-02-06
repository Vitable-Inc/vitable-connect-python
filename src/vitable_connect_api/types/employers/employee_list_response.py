# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..employee import Employee

__all__ = ["EmployeeListResponse", "Pagination"]


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


class EmployeeListResponse(BaseModel):
    """Paginated list response containing employee resources."""

    data: List[Employee]

    pagination: Pagination
    """Pagination metadata for list responses."""
