# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberRetrieveResponse", "Data", "DataAddress"]


class DataAddress(BaseModel):
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


class Data(BaseModel):
    """
    A member's profile: identity, contact details, address, demographics, and onboarding status.
    """

    id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    age: int
    """Member's age in years, derived from date of birth"""

    date_of_birth: date
    """Date of birth (YYYY-MM-DD)"""

    first_name: str
    """Member's legal first name"""

    last_name: str
    """Member's legal last name"""

    name: str
    """Member's full name"""

    status: Literal["onboarded", "pending_onboarding"]
    """Member profile status (onboarded or pending onboarding)"""

    address: Optional[DataAddress] = None
    """Member's residential address"""

    email: Optional[str] = None
    """Email address"""

    phone: Optional[str] = None
    """Phone number (10-digit US domestic string)"""

    preferred_language: Optional[str] = None
    """Member's preferred language code (e.g., en, es)"""

    sex_at_birth: Optional[str] = None
    """Sex assigned at birth, if provided"""

    tobacco_status: Optional[bool] = None
    """Whether the member uses tobacco, if known"""


class MemberRetrieveResponse(BaseModel):
    """Response containing a single member resource."""

    data: Data
    """
    A member's profile: identity, contact details, address, demographics, and
    onboarding status.
    """
