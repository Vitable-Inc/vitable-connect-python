# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SyncRetrieveResponse", "Data"]


class Data(BaseModel):
    accepted_at: datetime

    completed_at: Optional[datetime] = None

    group_id: str

    request_id: str

    results: object


class SyncRetrieveResponse(BaseModel):
    """Response containing a single group member sync request detail resource."""

    data: Data
