# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .employer import Employer

__all__ = ["EmployerRetrieveResponse"]


class EmployerRetrieveResponse(BaseModel):
    """Response containing a single employer resource."""

    data: Employer
    """Serializer for Employer entity in public API responses."""
