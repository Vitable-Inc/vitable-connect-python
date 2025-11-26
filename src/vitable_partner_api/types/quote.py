# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Quote"]


class Quote(BaseModel):
    benefit_product_id: str

    employer_id: str

    total_cost_in_cents: int

    breakdown: Optional[Dict[str, object]] = None
