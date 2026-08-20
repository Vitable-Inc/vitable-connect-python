# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthLoginParams"]


class AuthLoginParams(TypedDict, total=False):
    email_or_phone: Required[str]

    user_type: Required[
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
    - `NursePractitioner` - Provider
    - `CompanyAdmin` - Company Admin
    - `VitableAdmin` - Vitable Admin
    - `ClinicalAdmin` - Clinical Admin
    - `PartnerEmployee` - Partner Employee
    - `OrganizationUser` - Organization User
    - `ExternalAdmin` - External Admin
    """

    app_name: str

    app_version: str

    password: str

    two_factor_token: str
