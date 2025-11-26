# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QualifyingLifeEventCreateParams"]


class QualifyingLifeEventCreateParams(TypedDict, total=False):
    event_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    event_type: Required[
        Literal[
            "MARRIAGE",
            "BIRTH",
            "ADOPTION",
            "DIVORCE",
            "DEATH",
            "JOB_LOSS",
            "REDUCTION_IN_HOURS",
            "EMPLOYER_BANKRUPTCY",
            "MEDICARE_ENTITLEMENT",
            "TERMINATION",
            "OTHER",
        ]
    ]

    description: str

    proof_document_url: str
