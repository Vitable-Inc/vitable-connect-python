# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .webhook_event import WebhookEvent

__all__ = ["WebhookEventRetrieveResponse"]


class WebhookEventRetrieveResponse(BaseModel):
    """Response containing a single webhook event resource."""

    data: WebhookEvent
