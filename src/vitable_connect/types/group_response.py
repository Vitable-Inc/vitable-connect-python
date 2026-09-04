# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .group import Group
from .._models import BaseModel

__all__ = ["GroupResponse"]


class GroupResponse(BaseModel):
    """Response containing a single group resource."""

    data: Group
