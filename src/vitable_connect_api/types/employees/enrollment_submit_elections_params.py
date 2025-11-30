# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..coverage_tier import CoverageTier

__all__ = ["EnrollmentSubmitElectionsParams", "Election"]


class EnrollmentSubmitElectionsParams(TypedDict, total=False):
    elections: Required[Iterable[Election]]
    """List of enrollment elections"""


class Election(TypedDict, total=False):
    decision: Required[Literal["Enrolled", "Waived"]]
    """
    - `Enrolled` - Enrolled
    - `Waived` - Waived
    """

    enrollment_id: Required[str]
    """ID of the enrollment (enrl\\__\\**)"""

    coverage_tier: Optional[CoverageTier]
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """

    dependent_ids: Optional[SequenceNotStr[str]]
    """List of dependent IDs to include in coverage (dpnd\\__\\**)"""

    selected_plan_id: Optional[str]
    """ID of the selected plan (plan\\__\\**). Required if decision is 'Enrolled'"""
