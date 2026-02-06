# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..employee import Employee

__all__ = ["EmployeeCreateResponse"]


class EmployeeCreateResponse(BaseModel):
    """Response containing a single employee resource."""

    data: Employee
    """Serializer for Employee entity in public API responses.

    Note: Employee is in the company module but exposed via account public API.
    Contains nested MemberEntity with personal identity information.
    """
