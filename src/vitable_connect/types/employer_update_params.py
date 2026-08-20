# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmployerUpdateParams", "Address"]


class EmployerUpdateParams(TypedDict, total=False):
    active: Optional[bool]
    """Whether the employer is active"""

    address: Optional[Address]
    """Employer address"""

    legal_name: Optional[str]
    """Legal business name"""

    name: Optional[str]
    """Employer display name"""


class Address(TypedDict, total=False):
    """Employer address"""

    address_line_1: Required[str]
    """Primary street address"""

    city: Required[str]
    """City name"""

    state: Required[str]
    """Two-letter state code"""

    zipcode: Required[str]
    """ZIP code"""

    address_line_2: Optional[str]
    """Secondary street address"""
