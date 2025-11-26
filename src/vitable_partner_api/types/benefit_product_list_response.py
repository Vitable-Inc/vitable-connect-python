# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .benefit_product import BenefitProduct

__all__ = ["BenefitProductListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    offset: int

    total: int


class BenefitProductListResponse(BaseModel):
    data: Optional[List[BenefitProduct]] = None

    pagination: Optional[Pagination] = None
