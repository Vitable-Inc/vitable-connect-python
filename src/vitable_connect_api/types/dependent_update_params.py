# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .members.relationship import Relationship

__all__ = ["DependentUpdateParams"]


class DependentUpdateParams(TypedDict, total=False):
    active: Optional[bool]
    """Whether the dependent is active"""

    gender: Optional[str]
    """Gender identity"""

    relationship: Optional[Relationship]
    """
    - `Spouse` - Spouse
    - `Child` - Child
    """
