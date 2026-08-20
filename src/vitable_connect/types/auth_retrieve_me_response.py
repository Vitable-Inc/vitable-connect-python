# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthRetrieveMeResponse", "User"]


class User(BaseModel):
    """The authenticated IdP identity — no persona (no base_user_id / user_type)."""

    email: str

    first_name: Optional[str] = None

    idp_provider: str

    idp_user_id: str

    last_name: Optional[str] = None


class AuthRetrieveMeResponse(BaseModel):
    user: User
    """The authenticated IdP identity — no persona (no base_user_id / user_type)."""
