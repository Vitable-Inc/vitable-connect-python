# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Optional[Literal["BROKERAGE", "TPA", "GENERAL_AGENT", "CHANNEL_PARTNER", "CONSULTING_FIRM", "API_PLATFORM"]]
    """
    - `BROKERAGE` - BROKERAGE
    - `TPA` - TPA
    - `GENERAL_AGENT` - GENERAL_AGENT
    - `CHANNEL_PARTNER` - CHANNEL_PARTNER
    - `CONSULTING_FIRM` - CONSULTING_FIRM
    - `API_PLATFORM` - API_PLATFORM
    """
