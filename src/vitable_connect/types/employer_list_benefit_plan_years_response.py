# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "EmployerListBenefitPlanYearsResponse",
    "Data",
    "DataEmployeeContribution",
    "DataEmployerContribution",
    "DataEnrollmentRate",
]


class DataEmployeeContribution(BaseModel):
    """Employee contribution range."""

    max_cents: int
    """Highest per-tier contribution in cents."""

    min_cents: int
    """Lowest per-tier contribution in cents."""


class DataEmployerContribution(BaseModel):
    """Employer contribution range."""

    max_cents: int
    """Highest per-tier contribution in cents."""

    min_cents: int
    """Lowest per-tier contribution in cents."""


class DataEnrollmentRate(BaseModel):
    """Enrolled/eligible rate for this plan year."""

    eligible: int
    """Employees eligible for this plan year."""

    enrolled: int
    """Employees enrolled in this plan year."""

    percentage: int
    """`enrolled / eligible` whole-number percent (0 when none)."""


class Data(BaseModel):
    """One plan year, list view.

    Standalone (no shared base) so the exact list payload is readable in one place; the detail
    serializer is a separate class even where fields overlap.
    """

    benefit_id: str
    """Prefixed benefit identifier (`bprd_*`)."""

    benefit_plan_year_id: str
    """Prefixed plan-year identifier (`plyr_*`)."""

    carrier: Optional[str] = None
    """Carrier name, or null (e.g. ICHRA)."""

    coverage_end: Optional[date] = None
    """Coverage end."""

    coverage_start: date
    """Coverage start."""

    employee_contribution: Optional[DataEmployeeContribution] = None
    """Employee contribution range."""

    employer_contribution: Optional[DataEmployerContribution] = None
    """Employer contribution range."""

    enrollment_rate: DataEnrollmentRate
    """Enrolled/eligible rate for this plan year."""

    family: Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]
    """
    - `mec` - Mec
    - `mvp` - Mvp
    - `ichra` - Ichra
    - `vpc` - Vpc
    - `dental` - Dental
    - `vision` - Vision
    """

    is_current: bool
    """Whether this is the current plan year."""

    network_names: List[str]
    """
    Displayed networks: ["multi"] for ICHRA, otherwise the plan year's distinct
    network names.
    """

    offered_states: List[str]
    """Distinct offered state codes."""

    open_enrollment_end: Optional[date] = None
    """Open-enrollment end."""

    open_enrollment_start: date
    """Open-enrollment start."""

    premium_in_cents: Optional[int] = None
    """Monthly premium in cents; only for an ICHRA benefit with effective coverage."""

    product_name: str
    """Benefit/product display name."""

    status: Literal["active", "upcoming", "open_enrollment", "inactive"]
    """
    - `active` - Active
    - `upcoming` - Upcoming
    - `open_enrollment` - Open Enrollment
    - `inactive` - Inactive
    """

    year: int
    """Calendar coverage year."""


class EmployerListBenefitPlanYearsResponse(BaseModel):
    data: List[Data]
