# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["EnrollmentElectParams", "Election"]


class EnrollmentElectParams(TypedDict, total=False):
    elections: Required[Iterable[Election]]


class Election(TypedDict, total=False):
    decision: Required[Literal["enrolled", "waived"]]

    enrollment_id: Required[str]

    dependent_ids: SequenceNotStr[str]

    plan_id: str
    """Required if decision is enrolled"""
