# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Member"]


class Member(BaseModel):
    id: str

    date_of_birth: date

    first_name: str

    last_name: str

    gender: Optional[Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"]] = None

    sex: Optional[Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"]] = None

    suffix: Optional[str] = None
