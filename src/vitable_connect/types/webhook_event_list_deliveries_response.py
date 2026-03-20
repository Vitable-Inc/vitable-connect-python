# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookEventListDeliveriesResponse", "Data"]


class Data(BaseModel):
    id: str
    """Prefixed unique identifier for this delivery (e.g., `wdlv_...`)."""

    created_at: datetime
    """When this delivery record was created, in UTC."""

    delivered_at: Optional[datetime] = None
    """When the delivery was successfully received, in UTC."""

    failed_at: Optional[datetime] = None
    """When the delivery was marked as permanently failed, in UTC."""

    failure_reason: str
    """Reason for failure, if applicable."""

    started_at: Optional[datetime] = None
    """When the delivery attempt started, in UTC."""

    status: str
    """Current delivery status: Pending, In Progress, Delivered, or Failed."""

    subscription_id: str
    """The webhook subscription this delivery was sent to."""

    webhook_event_id: str
    """The webhook event this delivery belongs to."""


class WebhookEventListDeliveriesResponse(BaseModel):
    data: List[Data]
