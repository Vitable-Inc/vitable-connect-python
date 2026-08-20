# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberRetrieveHouseholdResponse", "Data"]


class Data(BaseModel):
    """Wire serializer for :class:`HouseholdMemberDTO` (one household participant)."""

    date_of_birth: date
    """Date of birth (YYYY-MM-DD)"""

    first_name: str
    """Household member's first name"""

    household_admin_in: bool
    """Whether this participant is a household admin (the account holder always is)"""

    last_name: str
    """Household member's last name"""

    member_id: str
    """Member identifier with 'mbr\\__' prefix"""

    member_type: Literal["Account Holder", "Dependent", "Inactive"]
    """
    - `Account Holder` - Account Holder
    - `Dependent` - Dependent
    - `Inactive` - Inactive
    """

    relationship: Optional[Literal["Child", "Spouse", "Roommate", "Other"]] = None
    """
    - `Child` - Child
    - `Spouse` - Spouse
    - `Roommate` - Roommate
    - `Other` - Other
    """


class MemberRetrieveHouseholdResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of the members of a member's household."""

    data: List[Data]
