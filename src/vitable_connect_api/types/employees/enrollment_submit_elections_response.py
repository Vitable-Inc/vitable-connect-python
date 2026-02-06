# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..enrollment import Enrollment

__all__ = ["EnrollmentSubmitElectionsResponse", "Pagination"]


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


class EnrollmentSubmitElectionsResponse(BaseModel):
    """Paginated list response containing enrollment resources."""

    data: List[Enrollment]

    pagination: Pagination
    """Pagination metadata for list responses."""
