# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EmployerRetrieveHRISResponse", "HRIS"]


class HRIS(BaseModel):
    """HRIS connection details, or null when the employer has no integration."""

    last_sync_on: Optional[datetime] = None
    """When the last sync completed, or null when none has."""

    provider: str
    """HRIS/payroll provider the employer is connected to (e.g. `Paychex`)."""

    status: str
    """Connection status reported by the integration."""

    synced_row_count: Optional[int] = None
    """Rows in the latest completed sync, or null when none has."""


class EmployerRetrieveHRISResponse(BaseModel):
    hris: Optional[HRIS] = None
    """HRIS connection details, or null when the employer has no integration."""
