# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..enrollment import Enrollment

__all__ = ["EnrollmentElectResponse"]


class EnrollmentElectResponse(BaseModel):
    data: Optional[List[Enrollment]] = None
