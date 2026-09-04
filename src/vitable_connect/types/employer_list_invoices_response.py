# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EmployerListInvoicesResponse", "Data", "Pagination"]


class Data(BaseModel):
    invoice_id: str
    """Chargebee invoice id (external id, not a prefixed UUID)."""

    period: Optional[str] = None
    """Invoice date as an ISO string, or null."""

    status: Optional[str] = None
    """Chargebee invoice status (e.g. `paid`), or null."""

    total: Optional[float] = None
    """Invoice total in dollars, or null."""


class Pagination(BaseModel):
    next_offset: Optional[str] = None
    """
    Opaque JSON-encoded cursor for the next page; null when there are no more pages.
    """


class EmployerListInvoicesResponse(BaseModel):
    """
    Cursor-paginated invoices envelope: ``{ "data": [...], "pagination": { "next_offset": ... } }``.
    """

    data: List[Data]

    pagination: Pagination
