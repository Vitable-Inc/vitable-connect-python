# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Employer", "Address"]


class Address(BaseModel):
    city: str
    """City name"""

    state: str
    """Two-letter state code (e.g., CA, NY)"""

    street_1: str
    """Primary street address"""

    zip_code: str
    """ZIP code (5 or 9 digit)"""

    country: Optional[str] = None
    """Country code (default: US)"""

    street_2: Optional[str] = None
    """Secondary street address (apt, suite, etc.)"""


class Employer(BaseModel):
    id: str
    """Unique employer identifier with 'empr\\__' prefix"""

    active: bool
    """Whether the employer is currently active in the system"""

    created_at: datetime
    """Timestamp when the employer was created"""

    legal_name: str
    """Legal business name for compliance and tax purposes"""

    name: str
    """Display name of the employer"""

    organization_id: str
    """ID of the parent organization (org\\__\\**)"""

    updated_at: datetime
    """Timestamp when the employer was last updated"""

    address: Optional[Address] = None
    """Nested address within EmployerSerializer."""

    ein: Optional[str] = None
    """Employer Identification Number (masked in responses)"""

    eligibility_policy_id: Optional[str] = None
    """ID of the benefit eligibility policy (epol\\__\\**), if assigned"""
