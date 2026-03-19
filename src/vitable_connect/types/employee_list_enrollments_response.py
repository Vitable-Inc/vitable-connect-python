# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .enrollment import Enrollment
from .pagination import Pagination

__all__ = ["EmployeeListEnrollmentsResponse"]


class EmployeeListEnrollmentsResponse(BaseModel):
    """Paginated list response containing enrollment resources."""

    data: List[Enrollment]

    pagination: Pagination
    """Pagination metadata for list responses."""
