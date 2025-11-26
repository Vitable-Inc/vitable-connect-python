# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmployeeCreateParams"]


class EmployeeCreateParams(TypedDict, total=False):
    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    first_name: Required[str]

    last_name: Required[str]

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"]

    sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"]

    ssn: str
    """Social Security Number (only allowed on create)"""

    suffix: str
