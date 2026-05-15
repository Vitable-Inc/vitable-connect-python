# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str

    created_at: Optional[datetime] = None

    external_reference_id: str

    name: str

    organization_id: str

    updated_at: Optional[datetime] = None
