# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmployerCreateEligibilityPolicyParams"]


class EmployerCreateEligibilityPolicyParams(TypedDict, total=False):
    classification: Required[Literal["FULL_TIME", "PART_TIME", "ALL"]]

    waiting_period: Required[Literal["FIRST_OF_FOLLOWING_MONTH", "THIRTY_DAYS", "SIXTY_DAYS", "NONE"]]

    policy_to_replace_id: str
    """ID of the policy to replace"""
