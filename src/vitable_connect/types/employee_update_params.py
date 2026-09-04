# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .employee_class import EmployeeClass

__all__ = ["EmployeeUpdateParams", "Address"]


class EmployeeUpdateParams(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """
    Past or present date applied to each tracked employment field included in this
    request
    """

    address: Optional[Address]
    """Employee's residential address"""

    compensation_type: Optional[Literal["Salary", "Hourly"]]
    """
    - `Salary` - Salary
    - `Hourly` - Hourly
    """

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

    gender: Optional[Literal["Male", "Female", "Transgender", "Non-binary", "Prefer not to respond"]]
    """
    - `Male` - Male
    - `Female` - Female
    - `Transgender` - Transgender
    - `Non-binary` - Non Binary
    - `Prefer not to respond` - Prefer Not To Respond
    """

    phone: Optional[str]
    """Phone number"""

    start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Employment start date"""


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
