# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel
from .employee_class import EmployeeClass
from .enrollment_status import EnrollmentStatus

__all__ = ["Employee", "Enrollment", "Address"]


class Enrollment(BaseModel):
    id: str
    """Unique enrollment identifier with 'enrl\\__' prefix"""

    status: EnrollmentStatus
    """
    - `pending` - Pending
    - `enrolled` - Enrolled
    - `waived` - Waived
    - `inactive` - Inactive
    """

    answered_at: Optional[datetime] = None
    """Timestamp when the enrollment decision was made"""


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

    created_at: datetime
    """Timestamp when the employee was created"""

    date_of_birth: date
    """Date of birth (YYYY-MM-DD)"""

    email: str
    """Email address"""

    enrollments: List[Enrollment]
    """Benefit enrollments for this employee"""

    first_name: str
    """Employee's legal first name"""

    last_name: str
    """Employee's legal last name"""

    member_id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    status: str
    """Employee status (active or terminated)"""

    updated_at: datetime
    """Timestamp when the employee was last updated"""

    address: Optional[Address] = None
    """Employee's residential address"""

    employee_class: Optional[EmployeeClass] = None
    """
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Intern` - Intern
    - `Seasonal` - Seasonal
    - `Individual Contractor` - Individual Contractor
    """

    gender: Optional[str] = None
    """Gender identity, if provided"""

    hire_date: Optional[date] = None
    """Employee's hire date with the employer"""

    phone: Optional[str] = None
    """Phone number (10-digit US domestic string)"""

    reference_id: Optional[str] = None
    """Partner-assigned reference ID for the employee"""

    suffix: Optional[str] = None
    """Name suffix (e.g., Jr., Sr., III)"""

    termination_date: Optional[date] = None
    """Employee's termination date, if terminated"""
