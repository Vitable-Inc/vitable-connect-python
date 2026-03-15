# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..employee_class import EmployeeClass

__all__ = ["EmployeeListParams"]


class EmployeeListParams(TypedDict, total=False):
    active_in: bool
    """Filter by active status"""

    employee_class: EmployeeClass
    """Filter by employment classification"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""
