# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel
from .coverage_tier import CoverageTier
from .members.relationship import Relationship
from .employees.enrollment_status import EnrollmentStatus

__all__ = ["Enrollment", "EnrolledDependent"]


class EnrolledDependent(BaseModel):
    dependent_id: str
    """ID of the dependent (dpnd\\__\\**)"""

    first_name: str
    """Dependent's first name"""

    last_name: str
    """Dependent's last name"""

    relationship: Relationship
    """
    - `Spouse` - Spouse
    - `Child` - Child
    """


class Enrollment(BaseModel):
    id: str
    """Unique enrollment identifier with 'enrl\\__' prefix"""

    benefit_product_id: str
    """ID of the benefit product (bprd\\__\\**)"""

    created_at: datetime
    """Timestamp when the enrollment was created"""

    employee_id: str
    """ID of the employee (empl\\__\\**)"""

    plan_year_id: str
    """ID of the plan year (plyr\\__\\**)"""

    status: EnrollmentStatus
    """
    - `pending` - Pending
    - `enrolled` - Enrolled
    - `waived` - Waived
    - `inactive` - Inactive
    """

    updated_at: datetime
    """Timestamp when the enrollment was last updated"""

    coverage_end_date: Optional[date] = None
    """Date when coverage ends"""

    coverage_start_date: Optional[date] = None
    """Date when coverage begins"""

    coverage_tier: Optional[CoverageTier] = None
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """

    decision: Optional[str] = None
    """Employee's election decision: 'enrolled' (accepted) or 'waived' (declined)"""

    employee_contribution_cents: Optional[int] = None
    """Employee's monthly contribution in cents"""

    employer_contribution_cents: Optional[int] = None
    """Employer's monthly contribution in cents"""

    enrolled_dependents: Optional[List[EnrolledDependent]] = None
    """List of dependents included in this enrollment"""

    selected_plan_id: Optional[str] = None
    """ID of the selected plan (plan\\__\\**), if enrolled"""

    selected_plan_name: Optional[str] = None
    """Name of the selected plan"""
