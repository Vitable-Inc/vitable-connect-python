# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EmployerSubmitPayrollAccessSetupResponse", "Data"]


class Data(BaseModel):
    completed: bool

    submitted_at: Optional[datetime] = None


class EmployerSubmitPayrollAccessSetupResponse(BaseModel):
    """Response containing a single payroll access setup status resource."""

    data: Data
