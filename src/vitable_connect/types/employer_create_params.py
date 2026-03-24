# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EmployerCreateParams", "Address"]


class EmployerCreateParams(TypedDict, total=False):
    address: Required[Address]
    """Employer address"""

    ein: Required[str]
    """Employer Identification Number (format: XX-XXXXXXX)"""

    email: Required[str]
    """Email address for billing and communications"""

    legal_name: Required[str]
    """Legal business name"""

    name: Required[str]
    """Employer display name"""

    phone_number: Optional[str]
    """Employer phone number (10-digit US format, e.g. 5551234567)"""

    reference_id: Optional[str]
    """External reference ID for this employer"""


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
