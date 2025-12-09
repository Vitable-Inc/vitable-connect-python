# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .employers.employee_class import EmployeeClass

__all__ = ["EmployeeUpdateParams", "Address"]


class EmployeeUpdateParams(TypedDict, total=False):
    address: Optional[Address]
    """Employee's residential address"""

    email: Optional[str]
    """Email address"""

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

    termination_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Termination date if terminating"""


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
