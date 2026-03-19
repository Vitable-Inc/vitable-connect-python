# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .benefit_eligibility_policy import BenefitEligibilityPolicy

__all__ = ["BenefitEligibilityPolicyResponse"]


class BenefitEligibilityPolicyResponse(BaseModel):
    """Response containing a single benefit eligibility policy resource."""

    data: BenefitEligibilityPolicy
