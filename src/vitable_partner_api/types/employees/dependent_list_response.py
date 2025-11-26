# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..dependent import Dependent

__all__ = ["DependentListResponse"]


class DependentListResponse(BaseModel):
    data: Optional[List[Dependent]] = None
