# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .member import Member

__all__ = ["Dependent"]


class Dependent(Member):
    relationship: Literal["SPOUSE", "CHILD"]
