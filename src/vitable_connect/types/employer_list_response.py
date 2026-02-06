# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .employer import Employer
from .pagination import Pagination

__all__ = ["EmployerListResponse"]


class EmployerListResponse(BaseModel):
    """Paginated list response containing employer resources."""

    data: List[Employer]

    pagination: Pagination
    """Pagination metadata for list responses."""
