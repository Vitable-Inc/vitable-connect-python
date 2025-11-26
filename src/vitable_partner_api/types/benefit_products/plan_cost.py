# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PlanCost"]


class PlanCost(BaseModel):
    dependent_cost_in_cents: int

    employee_cost_in_cents: int

    plan_id: str

    plan_year_id: str
