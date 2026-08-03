# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["EmployerListResponse", "Address", "BenefitLifecycleStage", "EnrollmentRateSummary", "HRISStatus"]


class Address(BaseModel):
    """Shared read serializer for a postal address on public API responses.

    One definition for the address block every public resource emits (employer, employee, …), so the
    5-field shape isn't hand-rolled per endpoint. Read-only: it renders an already-built address
    value object (e.g. ``AddressDVO``) whose attributes map 1:1 to these fields.
    """

    address_line_1: str
    """Primary street address."""

    address_line_2: Optional[str] = None
    """Secondary street address (apt, suite, etc.)."""

    city: str
    """City name."""

    state: str
    """Two-letter state code (e.g. `CA`, `NY`)."""

    zipcode: str
    """ZIP code (5 or 9 digit)."""


class BenefitLifecycleStage(BaseModel):
    as_of_date: Optional[date] = None
    """Anchor date for the stage (e.g. renewal date); null when not applicable."""

    stage: str
    """
    Computed employer benefit-lifecycle stage: `open_enrollment`, `renewal`,
    `active`, `onboarding`, or `cancelled`.
    """


class EnrollmentRateSummary(BaseModel):
    """Enrolled/eligible employees roll-up."""

    eligible: int
    """Employees eligible for at least one active benefit."""

    enrolled: int
    """Employees enrolled in at least one active benefit."""

    percentage: int
    """`enrolled / eligible` as a whole-number percent (0 when none eligible)."""


class HRISStatus(BaseModel):
    """HRIS connection, or null when the employer has none."""

    provider: str
    """HRIS/payroll provider the employer is connected to (e.g. `Paychex`)."""

    status: str
    """Connection status reported by the integration."""


class EmployerListResponse(BaseModel):
    """One employer row of the organization's book (list projection).

    Carries the enriched/computed columns (enrollment roll-up, benefit-family tags, HRIS connection,
    benefit-lifecycle stage) alongside the flat CRM fields of the underlying employer (legal name,
    EIN, contact, address, timestamps) for parity with the legacy ``Employer`` contract.
    """

    active: bool
    """Whether the employer is currently active in the system."""

    address: Address
    """Shared read serializer for a postal address on public API responses.

    One definition for the address block every public resource emits (employer,
    employee, …), so the 5-field shape isn't hand-rolled per endpoint. Read-only: it
    renders an already-built address value object (e.g. `AddressDVO`) whose
    attributes map 1:1 to these fields.
    """

    benefit_families: List[str]
    """Distinct benefit-family tags across the employer's active benefits (e.g.

    `MEC`, `ICHRA`, `VPC`).
    """

    benefit_lifecycle_stage: BenefitLifecycleStage

    created_at: datetime
    """Timestamp when the employer was created."""

    ein: Optional[str] = None
    """Employer Identification Number (masked in responses)."""

    email: Optional[str] = None
    """Email address for billing and communications."""

    employer_id: str
    """Prefixed employer identifier (`empr_<base64-encoded-uuid>`)."""

    enrollment_rate_summary: EnrollmentRateSummary
    """Enrolled/eligible employees roll-up."""

    hris_status: Optional[HRISStatus] = None
    """HRIS connection, or null when the employer has none."""

    legal_name: Optional[str] = None
    """Legal business name for compliance and tax purposes."""

    name: str
    """Employer name."""

    organization_id: Optional[str] = None
    """ID of the parent organization (`org_*`), or null when unknown."""

    phone_number: Optional[str] = None
    """Employer phone number."""

    reference_id: Optional[str] = None
    """
    The organization's own reference id for this employer, or null when none was
    assigned.
    """

    updated_at: datetime
    """Timestamp when the employer was last updated."""
