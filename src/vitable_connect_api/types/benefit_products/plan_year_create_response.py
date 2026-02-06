# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .plan_year import PlanYear

__all__ = ["PlanYearCreateResponse"]


class PlanYearCreateResponse(BaseModel):
    """Response containing a single plan year resource."""

    data: PlanYear
    """Serializer for Plan Year entity in public API responses.

    A Plan Year represents a benefit period configuration including coverage dates,
    open enrollment windows, available plans, and contribution structures.
    """
