# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..coverage_tier import CoverageTier

__all__ = ["PlanYearCreateParams", "ContributionClass"]


class PlanYearCreateParams(TypedDict, total=False):
    contribution_classes: Required[Iterable[ContributionClass]]
    """List of contribution classes (at least one required)"""

    coverage_end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Coverage end date"""

    coverage_start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Coverage start date"""

    employer_id: Required[str]
    """Employer ID this plan year is for (empr\\__\\**)"""

    open_enrollment_end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Open enrollment end date"""

    open_enrollment_start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Open enrollment start date"""


class ContributionClass(TypedDict, total=False):
    """Contribution class input for plan year creation."""

    coverage_tier: Required[CoverageTier]
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """

    employee_contribution_cents: Required[int]
    """Employee's monthly contribution in cents"""

    employer_contribution_cents: Required[int]
    """Employer's monthly contribution in cents"""

    employment: Required[str]
    """Employment type (e.g., 'full_time', 'part_time')"""
