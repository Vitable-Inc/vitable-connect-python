# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["SyncSubmitResponse", "Data"]


class Data(BaseModel):
    accepted_at: datetime

    group_id: str

    request_id: str


class SyncSubmitResponse(BaseModel):
    """Response containing a single group member sync detail resource."""

    data: Data
