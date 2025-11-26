# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .plan import Plan
from .._models import BaseModel

__all__ = ["EnrollmentGetEligiblePlansResponse"]


class EnrollmentGetEligiblePlansResponse(BaseModel):
    data: Optional[List[Plan]] = None
