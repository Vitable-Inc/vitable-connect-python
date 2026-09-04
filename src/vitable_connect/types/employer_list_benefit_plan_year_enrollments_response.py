# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmployerListBenefitPlanYearEnrollmentsResponse"]


class EmployerListBenefitPlanYearEnrollmentsResponse(BaseModel):
    carrier: Optional[str] = None
    """
    The carrier for this enrollment: the individual-market carrier for an ICHRA
    plan, otherwise the benefit's own. Null when the benefit has no carrier.
    """

    dependent_count: int
    """Dependents covered under this enrollment today.

    Counts the same dependents `premium_in_cents` is priced for, so a dependent
    whose termination is dated in the future still counts.
    """

    election_status: Literal["Enrolled", "Waived", "Pending", "Expired"]
    """
    - `Enrolled` - Enrolled
    - `Waived` - Waived
    - `Pending` - Pending
    - `Expired` - Expired
    """

    employee_deduction_in_cents: Optional[int] = None
    """
    What the employee is deducted monthly, in cents: `premium_in_cents` less
    `employer_contribution_in_cents`, floored at zero. Null when unanswered/waived.
    """

    employee_external_reference_id: Optional[str] = None
    """Your own reference id for this employee, as you supplied it.

    Null when you have not set one.
    """

    employee_id: str
    """Our id for this person's employment with this employer (`empl_<...>`).

    A person who leaves and is rehired has two.
    """

    employer_contribution_in_cents: Optional[int] = None
    """The employer's monthly share of `premium_in_cents`, in cents.

    Null when unanswered/waived.
    """

    member_first_name: str
    """The member's first name."""

    member_id: str
    """Our id for the person (`mbr_<...>`).

    Stable across every employer they work for.
    """

    member_last_name: str
    """The member's last name."""

    plan: Optional[str] = None
    """Chosen plan name, or null when unanswered/waived."""

    policy_status: Optional[Literal["Coverage Upcoming", "Coverage Effective", "Coverage Ended", "Cancelled"]] = None
    """
    - `Coverage Upcoming` - Coverage Upcoming
    - `Coverage Effective` - Coverage Effective
    - `Coverage Ended` - Coverage Ended
    - `Cancelled` - Cancelled
    """

    premium_in_cents: Optional[int] = None
    """Monthly premium in cents for the chosen plan, dependents included.

    The plan's own cost, not the employer's share of it. Null when
    unanswered/waived.
    """

    tier: Optional[str] = None
    """Chosen coverage tier, or null when unanswered/waived."""
