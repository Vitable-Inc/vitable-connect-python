# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmployerCreateParams", "Address"]


class EmployerCreateParams(TypedDict, total=False):
    address: Required[Address]
    """Employer address"""

    ein: Required[str]
    """Employer Identification Number (format: XX-XXXXXXX or XXXXXXXXX)"""

    legal_name: Required[str]
    """Legal business name"""

    name: Required[str]
    """Employer display name"""


class Address(TypedDict, total=False):
    """Employer address"""

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
