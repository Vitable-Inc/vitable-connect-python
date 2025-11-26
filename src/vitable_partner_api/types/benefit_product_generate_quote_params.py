# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["BenefitProductGenerateQuoteParams"]


class BenefitProductGenerateQuoteParams(TypedDict, total=False):
    employer_id: Required[str]

    metadata: Dict[str, object]
    """Additional metadata for quote generation"""
