# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberListDependentsResponse", "Data"]


class Data(BaseModel):
    """Wire serializer for :class:`MemberLegalDependentDTO` (one legal-dependent row)."""

    age: int
    """Dependent's age in years, derived from date of birth"""

    date_of_birth: date
    """Date of birth (YYYY-MM-DD)"""

    first_name: str
    """Dependent's first name"""

    last_name: str
    """Dependent's last name"""

    member_id: str
    """The dependent's own member identifier with 'mbr\\__' prefix"""

    primary_member_id: str
    """The primary member's identifier with 'mbr\\__' prefix"""

    relationship: Literal["Spouse", "Child"]
    """
    - `Spouse` - Spouse
    - `Child` - Child
    """

    sex_at_birth: Optional[Literal["Male", "Female", "Other", "Unknown"]] = None
    """
    - `Male` - Male
    - `Female` - Female
    - `Other` - Other
    - `Unknown` - Unknown
    """


class MemberListDependentsResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of member dependents."""

    data: List[Data]
