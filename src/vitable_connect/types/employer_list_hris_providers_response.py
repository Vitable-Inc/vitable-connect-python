# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["EmployerListHRISProvidersResponse", "Data"]


class Data(BaseModel):
    provider: str
    """HRIS/payroll provider name, as stored on the connection (e.g. `ADP RUN`)."""


class EmployerListHRISProvidersResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of organization hris providers."""

    data: List[Data]
