# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmployerCreateBenefitEligibilityPolicyParams"]


class EmployerCreateBenefitEligibilityPolicyParams(TypedDict, total=False):
    classification: Required[str]
    """Which employee classifications are eligible. One of: full_time, part_time, all"""

    waiting_period: Required[str]
    """Waiting period before eligibility.

    One of: first_of_following_month, 30_days, 60_days, none
    """
