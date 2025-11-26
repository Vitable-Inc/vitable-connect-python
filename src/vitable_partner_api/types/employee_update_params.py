# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmployeeUpdateParams"]


class EmployeeUpdateParams(TypedDict, total=False):
    date_of_birth: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    first_name: str

    gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"]

    last_name: str

    sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"]

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    suffix: str
