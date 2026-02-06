# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..pagination import Pagination
from .qualifying_life_event import QualifyingLifeEvent

__all__ = ["QualifyingLifeEventListResponse"]


class QualifyingLifeEventListResponse(BaseModel):
    """Paginated list response containing qualifying life event resources."""

    data: List[QualifyingLifeEvent]

    pagination: Pagination
    """Pagination metadata for list responses."""
