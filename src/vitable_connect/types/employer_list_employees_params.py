# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EmployerListEmployeesParams"]


class EmployerListEmployeesParams(TypedDict, total=False):
    employment_status: Literal["active", "terminated"]
    """Filter by employment status (active or terminated)"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    search: Optional[str]
    """Case-insensitive search across employee first name, last name, and email"""
