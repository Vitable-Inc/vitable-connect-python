# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "EmployerRetrieveBenefitPlanYearResponse",
    "Data",
    "DataContributionStrategy",
    "DataContributionStrategyContributionTier",
    "DataContributionStrategyIchraContributionClass",
    "DataEligibilityPolicy",
    "DataEligibilityPolicyRule",
    "DataEligibilityPolicyRuleEligibleGeographicalLocation",
    "DataEmployeeContribution",
    "DataEmployerContribution",
    "DataEnrollmentRate",
]


class DataContributionStrategyContributionTier(BaseModel):
    """
    One non-ICHRA coverage tier, mirroring the internal configuration ``CompanyBenefitPlanTierCostDTO``
    minus the tier-cost id, ``pepm`` and ``pepm_per_dependent``; ``benefit_plan_id`` is the prefixed
    ``bpln_*`` form rather than a raw UUID.
    """

    benefit_plan_id: str
    """Prefixed benefit-plan identifier (`bpln_*`)."""

    benefit_plan_name: str
    """Benefit plan name."""

    benefit_plan_tier_name: str
    """Coverage-tier name."""

    cost: int
    """Monthly employee deduction in cents."""

    cost_per_dependent: int
    """Monthly employee deduction per dependent, in cents."""

    dependents_required_in: bool
    """Whether dependents are required for this tier."""

    spouse_required_in: bool
    """Whether a spouse is required for this tier."""


class DataContributionStrategyIchraContributionClass(BaseModel):
    """
    One ICHRA contribution class, mirroring the internal configuration endpoint's
    ``IchraContributionClassConfigurationEntitySerializer`` field-for-field. Two deliberate
    differences for the public surface: the identifier is the opaque prefixed ``iccl_*`` form rather
    than a raw UUID, and the matcher choices come from the domain enums rather than the model's.
    """

    amount_in_cents: int
    """Monthly allowance in cents."""

    compensation: Literal["Unspecified", "Salary", "Hourly"]
    """
    - `Unspecified` - Unspecified
    - `Salary` - Salary
    - `Hourly` - Hourly
    """

    contribution_class_id: str
    """Prefixed contribution-class identifier (`iccl_*`)."""

    employment: Literal["Unspecified", "Full Time", "Part Time", "Temporary", "Seasonal"]
    """
    - `Unspecified` - Unspecified
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Seasonal` - Seasonal
    """

    family_status: Literal["Unspecified", "EE", "ES", "EC", "EF"]
    """
    - `Unspecified` - Unspecified
    - `EE` - Ee
    - `ES` - Es
    - `EC` - Ec
    - `EF` - Ef
    """

    location: Literal["Unspecified", "State"]
    """
    - `Unspecified` - Unspecified
    - `State` - State
    """

    location_value: Optional[str] = None
    """Location matcher value (CSV of state codes), or null."""

    max_age: Optional[int] = None
    """Age-band upper bound, or null."""

    min_age: Optional[int] = None
    """Age-band lower bound, or null."""


class DataContributionStrategy(BaseModel):
    """
    How the plan year prices contributions: exactly one collection is populated, determined by the
    plan year's ``family`` (ICHRA vs tier-priced).
    """

    contribution_tiers: List[DataContributionStrategyContributionTier]
    """Coverage tiers and their costs; empty for ICHRA benefits."""

    ichra_contribution_classes: List[DataContributionStrategyIchraContributionClass]
    """ICHRA contribution classes; empty for tier-priced benefits."""


class DataEligibilityPolicyRuleEligibleGeographicalLocation(BaseModel):
    """Geographic matcher."""

    state_codes: List[str]
    """States the rule is restricted to; empty when `type` is `All`."""

    type: Literal["All", "StateCodes"]
    """
    - `All` - All
    - `StateCodes` - State Codes
    """


class DataEligibilityPolicyRule(BaseModel):
    """One eligibility rule — the workforce slice it makes eligible.

    Mirrors the internal
    ``PlanYearEligibilityPolicyRuleDTO`` minus the raw ids and timestamps.
    """

    compensation_type: Literal["Salary", "Hourly", "All"]
    """
    - `Salary` - Salary
    - `Hourly` - Hourly
    - `All` - All
    """

    eligible_geographical_location: DataEligibilityPolicyRuleEligibleGeographicalLocation
    """Geographic matcher."""

    employee_class: Literal["Full Time", "Part Time", "Temporary", "Intern", "Seasonal", "Individual Contractor", "All"]
    """
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Intern` - Intern
    - `Seasonal` - Seasonal
    - `Individual Contractor` - Individual Contractor
    - `All` - All
    """


