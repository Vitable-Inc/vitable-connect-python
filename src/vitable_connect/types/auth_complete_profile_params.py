# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthCompleteProfileParams"]


class AuthCompleteProfileParams(TypedDict, total=False):
    first_name: Required[str]

    last_name: Required[str]

    phone: Required[str]

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
