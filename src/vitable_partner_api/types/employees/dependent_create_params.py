# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DependentCreateParams"]


class DependentCreateParams(TypedDict, total=False):
    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    first_name: Required[str]

    last_name: Required[str]

    relationship: Required[Literal["SPOUSE", "CHILD"]]

    gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"]

    sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"]

    suffix: str
