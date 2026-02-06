# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EnrollmentReissueParams"]


class EnrollmentReissueParams(TypedDict, total=False):
    qle_id: Required[str]
    """ID of the qualifying life event (qle\\__\\**)"""

    reason: Optional[str]
    """Optional reason for reissue"""
