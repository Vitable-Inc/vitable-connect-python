# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SyncRetrieveResponse", "Data", "DataResults", "DataResultsFailure"]


class DataResultsFailure(BaseModel):
    operation: Literal["add", "remove"]
    """
    - `add` - add
    - `remove` - remove
    """

    reason: str

    reference_id: str


class DataResults(BaseModel):
    added_group_member_ids: List[str]

    failures: List[DataResultsFailure]

    removed_group_member_ids: List[str]


class Data(BaseModel):
    accepted_at: datetime

    completed_at: Optional[datetime] = None

    group_id: str

    request_id: str

    results: Optional[DataResults] = None


class SyncRetrieveResponse(BaseModel):
    """Response containing a single group member sync request detail resource."""

    data: Data
