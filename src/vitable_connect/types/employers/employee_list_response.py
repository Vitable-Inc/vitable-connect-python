# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..employee import Employee
from ..pagination import Pagination

__all__ = ["EmployeeListResponse"]


class EmployeeListResponse(BaseModel):
    """Paginated list response containing employee resources."""

    data: List[Employee]

    pagination: Pagination
    """Pagination metadata for list responses."""
