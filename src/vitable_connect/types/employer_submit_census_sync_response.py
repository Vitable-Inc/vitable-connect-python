# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["EmployerSubmitCensusSyncResponse", "Data"]


class Data(BaseModel):
    accepted_at: datetime

    employer_id: str


class EmployerSubmitCensusSyncResponse(BaseModel):
    """Response containing a single census sync detail resource."""

    data: Data
