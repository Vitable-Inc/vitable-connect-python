# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EmployerRetrievePayrollAccessSetupResponse", "Data"]


class Data(BaseModel):
    completed: bool

    submitted_at: Optional[datetime] = None


class EmployerRetrievePayrollAccessSetupResponse(BaseModel):
    """Response containing a single payroll access setup status resource."""

    data: Data
