# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .enrollment import Enrollment

__all__ = ["EnrollmentRetrieveResponse"]


class EnrollmentRetrieveResponse(BaseModel):
    """Response containing a single enrollment resource."""

    data: Enrollment
    """Serializer for Enrollment entity in public API responses.

    An Enrollment represents an employee's benefit enrollment for a specific plan
    year.
    """
