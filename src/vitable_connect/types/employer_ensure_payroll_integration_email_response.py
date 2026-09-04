# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmployerEnsurePayrollIntegrationEmailResponse", "Data"]


class Data(BaseModel):
    integration_email: str


class EmployerEnsurePayrollIntegrationEmailResponse(BaseModel):
    """Response containing a single payroll integration email resource."""

    data: Data
