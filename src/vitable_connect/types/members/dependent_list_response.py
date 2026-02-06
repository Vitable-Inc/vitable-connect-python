# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..dependent import Dependent
from ..pagination import Pagination

__all__ = ["DependentListResponse"]


class DependentListResponse(BaseModel):
    """Paginated list response containing dependent resources."""

    data: List[Dependent]

    pagination: Pagination
    """Pagination metadata for list responses."""
