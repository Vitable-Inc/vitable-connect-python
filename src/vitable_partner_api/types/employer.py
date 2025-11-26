# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .eligibility_policy import EligibilityPolicy

__all__ = ["Employer"]


class Employer(BaseModel):
    id: str

    active: bool

    legal_name: str

    name: str

    eligibility_policy: Optional[EligibilityPolicy] = None

    organization_id: Optional[str] = None
