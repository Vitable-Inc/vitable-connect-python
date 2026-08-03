# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EmployerListParams"]


class EmployerListParams(TypedDict, total=False):
    benefit_family: List[Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]]
    """Filter to employers with at least one active benefit in these families."""

    benefit_lifecycle_stage: List[Literal["open_enrollment", "renewal", "active", "onboarding", "cancelled"]]
    """Filter to employers in one of these computed benefit-lifecycle stages."""

    hris_status: List[Literal["Pending", "Active", "Inactive", "Paused", "Terminated"]]
    """Filter to employers whose HRIS connection is in one of these statuses."""

    include_cancelled: bool
    """
    Include cancelled employers (hidden by default unless their stage is explicitly
    requested).
    """

    limit: int
    """Items per page."""

    page: int
    """Page number."""

    search: Optional[str]
    """Case-insensitive employer-name substring filter."""
