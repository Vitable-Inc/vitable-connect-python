# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..qualifying_life_event import QualifyingLifeEvent

__all__ = ["QualifyingLifeEventListResponse"]


class QualifyingLifeEventListResponse(BaseModel):
    data: Optional[List[QualifyingLifeEvent]] = None
