# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Employer", "Address", "Contact"]


class Address(BaseModel):
    """Nested address within EmployerSerializer."""

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


class Contact(BaseModel):
    """
    Primary company-admin contact (email + phone; company admins have no person name).
    """

    email: Optional[str] = None
    """Primary contact email"""

    phone: Optional[str] = None
    """Primary contact phone, or null"""


class Employer(BaseModel):
    """Serializer for Employer entity in public API responses."""

    id: str
    """Unique employer identifier with 'empr\\__' prefix"""

    active: bool
    """Whether the employer is currently active in the system"""

    address: Address
    """Nested address within EmployerSerializer."""

    contact: Optional[Contact] = None
    """
    Primary company-admin contact (email + phone; company admins have no person
    name).
    """

    created_at: datetime
    """Timestamp when the employer was created"""

    ein: Optional[str] = None
    """Employer Identification Number (format: XX-XXXXXXX)"""

    legal_name: str
    """Legal business name for compliance and tax purposes"""

    name: str
    """Display name of the employer"""

    organization_id: Optional[str] = None
    """ID of the parent organization (org\\__\\**)"""

    updated_at: datetime
    """Timestamp when the employer was last updated"""

    email: Optional[str] = None
    """Email address for billing and communications"""

    phone_number: Optional[str] = None
    """Employer phone number (E.164 format recommended)"""

    reference_id: Optional[str] = None
    """Partner-assigned reference ID for the employer"""
