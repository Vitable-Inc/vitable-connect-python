# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .event_type import EventType

__all__ = ["QualifyingLifeEventRecordParams"]


class QualifyingLifeEventRecordParams(TypedDict, total=False):
    event_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date when the event occurred"""

    event_type: Required[EventType]
    """
    - `Marriage` - Marriage
    - `Birth` - Birth
    - `Adoption` - Adoption
    - `Divorce` - Divorce
    - `Death` - Death
    - `Job Loss` - Job Loss
    - `Reduction In Hours` - Reduction In Hours
    - `Employer Bankruptcy` - Employer Bankruptcy
    - `Medicare Entitlement` - Medicare Entitlement
    - `Termination` - Termination
    - `Other` - Other
    """

    notes: Optional[str]
    """Optional notes about the event"""
