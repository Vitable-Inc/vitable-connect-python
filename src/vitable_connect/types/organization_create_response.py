# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OrganizationCreateResponse"]


class OrganizationCreateResponse(BaseModel):
    id: str
    """Prefixed organization identifier (`org_<base64-encoded-uuid>`)."""

    idp_org_id: Optional[str] = None
    """IdP-issued tenant id (WorkOS org id)."""

    idp_provider: Optional[Literal["workos", "vitable"]] = None
    """
    - `workos` - WorkOS
    - `vitable` - Vitable
    """

    name: str
    """Human-readable organization name."""

    super_in: bool
    """Whether this organization reads across every organization."""

    type: Optional[
        Literal["BROKERAGE", "TPA", "GENERAL_AGENT", "CHANNEL_PARTNER", "CONSULTING_FIRM", "API_PLATFORM"]
    ] = None
    """
    - `BROKERAGE` - Brokerage
    - `TPA` - TPA
    - `GENERAL_AGENT` - General Agent
    - `CHANNEL_PARTNER` - Channel Partner
    - `CONSULTING_FIRM` - Consulting Firm
    - `API_PLATFORM` - API Platform
    """
