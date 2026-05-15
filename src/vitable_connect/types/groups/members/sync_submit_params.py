# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SyncSubmitParams", "Member", "MemberAddress"]


class SyncSubmitParams(TypedDict, total=False):
    members: Required[Iterable[Member]]


class MemberAddress(TypedDict, total=False):
    address_line_1: Required[str]

    city: Required[str]

    state: Required[str]

    zipcode: Required[str]

    address_line_2: Optional[str]


class Member(TypedDict, total=False):
    address: Required[MemberAddress]

    date_of_birth: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    first_name: Required[str]

    last_name: Required[str]

    phone: Required[str]

    plan_id: Required[str]

    reference_id: Required[str]

    email: Optional[str]
