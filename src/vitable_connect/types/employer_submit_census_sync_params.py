# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .employee_class import EmployeeClass

__all__ = ["EmployerSubmitCensusSyncParams", "Employee", "EmployeeAddress"]


class EmployerSubmitCensusSyncParams(TypedDict, total=False):
    employees: Required[Iterable[Employee]]


class EmployeeAddress(TypedDict, total=False):
    address_line_1: Required[str]

    city: Required[str]

    state: Required[
        Literal[
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

    zipcode: Required[str]

    address_line_2: Optional[str]


class Employee(TypedDict, total=False):
    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    email: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    phone: Required[str]

    address: Optional[EmployeeAddress]

    compensation_type: Optional[Literal["Salary", "Hourly"]]
    """
    - `Salary` - Salary
    - `Hourly` - Hourly
    """

    employee_class: Optional[EmployeeClass]
    """
    - `Full Time` - Full Time
    - `Part Time` - Part Time
    - `Temporary` - Temporary
    - `Intern` - Intern
    - `Seasonal` - Seasonal
    - `Individual Contractor` - Individual Contractor
    """

    reference_id: Optional[str]

    start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
