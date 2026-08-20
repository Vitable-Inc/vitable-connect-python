# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmployerListPayrollDeductionStatementsParams"]


class EmployerListPayrollDeductionStatementsParams(TypedDict, total=False):
    limit: int
    """Maximum number of statements per page"""

    page: int
    """Page number to retrieve (starts at 1)"""
