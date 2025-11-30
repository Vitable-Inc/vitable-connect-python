# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .event_type import EventType
from .qualifying_life_event_status import QualifyingLifeEventStatus

__all__ = ["QualifyingLifeEventListParams"]


class QualifyingLifeEventListParams(TypedDict, total=False):
    event_type: EventType
    """Filter by QLE type"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    status: QualifyingLifeEventStatus
    """Filter by QLE status"""
