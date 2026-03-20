# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookEvent"]


class WebhookEvent(BaseModel):
    id: str
    """Prefixed unique identifier for this webhook event (e.g., `wevt_...`)."""

    created_at: datetime
    """When the event occurred, in UTC."""

    event_name: str
    """
    The event type, formatted as `{resource}.{action}` (e.g.,
    `enrollment.accepted`).
    """

    organization_id: str
    """The organization this event belongs to."""

    resource_id: str
    """Prefixed ID of the affected resource.

    Use this to fetch the current state from the API.
    """

    resource_type: str
    """The type of resource affected (e.g., `enrollment`, `employee`)."""
