# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["AuthListPersonasResponse", "AuthListPersonasResponseItem"]


class AuthListPersonasResponseItem(BaseModel):
    display_name: str

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


AuthListPersonasResponse: TypeAlias = List[AuthListPersonasResponseItem]
