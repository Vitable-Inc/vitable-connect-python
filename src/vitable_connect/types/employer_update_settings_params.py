# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmployerUpdateSettingsParams"]


class EmployerUpdateSettingsParams(TypedDict, total=False):
    pay_frequency: Required[Literal["weekly", "bi_weekly", "semi_monthly", "monthly"]]
    """
    - `weekly` - weekly
    - `bi_weekly` - bi_weekly
    - `semi_monthly` - semi_monthly
    - `monthly` - monthly
    """
