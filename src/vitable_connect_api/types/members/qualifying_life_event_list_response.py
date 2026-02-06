# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .qualifying_life_event import QualifyingLifeEvent

__all__ = ["QualifyingLifeEventListResponse", "Pagination"]


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


class QualifyingLifeEventListResponse(BaseModel):
    """Paginated list response containing qualifying life event resources."""

    data: List[QualifyingLifeEvent]

    pagination: Pagination
    """Pagination metadata for list responses."""
