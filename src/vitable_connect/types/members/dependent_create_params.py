# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .relationship import Relationship
from ..employers.sex import Sex

__all__ = ["DependentCreateParams"]


class DependentCreateParams(TypedDict, total=False):
    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date of birth (YYYY-MM-DD)"""

    first_name: Required[str]
    """Dependent's legal first name"""

    last_name: Required[str]
    """Dependent's legal last name"""

    relationship: Required[Relationship]
    """
    - `Spouse` - Spouse
    - `Child` - Child
    """

    sex: Required[Sex]
    """
    - `Male` - Male
    - `Female` - Female
    - `Other` - Other
    - `Unknown` - Unknown
    """

    gender: Optional[str]
    """Gender identity"""

    ssn: Optional[str]
    """Social Security Number (optional, XXX-XX-XXXX or XXXXXXXXX)"""

    suffix: Optional[str]
    """Name suffix (Jr., Sr., III)"""
