# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..plan_year import PlanYear

__all__ = ["PlanYearListResponse"]


class PlanYearListResponse(BaseModel):
    data: Optional[List[PlanYear]] = None
