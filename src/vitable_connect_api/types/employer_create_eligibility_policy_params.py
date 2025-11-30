# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployerCreateEligibilityPolicyParams", "Rule"]


class EmployerCreateEligibilityPolicyParams(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date when policy becomes effective"""

    name: Required[str]
    """Display name for the policy"""

    rules: Required[Iterable[Rule]]
    """List of eligibility rules (at least one required)"""

    policy_to_replace_id: str
    """ID of existing policy to replace (epol\\__\\**)"""

    description: Optional[str]
    """Detailed description"""


class Rule(TypedDict, total=False):
    operator: Required[str]
    """Comparison operator"""

    rule_type: Required[str]
    """Type of eligibility rule"""

    value: Required[str]
    """Value to compare against (can be string, number, boolean, or list)"""
