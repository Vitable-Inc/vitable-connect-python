# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .employer import Employer

__all__ = ["EmployerListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    offset: int

    total: int


class EmployerListResponse(BaseModel):
    data: Optional[List[Employer]] = None

    pagination: Optional[Pagination] = None
