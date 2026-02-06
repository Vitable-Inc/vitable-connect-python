# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .category import Category
from .product_code import ProductCode

__all__ = ["BenefitProductListParams"]


class BenefitProductListParams(TypedDict, total=False):
    active_in: bool
    """Filter by active status"""

    category: Category
    """Filter by product category"""

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    product_code: ProductCode
    """Filter by product code"""
