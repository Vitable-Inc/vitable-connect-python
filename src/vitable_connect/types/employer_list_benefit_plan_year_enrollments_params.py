# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmployerListBenefitPlanYearEnrollmentsParams"]


class EmployerListBenefitPlanYearEnrollmentsParams(TypedDict, total=False):
    employer_id: Required[str]
    """Unique employer identifier (empr\\__\\**)"""

    election_status: List[Literal["Enrolled", "Expired", "Pending", "Waived"]]
    """Filter by election status. Repeat the parameter to match several."""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    search: str
    """Case-insensitive search.

    Matches member name partially, and the `member_id` exactly — either your own
    reference id or the prefixed `grpmbr_<...>` id.
    """
