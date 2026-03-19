# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["BenefitEligibilityPolicy"]


class BenefitEligibilityPolicy(BaseModel):
    id: str

    active: bool

    classification: str

    created_at: datetime

    employer_id: str

    updated_at: datetime

    waiting_period: str
