# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["EmployerListHRISProvidersResponse", "Data"]


class Data(BaseModel):
    provider: str
    """HRIS/payroll provider id, as stored on the connection (e.g.

    `adp_run`). Filter with this.
    """

    provider_label: str
    """Display name of that provider (e.g. `ADP Run`)."""


class EmployerListHRISProvidersResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of organization hris providers."""

    data: List[Data]
