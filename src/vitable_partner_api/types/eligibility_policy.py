# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EligibilityPolicy"]


class EligibilityPolicy(BaseModel):
    id: str

    active: bool

    classification: Literal["FULL_TIME", "PART_TIME", "ALL"]

    employer_id: str

    waiting_period: Literal["FIRST_OF_FOLLOWING_MONTH", "THIRTY_DAYS", "SIXTY_DAYS", "NONE"]

    archived_at: Optional[datetime] = None

    replaces_policy_id: Optional[str] = None
