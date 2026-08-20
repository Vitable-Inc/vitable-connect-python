# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberListQualifyingLifeEventsResponse"]


class MemberListQualifyingLifeEventsResponse(BaseModel):
    id: str
    """Opaque qualifying life event identifier"""

    event_type: Literal["Married", "Divorced", "New child", "Court ordered", "Other"]
    """
    - `Married` - Married
    - `Divorced` - Divorced
    - `New child` - New Child
    - `Court ordered` - Court Ordered
    - `Other` - Other
    """

    other_event: Optional[str] = None
    """Custom event description when event_type is Other; otherwise normally null"""

    status: Literal["pending", "approved", "denied"]
    """
    - `pending` - Pending
    - `approved` - Approved
    - `denied` - Denied
    """

    submitted_at: datetime
    """When the member submitted the event"""
