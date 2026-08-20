# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberListIDCardsResponse", "Data", "DataNetwork", "DataNetworkAddress"]


class DataNetworkAddress(BaseModel):
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


class DataNetwork(BaseModel):
    """Provider network shown on the card; null for an rx card"""

    id: str

    address: DataNetworkAddress
    """Shared read serializer for a postal address on public API responses.

    One definition for the address block every public resource emits (employer,
    employee, …), so the 5-field shape isn't hand-rolled per endpoint. Read-only: it
    renders an already-built address value object (e.g. `AddressDVO`) whose
    attributes map 1:1 to these fields.
    """

    logo: Optional[str] = None

    member_phone: Optional[str] = None

    name: str
    """Name of the network"""

    phone: str

    provider_phone: Optional[str] = None

    website: str
    """Website of the network"""

    edi: Optional[str] = None
    """Network's EDI"""

    member_website: Optional[str] = None
    """Website for members"""

    provider_website: Optional[str] = None
    """Website for providers"""


class Data(BaseModel):
    """Wire serializer for :class:`DigitalBenefitCardDTO` (one benefit ID card)."""

    card_type: Literal["medical", "dental", "vision", "rx"]
    """
    - `medical` - medical
    - `dental` - dental
    - `vision` - vision
    - `rx` - rx
    """

    group_id: str
    """Group number printed on the card (the rx group id for an rx card)"""

    group_member_id: str
    """Member id printed on the card (the Ventegra cardholder id for an rx card)"""

    member_name: str
    """Name of the member the card is issued to"""

    nsa_table: List[List[str]]
    """No Surprises Act cost-sharing table rendered on the card; empty for an rx card"""

    benefit_code: Optional[
        Literal[
            "EBA",
            "VPC",
            "VPC_CORE",
            "MEC",
            "MEC2",
            "MEC_PLUS",
            "MVP",
            "MVP2",
            "MVPSL",
            "MVPSL2",
            "VD",
            "VV",
            "ICHRA",
            "ICHRA_PREMIUM_PLUS",
            "ICHRA_REIMBURSEMENT_ONLY",
        ]
    ] = None
    """
    - `EBA` - Eba Mec
    - `VPC` - Vpc Enhanced
    - `VPC_CORE` - Vpc Core
    - `MEC` - Vpc Mec
    - `MEC2` - Mec2
    - `MEC_PLUS` - Mec Plus
    - `MVP` - Mvp
    - `MVP2` - Mvp2
    - `MVPSL` - Mvpsl
    - `MVPSL2` - Mvpsl2
    - `VD` - Dental
    - `VV` - Vision
    - `ICHRA` - Ichra
    - `ICHRA_PREMIUM_PLUS` - Ichra Premium Plus
    - `ICHRA_REIMBURSEMENT_ONLY` - Ichra Reimbursement Only
    """

    carrier_phone: Optional[str] = None
    """Carrier phone number on the card; null for an rx card"""

    carrier_website: Optional[str] = None
    """Carrier website on the card; null for an rx card"""

    claims_payer_display_name: Optional[str] = None
    """Claims payer shown on the card"""

    employer_name: Optional[str] = None
    """Employer the card's coverage is through; null for an rx card without group info"""

    general_disclaimer: Optional[str] = None
    """General disclaimer text; null for an rx card"""

    network: Optional[DataNetwork] = None
    """Provider network shown on the card; null for an rx card"""

    plan_disclaimer: Optional[str] = None
    """Plan-specific disclaimer text; null for an rx card"""

    plan_name: Optional[str] = None
    """Benefit plan name on the card; null for a consumer-membership rx card"""


class MemberListIDCardsResponse(BaseModel):
    """Unpaginated ``{"data": [...]}`` list of member digital benefit cards."""

    data: List[Data]
