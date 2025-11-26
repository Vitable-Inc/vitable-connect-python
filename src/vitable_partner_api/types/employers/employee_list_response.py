# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..employee import Employee

__all__ = ["EmployeeListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    offset: int

    total: int


class EmployeeListResponse(BaseModel):
    data: Optional[List[Employee]] = None

    pagination: Optional[Pagination] = None
