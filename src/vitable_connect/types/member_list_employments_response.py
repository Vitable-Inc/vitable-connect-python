# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .employee import Employee

__all__ = ["MemberListEmploymentsResponse"]


class MemberListEmploymentsResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of member employments."""

    data: List[Employee]
