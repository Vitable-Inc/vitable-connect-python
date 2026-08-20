# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AuthSignUpParams"]


class AuthSignUpParams(TypedDict, total=False):
    user_type: Optional[
        Literal[
            "Member",
            "NursePractitioner",
            "CompanyAdmin",
            "VitableAdmin",
            "ClinicalAdmin",
            "PartnerEmployee",
            "OrganizationUser",
            "ExternalAdmin",
        ]
    ]
    """
    - `Member` - Member
    - `NursePractitioner` - NursePractitioner
    - `CompanyAdmin` - CompanyAdmin
    - `VitableAdmin` - VitableAdmin
    - `ClinicalAdmin` - ClinicalAdmin
    - `PartnerEmployee` - PartnerEmployee
    - `OrganizationUser` - OrganizationUser
    - `ExternalAdmin` - ExternalAdmin
    """
