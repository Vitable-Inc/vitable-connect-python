# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .enrollment_status import EnrollmentStatus

__all__ = ["EnrollmentRetrieveResponse", "Data", "DataBenefit"]


class DataBenefit(BaseModel):
    """Nested benefit product summary"""

    id: str
    """Benefit product ID (bprd\\__\\**)"""

    category: Literal["Medical", "Dental", "Vision", "Hospital"]
    """
    - `Medical` - Medical
    - `Dental` - Dental
    - `Vision` - Vision
    - `Hospital` - Hospital
    """

    name: str
    """Display name of the benefit product"""

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


class Data(BaseModel):
    """A single enrollment, including the enrolled plan's documents.

    The plan documents are resolved one enrollment at a time and are therefore not part of the
    list row.
    """

    id: str
    """Unique enrollment identifier (enrl\\__\\**)"""

    answered_at: Optional[datetime] = None
    """When the employee enrolled or waived"""

    benefit: DataBenefit
    """Nested benefit product summary"""

    coverage_end: Optional[date] = None
    """Coverage period end date"""

    coverage_start: date
    """Coverage period start date"""

    created_at: datetime
    """When the enrollment was created"""

    employee_deduction_in_cents: Optional[int] = None
    """Employee monthly payroll deduction in cents"""

    employee_id: str
    """Employee ID (empl\\__\\**)"""

    employer_contribution_in_cents: Optional[int] = None
    """Employer monthly contribution in cents"""

    employer_id: str
    """Employer ID (empr\\__\\**)"""

    status: EnrollmentStatus
    """
    - `pending` - Pending
    - `enrolled` - Enrolled
    - `waived` - Waived
    - `inactive` - Inactive
    """

    terminated_at: Optional[datetime] = None
    """When coverage was terminated"""

    updated_at: datetime
    """When the enrollment was last updated"""

    sbc_url: Optional[str] = None
    """
    Summary of Benefits and Coverage (SBC) document URL for the enrolled plan; null
    when not on file. Only individual (ICHRA) plans carry an SBC — group plans have
    no SBC on record and always resolve to null.
    """


class EnrollmentRetrieveResponse(BaseModel):
    """Response containing a single enrollment resource."""

    data: Data
    """A single enrollment, including the enrolled plan's documents.

    The plan documents are resolved one enrollment at a time and are therefore not
    part of the list row.
    """
