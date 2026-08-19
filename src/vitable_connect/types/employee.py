# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .employee_class import EmployeeClass

__all__ = ["Employee", "Deduction", "Address"]


class Deduction(BaseModel):
    benefit_name: str
    """Name of the benefit plan"""

    deduction_amount_in_cents: int
    """Employee deduction amount in cents"""

    deduction_category: Optional[str] = None
    """Deduction category (reserved for future use)"""

    frequency: Literal["weekly", "bi_weekly", "semi_monthly", "monthly"]
    """
    - `weekly` - Weekly
    - `bi_weekly` - Bi Weekly
    - `semi_monthly` - Semi Monthly
    - `monthly` - Monthly
    """

    period_end_date: date
    """Period end date (YYYY-MM-DD)"""

    period_start_date: date
    """Period start date (YYYY-MM-DD)"""

    tax_classification: Literal["Unknown", "Pre-tax", "Post-tax"]
    """
    - `Unknown` - Unknown
    - `Pre-tax` - Pre Tax
    - `Post-tax` - Post Tax
    """


class Address(BaseModel):
    """Employee's residential address"""

    address_line_1: str
    """Primary street address"""

    city: str
    """City name"""

    state: str
    """Two-letter state code (e.g., CA, NY)"""

    zipcode: str
    """ZIP code (5 or 9 digit)"""

    address_line_2: Optional[str] = None
    """Secondary street address (apt, suite, etc.)"""


class Employee(BaseModel):
    id: str
    """Unique employee identifier with 'empl\\__' prefix"""

    classification_effective_date: date
    """Date the employee's current classification took effect"""

    compensation_type: Optional[Literal["Salary", "Hourly"]] = None
    """
    - `Salary` - Salary
    - `Hourly` - Hourly
    """

    compensation_type_effective_date: date
    """Date the employee's current compensation type took effect"""

    created_at: datetime
    """Timestamp when the employee was created"""

    date_of_birth: date
    """Date of birth (YYYY-MM-DD)"""

    deductions: List[Deduction]
    """Payroll deductions from the most recent statement period.

    Replaced when a new statement is generated.
    """

    email: str
    """Email address"""

    employee_class: EmployeeClass
    """
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Intern` - Intern
    - `Seasonal` - Seasonal
    - `Individual Contractor` - Individual Contractor
    """

    employer_id: str
    """Unique identifier of the employer this employment is with (empr\\__\\**)"""

    first_name: str
    """Employee's legal first name"""

    last_name: str
    """Employee's legal last name"""

    member_id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    phone: Optional[str] = None
    """Phone number (10-digit US domestic string)"""

    start_date: date
    """Employee's start date with the employer"""

    status: Literal["active", "terminated"]
    """Employee status (active or terminated)"""

    updated_at: datetime
    """Timestamp when the employee was last updated"""

    address: Optional[Address] = None
    """Employee's residential address"""

    employer_name: Optional[str] = None
    """Name of the employer this employment is with"""

    gender: Optional[str] = None
    """Gender identity, if provided"""

    reference_id: Optional[str] = None
    """Partner-assigned reference ID for the employee"""

    suffix: Optional[str] = None
    """Name suffix (e.g., Jr., Sr., III)"""

    termination_date: Optional[date] = None
    """Employee's termination date, if terminated"""
