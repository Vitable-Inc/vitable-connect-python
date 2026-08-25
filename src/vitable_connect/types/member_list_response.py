# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberListResponse", "Address"]


class Address(BaseModel):
    """Member's residential address"""

    address_line_1: str
    """Primary street address"""

    city: str
    """City name"""

    state: Literal[
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WI",
        "WV",
        "WY",
        "PR",
        "GU",
        "AS",
        "VI",
        "MP",
        "MH",
        "PW",
        "FM",
        "AE",
        "AA",
        "AP",
    ]
    """
    - `AL` - AL
    - `AK` - AK
    - `AZ` - AZ
    - `AR` - AR
    - `CA` - CA
    - `CO` - CO
    - `CT` - CT
    - `DC` - DC
    - `DE` - DE
    - `FL` - FL
    - `GA` - GA
    - `HI` - HI
    - `ID` - ID
    - `IL` - IL
    - `IN` - IN
    - `IA` - IA
    - `KS` - KS
    - `KY` - KY
    - `LA` - LA
    - `ME` - ME
    - `MD` - MD
    - `MA` - MA
    - `MI` - MI
    - `MN` - MN
    - `MS` - MS
    - `MO` - MO
    - `MT` - MT
    - `NE` - NE
    - `NV` - NV
    - `NH` - NH
    - `NJ` - NJ
    - `NM` - NM
    - `NY` - NY
    - `NC` - NC
    - `ND` - ND
    - `OH` - OH
    - `OK` - OK
    - `OR` - OR
    - `PA` - PA
    - `RI` - RI
    - `SC` - SC
    - `SD` - SD
    - `TN` - TN
    - `TX` - TX
    - `UT` - UT
    - `VT` - VT
    - `VA` - VA
    - `WA` - WA
    - `WI` - WI
    - `WV` - WV
    - `WY` - WY
    - `PR` - PR
    - `GU` - GU
    - `AS` - AS
    - `VI` - VI
    - `MP` - MP
    - `MH` - MH
    - `PW` - PW
    - `FM` - FM
    - `AE` - AE
    - `AA` - AA
    - `AP` - AP
    """

    zipcode: str
    """ZIP code (5 or 9 digit)"""

    address_line_2: Optional[str] = None
    """Secondary street address (apt, suite, etc.)"""


class MemberListResponse(BaseModel):
    """
    A member in the organization's directory: identity, contact details, address, and join date.
    """

    id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    first_name: str
    """Member's legal first name"""

    last_name: str
    """Member's legal last name"""

    address: Optional[Address] = None
    """Member's residential address"""

    email: Optional[str] = None
    """Email address"""

    phone: Optional[str] = None
    """Phone number (10-digit US domestic string)"""
