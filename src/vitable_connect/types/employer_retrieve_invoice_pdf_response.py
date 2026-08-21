# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmployerRetrieveInvoicePdfResponse", "Data"]


class Data(BaseModel):
    download_url: str
    """Time-limited Chargebee PDF download link for the invoice."""


class EmployerRetrieveInvoicePdfResponse(BaseModel):
    """Response containing a single employer invoice pdf resource."""

    data: Data
