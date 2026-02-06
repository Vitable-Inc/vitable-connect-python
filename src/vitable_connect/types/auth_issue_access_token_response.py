# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .type import Type
from .._models import BaseModel

__all__ = ["AuthIssueAccessTokenResponse", "BoundEntity"]


class BoundEntity(BaseModel):
    """Entity the token is bound to, if any"""

    id: str
    """Prefixed entity ID the token is bound to (empr*\\** or empl*\\**)"""

    type: Type
    """
    - `employer` - employer
    - `employee` - employee
    """


class AuthIssueAccessTokenResponse(BaseModel):
    access_token: str
    """The issued access token (vit*at*\\**)"""

    expires_in: int
    """Token lifetime in seconds"""

    token_type: str
    """Token type, always 'Bearer'"""

    bound_entity: Optional[BoundEntity] = None
    """Entity the token is bound to, if any"""
