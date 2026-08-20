# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MemberListResponse", "Address"]


class Address(BaseModel):
    """Member's residential address"""

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


class MemberListResponse(BaseModel):
    """
    A member in the organization's directory: identity, contact details, address, and join date.
    """

    id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    first_name: str
    """Member's legal first name"""

    last_name: str
    """Member's legal last name"""

    address: Optional[Address] = None
    """Member's residential address"""

    email: Optional[str] = None
    """Email address"""

    phone: Optional[str] = None
    """Phone number (10-digit US domestic string)"""
