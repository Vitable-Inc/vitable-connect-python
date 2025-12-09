# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ..._models import BaseModel
from ..plan_tier import PlanTier
from ..coverage_tier import CoverageTier
from .plan_year_status import PlanYearStatus

__all__ = ["PlanYear", "ContributionClass", "Plan"]


class ContributionClass(BaseModel):
    """Defines eligibility tiers for contributions within a plan year.

    Contribution classes specify cost structures based on employment type
    and family coverage status.
    """

    id: str
    """Unique contribution class identifier"""

    employee_contribution_cents: int
    """Employee's monthly contribution amount in cents"""

    employer_contribution_cents: int
    """Employer's monthly contribution amount in cents"""

    employment: str
    """Employment type for this contribution class (e.g., 'full_time', 'part_time')"""

    family_status: CoverageTier
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """


class Plan(BaseModel):
    """Nested plan within PlanYearSerializer."""

    id: str
    """Unique plan identifier with 'plan\\__' prefix"""

    carrier_plan_id: str
    """Reference to the carrier's plan definition (cplan\\__\\**)"""

    monthly_premium_cents: int
    """Base monthly premium in cents"""

    name: str
    """Display name of the insurance plan"""

    deductible_cents: Optional[int] = None
    """Annual deductible amount in cents"""

    out_of_pocket_max_cents: Optional[int] = None
    """Annual out-of-pocket maximum in cents"""

    tier: Optional[PlanTier] = None
    """
    - `Bronze` - Bronze
    - `Silver` - Silver
    - `Gold` - Gold
    - `Platinum` - Platinum
    """


class PlanYear(BaseModel):
    """Serializer for Plan Year entity in public API responses.

    A Plan Year represents a benefit period configuration including coverage dates,
    open enrollment windows, available plans, and contribution structures.
    """

    id: str
    """Unique plan year identifier with 'plyr\\__' prefix"""

    benefit_product_id: str
    """ID of the benefit product (bprd\\__\\**)"""

    contribution_classes: List[ContributionClass]
    """List of contribution classes defining eligibility tiers and cost structures"""

    coverage_end: date
    """Date when benefit coverage ends"""

    coverage_start: date
    """Date when benefit coverage begins"""

    created_at: datetime
    """Timestamp when the plan year was created"""

    employer_id: str
    """ID of the employer this plan year is for (empr\\__\\**)"""

    open_enrollment_end_date: date
    """Date when open enrollment period ends"""

    open_enrollment_start_date: date
    """Date when open enrollment period begins"""

    plans: List[Plan]
    """List of insurance plans available in this plan year"""

    status: PlanYearStatus
    """
    - `draft` - Draft
    - `open_enrollment` - Open Enrollment
    - `active` - Active
    - `expired` - Expired
    """

    updated_at: datetime
    """Timestamp when the plan year was last updated"""
