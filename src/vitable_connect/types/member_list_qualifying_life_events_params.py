# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MemberListQualifyingLifeEventsParams"]


class MemberListQualifyingLifeEventsParams(TypedDict, total=False):
    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    status: Literal["approved", "denied", "pending"]
    """Optional. Filter to a single QLE status; omit to return all statuses."""
