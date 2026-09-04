# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Pagination"]


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
