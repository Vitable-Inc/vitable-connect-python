# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemberRetrieveResponse", "Data", "DataAddress"]


class DataAddress(BaseModel):
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


class Data(BaseModel):
    """
    A member's profile: identity, contact details, address, demographics, and onboarding status.
    """

    id: str
    """Unique member identifier with 'mbr\\__' prefix"""

    age: int
    """Member's age in years, derived from date of birth"""

    date_of_birth: date
    """Date of birth (YYYY-MM-DD)"""

    first_name: str
    """Member's legal first name"""

    last_name: str
    """Member's legal last name"""

    name: str
    """Member's full legal name"""

    status: Literal["onboarded", "pending_onboarding"]
    """Member profile status (onboarded or pending onboarding)"""

    address: Optional[DataAddress] = None
    """Member's residential address"""

    email: Optional[str] = None
    """Email address"""

    gender: Optional[Literal["Male", "Female", "Transgender", "Non-binary", "Prefer not to respond"]] = None
    """
    - `Male` - Male
    - `Female` - Female
    - `Transgender` - Transgender
    - `Non-binary` - Non Binary
    - `Prefer not to respond` - Prefer Not To Respond
    """

    marital_status: Optional[Literal["Single", "Married"]] = None
    """
    - `Single` - Single
    - `Married` - Married
    """

    middle_name: Optional[str] = None
    """Member's legal middle name"""

    phone: Optional[str] = None
    """Phone number (10-digit US domestic string)"""

    preferred_language: Optional[Literal["en", "es", "zh", "ru", "sw", "th"]] = None
    """
    - `en` - English
    - `es` - Spanish
    - `zh` - Chinese
    - `ru` - Russian
    - `sw` - Swahili
    - `th` - Thai
    """

    sex_at_birth: Optional[Literal["Male", "Female", "Other", "Unknown"]] = None
    """
    - `Male` - Male
    - `Female` - Female
    - `Other` - Other
    - `Unknown` - Unknown
    """

    suffix: Optional[Literal["Sr", "Jr", "I", "II", "III", "IV", "V"]] = None
    """
    - `Sr` - Sr
    - `Jr` - Jr
    - `I` - I
    - `II` - II
    - `III` - III
    - `IV` - IV
    - `V` - V
    """

    tobacco_status: Optional[bool] = None
    """Whether the member uses tobacco, if known"""


class MemberRetrieveResponse(BaseModel):
    """Response containing a single member resource."""

    data: Data
    """
    A member's profile: identity, contact details, address, demographics, and
    onboarding status.
    """
