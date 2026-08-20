# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthCompleteProfileResponse", "User"]


class User(BaseModel):
    base_user_id: str

    email: str

    first_name: Optional[str] = None

    idp_provider: Literal["workos", "vitable"]
    """
    - `workos` - WorkOS
    - `vitable` - Vitable
    """

    idp_user_id: str

    last_name: Optional[str] = None

    phone: Optional[str] = None

    user_type: Literal[
        "Member",
        "NursePractitioner",
        "CompanyAdmin",
        "VitableAdmin",
        "ClinicalAdmin",
        "PartnerEmployee",
        "OrganizationUser",
        "ExternalAdmin",
    ]
    """
    - `Member` - Member
    - `NursePractitioner` - Provider
    - `CompanyAdmin` - Company Admin
    - `VitableAdmin` - Vitable Admin
    - `ClinicalAdmin` - Clinical Admin
    - `PartnerEmployee` - Partner Employee
    - `OrganizationUser` - Organization User
    - `ExternalAdmin` - External Admin
    """


class AuthCompleteProfileResponse(BaseModel):
    user: User
