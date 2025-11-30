# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .coverage_tier import CoverageTier

__all__ = ["PlanYearUpdateParams", "ContributionClass"]


class PlanYearUpdateParams(TypedDict, total=False):
    contribution_classes: Optional[Iterable[ContributionClass]]
    """Updated contribution classes"""

    open_enrollment_end: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Open enrollment end date"""

    open_enrollment_start: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Open enrollment start date"""

    status: Optional[str]
    """Plan year status"""


class ContributionClass(TypedDict, total=False):
    employee_contribution_cents: Required[int]
    """Employee's monthly contribution in cents"""

    employer_contribution_cents: Required[int]
    """Employer's monthly contribution in cents"""

    employment: Required[str]
    """Employment type"""

    family_status: Required[CoverageTier]
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """
