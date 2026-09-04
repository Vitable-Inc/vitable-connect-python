# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .employee import Employee

__all__ = ["EmployeeRetrieveResponse"]


class EmployeeRetrieveResponse(BaseModel):
    """Response containing a single employee resource."""

    data: Employee
