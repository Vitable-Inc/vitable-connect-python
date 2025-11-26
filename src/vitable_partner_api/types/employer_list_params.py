# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmployerListParams"]


class EmployerListParams(TypedDict, total=False):
    limit: int
    """Number of results to return"""

    offset: int
    """Number of results to skip"""
