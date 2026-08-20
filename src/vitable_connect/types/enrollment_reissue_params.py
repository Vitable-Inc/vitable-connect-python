# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EnrollmentReissueParams"]


class EnrollmentReissueParams(TypedDict, total=False):
    qualifying_life_event_id: Optional[str]
    """Accepted member qualifying life event identifier (qle\\__\\**)"""

    reason: Optional[str]
    """
    Audit reason for the reissue; required for user-backed callers and optional for
    userless organization callers
    """

    ticket_number: Optional[str]
    """Optional support or operational ticket number"""
