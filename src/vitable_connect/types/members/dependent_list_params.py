# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..relationship import Relationship

__all__ = ["DependentListParams"]


class DependentListParams(TypedDict, total=False):
    active_in: bool
    """Filter by active status"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    relationship: Relationship
    """Filter by relationship type"""
