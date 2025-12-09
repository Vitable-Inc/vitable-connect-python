# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["BenefitEligibilityPolicy", "Rule"]


class Rule(BaseModel):
    """Individual eligibility rule within a policy."""

    operator: str
    """Comparison operator (e.g., 'equals', 'greater_than', 'in')"""

    rule_type: str
    """
    Type of eligibility rule (e.g., 'employment_status', 'hours_per_week',
    'waiting_period')
    """

    value: object
    """Value to compare against (type depends on rule_type)"""


class BenefitEligibilityPolicy(BaseModel):
    """Serializer for Benefit Eligibility Policy entity.

    Eligibility policies define rules that determine which employees qualify for benefits.
    """

    id: str
    """Unique eligibility policy identifier with 'epol\\__' prefix"""

    active: bool
    """Whether this policy is currently active"""

    created_at: datetime
    """Timestamp when the policy was created"""

    effective_date: date
    """Date when this policy becomes effective"""

    employer_id: str
    """ID of the employer this policy belongs to (empr\\__\\**)"""

    name: str
    """Display name for the eligibility policy"""

    rules: List[Rule]
    """List of eligibility rules that must be satisfied"""

    updated_at: datetime
    """Timestamp when the policy was last updated"""

    description: Optional[str] = None
    """Detailed description of the policy"""

    replaced_policy_id: Optional[str] = None
    """ID of the policy this one replaces, if any (epol\\__\\**)"""
