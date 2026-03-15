# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from .sex import Sex
from .._models import BaseModel
from .relationship import Relationship

__all__ = ["Dependent"]


class Dependent(BaseModel):
    """Serializer for Dependent entity in public API responses.

    Dependents are family members (spouse, children) who may be eligible
    for benefit coverage through an employee.
    """

    id: str
    """Unique dependent identifier with 'dpnd\\__' prefix"""

    active_in: bool
    """Whether the dependent is currently active"""

    created_at: datetime
    """Timestamp when the dependent was created"""

    date_of_birth: date
    """Dependent's date of birth (YYYY-MM-DD)"""

    first_name: str
    """Dependent's legal first name"""

    last_name: str
    """Dependent's legal last name"""

    member_id: str
    """ID of the primary member/employee (mbr\\__\\**)"""

    relationship: Relationship
    """
    - `Spouse` - Spouse
    - `Child` - Child
    """

    sex: Sex
    """
    - `Male` - Male
    - `Female` - Female
    - `Other` - Other
    - `Unknown` - Unknown
    """

    updated_at: datetime
    """Timestamp when the dependent was last updated"""

    gender: Optional[str] = None
    """Gender identity, if provided"""

    ssn_last_four: Optional[str] = None
    """Last 4 digits of SSN (masked)"""

    suffix: Optional[str] = None
    """Name suffix (e.g., Jr., Sr., III)"""
