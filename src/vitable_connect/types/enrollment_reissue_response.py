# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EnrollmentReissueResponse", "Data"]


class Data(BaseModel):
    enrollment_id: str
    """Opaque identifier for the new unanswered enrollment"""


class EnrollmentReissueResponse(BaseModel):
    """Response containing a single reissue enrollment resource."""

    data: Data
