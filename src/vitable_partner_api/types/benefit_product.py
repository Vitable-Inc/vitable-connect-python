# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .plan import Plan
from .._models import BaseModel

__all__ = ["BenefitProduct"]


class BenefitProduct(BaseModel):
    id: str

    name: str

    product_type: str

    plans: Optional[List[Plan]] = None
