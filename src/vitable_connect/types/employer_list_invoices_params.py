# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["EmployerListInvoicesParams"]


class EmployerListInvoicesParams(TypedDict, total=False):
    limit: int
    """Maximum number of invoices per page"""

    offset: Optional[str]
    """Opaque cursor from a previous page's next_offset"""
