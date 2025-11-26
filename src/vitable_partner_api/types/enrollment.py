# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Enrollment"]


class Enrollment(BaseModel):
    id: str

    decision: Literal["enrolled", "waived"]

    employee_id: str

    plan_year_id: str

    status: Literal["pending", "enrolled", "waived", "inactive"]
