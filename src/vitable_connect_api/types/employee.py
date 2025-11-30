# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from .sex import Sex
from .._models import BaseModel
from .employers.employee_class import EmployeeClass

__all__ = ["Employee", "Member", "Address"]


class Member(BaseModel):
    id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    date_of_birth: date
    """Member's date of birth (YYYY-MM-DD)"""

    first_name: str
    """Member's legal first name"""

    last_name: str
    """Member's legal last name"""

    sex: Sex
    """
    - `Male` - Male
    - `Female` - Female
    - `Other` - Other
    - `Unknown` - Unknown
    """

    email: Optional[str] = None
    """Email address for communications"""

    gender: Optional[str] = None
    """Gender identity, if provided"""

    phone: Optional[str] = None
    """Phone number"""

    suffix: Optional[str] = None
    """Name suffix (e.g., Jr., Sr., III)"""


class Address(BaseModel):
    city: str
    """City name"""

    state: str
    """Two-letter state code"""

    street_1: str
    """Primary street address"""

    zip_code: str
    """ZIP code"""

    country: Optional[str] = None
    """Country code"""

    street_2: Optional[str] = None
    """Secondary street address"""


class Employee(BaseModel):
    id: str
    """Unique employee identifier with 'empl\\__' prefix"""

    active: bool
    """Whether the employee is currently active"""

    created_at: datetime
    """Timestamp when the employee was created"""

    employer_id: str
    """ID of the employer this employee works for (empr\\__\\**)"""

    member: Member
    """Nested member entity containing personal identity information.

    Matches MemberEntity from account module domain.
    """

    start_date: date
    """Employee's start/hire date with the employer"""

    updated_at: datetime
    """Timestamp when the employee was last updated"""

    address: Optional[Address] = None
    """Nested address for employee."""

    employee_class: Optional[EmployeeClass] = None
    """
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Intern` - Intern
    - `Seasonal` - Seasonal
    - `Individual Contractor` - Individual Contractor
    """

    termination_date: Optional[date] = None
    """Employee's termination date, if terminated"""
