# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from ..._models import BaseModel
from .qualifying_life_event_status import QualifyingLifeEventStatus

__all__ = ["QualifyingLifeEvent"]


class QualifyingLifeEvent(BaseModel):
    """Serializer for Qualifying Life Event entity in public API responses.

    QLEs are significant life changes (marriage, birth, adoption, loss of coverage)
    that allow employees to modify benefit elections outside of open enrollment.
    """

    id: str
    """Unique QLE identifier with 'qle\\__' prefix"""

    created_at: datetime
    """Timestamp when the QLE was created"""

    employee_id: str
    """ID of the employee (empl\\__\\**)"""

    enrollment_window_end: date
    """End of the special enrollment period (typically 30-60 days from event)"""

    enrollment_window_start: date
    """Start of the special enrollment period"""

    event_date: date
    """Date when the qualifying life event occurred"""

    event_type: str
    """
    Type of qualifying life event (e.g., 'marriage', 'birth', 'adoption',
    'loss_of_coverage', 'divorce')
    """

    member_id: str
    """ID of the member experiencing the life event (mbr\\__\\**)"""

    status: QualifyingLifeEventStatus
    """
    - `pending` - Pending
    - `approved` - Approved
    - `denied` - Denied
    """

    updated_at: datetime
    """Timestamp when the QLE was last updated"""

    notes: Optional[str] = None
    """Additional notes or comments about the QLE"""

    reviewed_at: Optional[datetime] = None
    """Timestamp when the QLE was reviewed, if reviewed"""

    reviewed_by: Optional[str] = None
    """ID of the user who reviewed the QLE, if reviewed"""
