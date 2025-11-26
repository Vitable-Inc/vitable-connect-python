# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmployerUpdateParams"]


class EmployerUpdateParams(TypedDict, total=False):
    active: bool

    legal_name: str

    name: str
