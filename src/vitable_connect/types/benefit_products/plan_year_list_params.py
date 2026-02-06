# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .plan_year_status import PlanYearStatus

__all__ = ["PlanYearListParams"]


class PlanYearListParams(TypedDict, total=False):
    employer_id: str
    """Filter by employer ID"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    status: PlanYearStatus
    """Filter by plan year status"""
