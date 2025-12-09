# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .category import Category
from .product_code import ProductCode

__all__ = ["BenefitProductListResponse", "BenefitProductListResponseItem"]


class BenefitProductListResponseItem(BaseModel):
    """Serializer for Benefit Product entity in public API responses.

    Benefit Products represent types of benefits (dental, vision, medical, etc.)
    that an Organization can offer to their Employers.
    """

    id: str
    """Unique benefit product identifier with 'bprd\\__' prefix"""

    active: bool
    """Whether this product is currently available for offering"""

    category: Category
    """
    - `Medical` - Medical
    - `Dental` - Dental
    - `Vision` - Vision
    - `Hospital` - Hospital
    """

    created_at: datetime
    """Timestamp when the product was created"""

    name: str
    """Display name of the benefit product"""

    product_code: ProductCode
    """
    - `EBA` - Eba Mec
    - `VPC` - Vpc Enhanced
    - `VPC_CORE` - Vpc Core
    - `MEC` - Vpc Mec
    - `MEC2` - Mec2
    - `MEC_PLUS` - Mec Plus
    - `MVP` - Mvp
    - `MVP2` - Mvp2
    - `MVPSL` - Mvpsl
    - `MVPSL2` - Mvpsl2
    - `VD` - Dental
    - `VV` - Vision
    - `ICHRA` - Ichra
    - `ICHRA_PREMIUM_PLUS` - Ichra Premium Plus
    - `ICHRA_REIMBURSEMENT_ONLY` - Ichra Reimbursement Only
    """

    updated_at: datetime
    """Timestamp when the product was last updated"""

    carrier_name: Optional[str] = None
    """Name of the insurance carrier providing this product"""

    description: Optional[str] = None
    """Detailed description of the benefit product"""


BenefitProductListResponse: TypeAlias = List[BenefitProductListResponseItem]