class DataEligibilityPolicy(BaseModel):
    """The plan year's active eligibility policy.

    Mirrors the internal ``PlanYearEligibilityPolicyDTO``
    but exposes only the public subset (no raw ids, ``active_in``, or timestamps).
    """

    rules: List[DataEligibilityPolicyRule]
    """Eligibility rules; never empty for a valid policy."""

    termination_n_months: Optional[int] = None
    """
    Months of continued coverage; set only when `termination_rule` is
    `END_OF_N_MONTHS`.
    """

    termination_rule: Literal["END_OF_N_MONTHS", "END_OF_PLAN_YEAR"]
    """
    - `END_OF_N_MONTHS` - End Of N Months
    - `END_OF_PLAN_YEAR` - End Of Plan Year
    """

    waiting_period: Optional[Literal["FIRST_OF_FOLLOWING_MONTH", "THIRTY_DAYS", "SIXTY_DAYS"]] = None
    """
    - `FIRST_OF_FOLLOWING_MONTH` - First Of Following Month
    - `THIRTY_DAYS` - Thirty Days
    - `SIXTY_DAYS` - Sixty Days
    """


class DataEmployeeContribution(BaseModel):
    """Employee contribution range."""

    max_cents: int
    """Highest per-tier contribution in cents."""

    min_cents: int
    """Lowest per-tier contribution in cents."""


class DataEmployerContribution(BaseModel):
    """Employer contribution range."""

    max_cents: int
    """Highest per-tier contribution in cents."""

    min_cents: int
    """Lowest per-tier contribution in cents."""


class DataEnrollmentRate(BaseModel):
    """Enrolled/eligible rate for this plan year."""

    eligible: int
    """Employees eligible for this plan year."""

    enrolled: int
    """Employees enrolled in this plan year."""

    percentage: int
    """`enrolled / eligible` whole-number percent (0 when none)."""


class Data(BaseModel):
    """One plan year, detail view.

    Standalone (no shared base) so the exact detail payload is readable in one place; the list
    serializer is a separate class even where fields overlap. Detail carries the SPD link and omits
    the list-only ``is_current`` flag.
    """

    benefit_id: str
    """Prefixed benefit identifier (`bprd_*`)."""

    benefit_plan_year_id: str
    """Prefixed plan-year identifier (`plyr_*`)."""

    carrier: Optional[str] = None
    """Carrier name, or null (e.g. ICHRA)."""

    contribution_strategy: DataContributionStrategy
    """
    How the plan year prices contributions: exactly one collection is populated,
    determined by the plan year's `family` (ICHRA vs tier-priced).
    """

    coverage_end: Optional[date] = None
    """Coverage end."""

    coverage_start: date
    """Coverage start."""

    eligibility_policy: Optional[DataEligibilityPolicy] = None
    """The plan year's active eligibility policy.

    Mirrors the internal `PlanYearEligibilityPolicyDTO` but exposes only the public
    subset (no raw ids, `active_in`, or timestamps).
    """

    employee_contribution: Optional[DataEmployeeContribution] = None
    """Employee contribution range."""

    employer_contribution: Optional[DataEmployerContribution] = None
    """Employer contribution range."""

    enrollment_rate: DataEnrollmentRate
    """Enrolled/eligible rate for this plan year."""

    family: Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]
    """
    - `mec` - Mec
    - `mvp` - Mvp
    - `ichra` - Ichra
    - `vpc` - Vpc
    - `dental` - Dental
    - `vision` - Vision
    """

    network_names: List[str]
    """
    Displayed networks: ["multi"] for ICHRA, otherwise the plan year's distinct
    network names.
    """

    offered_states: List[str]
    """Distinct offered state codes."""

    open_enrollment_end: Optional[date] = None
    """Open-enrollment end."""

    open_enrollment_start: date
    """Open-enrollment start."""

    premium_in_cents: Optional[int] = None
    """Monthly premium in cents; only for an ICHRA benefit with effective coverage."""

    product_name: str
    """Benefit/product display name."""

    spd_file_url: Optional[str] = None
    """Summary Plan Description (SPD) link, or null."""

    status: Literal["active", "upcoming", "open_enrollment", "inactive"]
    """
    - `active` - Active
    - `upcoming` - Upcoming
    - `open_enrollment` - Open Enrollment
    - `inactive` - Inactive
    """

    year: int
    """Calendar coverage year."""


class EmployerRetrieveBenefitPlanYearResponse(BaseModel):
    """Response containing a single employer benefit plan year resource."""

    data: Data
    """One plan year, detail view.

    Standalone (no shared base) so the exact detail payload is readable in one
    place; the list serializer is a separate class even where fields overlap. Detail
    carries the SPD link and omits the list-only `is_current` flag.
    """
