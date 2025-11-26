# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel
from .benefit_product import BenefitProduct
from .benefit_products.plan_cost import PlanCost
from .benefit_products.plan_contribution_class import PlanContributionClass

__all__ = ["PlanYear"]


class PlanYear(BaseModel):
    id: str

    benefit_product: BenefitProduct

    configured: bool

    coverage_end_date: date

    coverage_start_date: date

    employer_id: str

    open_enrollment_end_date: date

    open_enrollment_start_date: date

    contribution_classes: Optional[List[PlanContributionClass]] = None

    plan_costs: Optional[List[PlanCost]] = None
