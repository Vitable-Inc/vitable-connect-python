# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmployerUpdateSettingsResponse", "Data"]


class Data(BaseModel):
    pay_frequency: Optional[Literal["weekly", "bi_weekly", "semi_monthly", "monthly"]] = None
    """
    - `weekly` - Weekly
    - `bi_weekly` - Bi-Weekly
    - `semi_monthly` - Semi-Monthly
    - `monthly` - Monthly
    """


class EmployerUpdateSettingsResponse(BaseModel):
    """Response containing a single employer settings resource."""

    data: Data
