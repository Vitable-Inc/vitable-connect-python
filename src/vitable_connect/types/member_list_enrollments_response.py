# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberListEnrollmentsResponse", "Data"]


class Data(BaseModel):
    """Wire serializer for :class:`MemberEnrollmentDTO` (one benefit enrollment row)."""

    id: str
    """Opaque, stable enrollment identifier used to target enrollment actions"""

    benefit_type: Literal["Medical", "Dental", "Vision", "Hospital"]
    """
    - `Medical` - Medical
    - `Dental` - Dental
    - `Vision` - Vision
    - `Hospital` - Hospital
    """

    cancelled_date: Optional[date] = None
    """
    Earliest applicable coverage boundary (YYYY-MM-DD) when coverage was cancelled
    before its effective start; null unless the enrollment was cancelled
    """

    election_status: Literal["Enrolled", "Waived", "Pending", "Expired"]
    """
    - `Enrolled` - Enrolled
    - `Waived` - Waived
    - `Pending` - Pending
    - `Expired` - Expired
    """

    employer_name: str
    """Name of the employer the enrollment is through"""

    enrollment_window_start: date
    """Enrollment / open-enrollment window start date (YYYY-MM-DD)"""

    in_last_month_of_coverage: bool
    """
    True when today falls in the final month of the plan-year coverage window;
    drives end-of-coverage enrollment actions on the client.
    """

    is_within_enrollment_window: bool
    """
    True when today falls inside the enrollment window this member has to answer in;
    drives enrollment-action availability on the client.
    """

    plan_year_coverage_end: Optional[date] = None
    """
    Benefit plan-year coverage end date (YYYY-MM-DD), distinct from this
    enrollment's coverage_end; null when the plan year is open-ended
    """

    policy_status: Optional[Literal["Coverage Upcoming", "Coverage Effective", "Coverage Ended", "Cancelled"]] = None
    """
    - `Coverage Upcoming` - Coverage Upcoming
    - `Coverage Effective` - Coverage Effective
    - `Coverage Ended` - Coverage Ended
    - `Cancelled` - Cancelled
    """

    product_code: Literal[
        "EBA",
        "VPC",
        "VPC_CORE",
        "MEC",
        "MEC2",
        "MEC_PLUS",
        "MVP",
        "MVP2",
        "MVPSL",
        "MVPSL2",
        "VD",
        "VV",
        "ICHRA",
        "ICHRA_PREMIUM_PLUS",
        "ICHRA_REIMBURSEMENT_ONLY",
    ]
    """
    - `EBA` - Eba Mec
    - `VPC` - Vpc Enhanced
    - `VPC_CORE` - Vpc Core
    - `MEC` - Vpc Mec
    - `MEC2` - Mec2
    - `MEC_PLUS` - Mec Plus
    - `MVP` - Mvp
    - `MVP2` - Mvp2
    - `MVPSL` - Mvpsl
    - `MVPSL2` - Mvpsl2
    - `VD` - Dental
    - `VV` - Vision
    - `ICHRA` - Ichra
    - `ICHRA_PREMIUM_PLUS` - Ichra Premium Plus
    - `ICHRA_REIMBURSEMENT_ONLY` - Ichra Reimbursement Only
    """

    product_name: str
    """Display name of the benefit product"""

    requires_qle_for_reissue: bool
    """
    Whether a qualifying life event would be required to reissue this enrollment
    under the product and open-enrollment rule at the time this list was read
    """

    carrier_name: Optional[str] = None
    """Insurance carrier name; null when no active carrier period is resolvable"""

    coverage_end: Optional[date] = None
    """Coverage window end date (YYYY-MM-DD); null while coverage is open-ended"""

    coverage_start: Optional[date] = None
    """Coverage window start date (YYYY-MM-DD)"""

    employee_deduction_in_cents: Optional[int] = None
    """Employee monthly payroll deduction in cents; null unless the row is an election"""

    employer_contribution_in_cents: Optional[int] = None
    """Employer monthly contribution in cents; null unless the row is an election"""

    enrollment_window_end: Optional[date] = None
    """Enrollment / open-enrollment window end date (YYYY-MM-DD); null when open-ended"""

    plan_name: Optional[str] = None
    """Chosen benefit plan name; null unless the row is an election"""

    premium_in_cents: Optional[int] = None
    """Total monthly plan premium in cents; null unless the row is an election"""

    tier_name: Optional[str] = None
    """
    Chosen benefit plan tier name (e.g., Employee Only); null unless the row is an
    election
    """


class MemberListEnrollmentsResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of member enrollments."""

    data: List[Data]
