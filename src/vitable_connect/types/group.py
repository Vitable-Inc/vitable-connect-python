# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str
    """Prefixed group identifier (`grp_<base64-encoded-uuid>`)."""

    created_at: Optional[datetime] = None
    """Group creation timestamp (ISO 8601, UTC)."""

    external_reference_id: str
    """Stable identifier for this group in the integrator's own system."""

    name: str
    """Human-readable group name."""

    organization_id: str
    """Prefixed organization identifier (`org_<base64-encoded-uuid>`)."""

    updated_at: Optional[datetime] = None
    """Last-update timestamp (ISO 8601, UTC)."""
