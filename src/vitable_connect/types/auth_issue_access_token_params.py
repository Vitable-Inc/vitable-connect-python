# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthIssueAccessTokenParams", "BoundEntity"]


class AuthIssueAccessTokenParams(TypedDict, total=False):
    grant_type: Required[Literal["client_credentials"]]
    """- `client_credentials` - client_credentials"""

    bound_entity: Optional[BoundEntity]
    """Optional entity to bind the token to for scoped access"""


class BoundEntity(TypedDict, total=False):
    """Optional entity to bind the token to for scoped access"""

    id: Required[str]
    """
    Prefixed entity ID to bind the token to (empr*\\** for employer, empl*\\** for
    employee)
    """

    type: Required[Literal["employer", "employee"]]
    """
    - `employer` - employer
    - `employee` - employee
    """
