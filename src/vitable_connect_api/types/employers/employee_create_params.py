# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..sex import Sex
from ..._utils import PropertyInfo
from .employee_class import EmployeeClass

__all__ = ["EmployeeCreateParams", "Address"]


class EmployeeCreateParams(TypedDict, total=False):
    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date of birth (YYYY-MM-DD)"""

    email: Required[str]
    """Email address"""

    first_name: Required[str]
    """Employee's legal first name"""

    last_name: Required[str]
    """Employee's legal last name"""

    sex: Required[Sex]
    """
    - `Male` - Male
    - `Female` - Female
    - `Other` - Other
    - `Unknown` - Unknown
    """

    ssn: Required[str]
    """Social Security Number (XXX-XX-XXXX or XXXXXXXXX). Only accepted on create."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Employment start/hire date"""

    address: Optional[Address]
    """Employee's residential address"""

    employee_class: Optional[EmployeeClass]
    """
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Intern` - Intern
    - `Seasonal` - Seasonal
    - `Individual Contractor` - Individual Contractor
    """

    gender: Optional[str]
    """Gender identity"""

    phone: Optional[str]
    """Phone number"""

    suffix: Optional[str]
    """Name suffix (Jr., Sr., III)"""


class Address(TypedDict, total=False):
    """Employee's residential address"""

    city: Required[str]
    """City name"""

    state: Required[str]
    """Two-letter state code"""

    street_1: Required[str]
    """Primary street address"""

    zip_code: Required[str]
    """ZIP code"""

    country: str
    """Country code"""

    street_2: Optional[str]
    """Secondary street address"""
