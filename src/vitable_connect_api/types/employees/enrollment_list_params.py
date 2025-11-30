# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .enrollment_status import EnrollmentStatus

__all__ = ["EnrollmentListParams"]


class EnrollmentListParams(TypedDict, total=False):
    coverage_effective_start_year: int
    """Filter by coverage year"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    plan_year: int
    """Filter by plan year start (YYYY)"""

    status: EnrollmentStatus
    """Filter by enrollment status"""
