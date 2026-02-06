# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .dependent import Dependent

__all__ = ["DependentResponse"]


class DependentResponse(BaseModel):
    """Response containing a single dependent resource."""

    data: Dependent
    """Serializer for Dependent entity in public API responses.

    Dependents are family members (spouse, children) who may be eligible for benefit
    coverage through an employee.
    """
