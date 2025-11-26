# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QualifyingLifeEvent"]


class QualifyingLifeEvent(BaseModel):
    id: str

    event_date: date

    event_type: Literal[
        "MARRIAGE",
        "BIRTH",
        "ADOPTION",
        "DIVORCE",
        "DEATH",
        "JOB_LOSS",
        "REDUCTION_IN_HOURS",
        "EMPLOYER_BANKRUPTCY",
        "MEDICARE_ENTITLEMENT",
        "TERMINATION",
        "OTHER",
    ]

    member_id: str

    status: Literal["PENDING", "APPROVED", "DENIED"]

    description: Optional[str] = None

    proof_document_url: Optional[str] = None

    review_notes: Optional[str] = None

    reviewed_at: Optional[datetime] = None

    reviewed_by_user_id: Optional[str] = None
