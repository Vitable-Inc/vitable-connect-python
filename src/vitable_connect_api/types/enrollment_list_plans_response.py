# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .plan_tier import PlanTier
from .coverage_tier import CoverageTier

__all__ = ["EnrollmentListPlansResponse", "EnrollmentListPlansResponseItem", "EnrollmentListPlansResponseItemCost"]


class EnrollmentListPlansResponseItemCost(BaseModel):
    """Cost breakdown for a plan option."""

    coverage_tier: CoverageTier
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """

    employee_contribution_cents: int
    """Employee's monthly contribution in cents"""

    employer_contribution_cents: int
    """Employer's monthly contribution in cents"""

    total_monthly_premium_cents: int
    """Total monthly premium in cents"""


class EnrollmentListPlansResponseItem(BaseModel):
    """Serializer for plan options available for enrollment selection.

    Returns plan details with cost breakdowns for each coverage tier.
    """

    id: str
    """Unique plan identifier (plan\\__\\**)"""

    costs: List[EnrollmentListPlansResponseItemCost]
    """Cost breakdown by coverage tier"""

    name: str
    """Display name of the plan"""

    carrier_name: Optional[str] = None
    """Name of the insurance carrier"""

    deductible_cents: Optional[int] = None
    """Annual deductible in cents"""

    description: Optional[str] = None
    """Plan description"""

    out_of_pocket_max_cents: Optional[int] = None
    """Annual out-of-pocket maximum in cents"""

    tier: Optional[PlanTier] = None
    """
    - `Bronze` - Bronze
    - `Silver` - Silver
    - `Gold` - Gold
    - `Platinum` - Platinum
    """


EnrollmentListPlansResponse: TypeAlias = List[EnrollmentListPlansResponseItem]
