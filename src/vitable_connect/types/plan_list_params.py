# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PlanListParams"]


class PlanListParams(TypedDict, total=False):
    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""
