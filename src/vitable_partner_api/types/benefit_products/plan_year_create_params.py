# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PlanYearCreateParams", "ContributionClass", "PlanCost"]


class PlanYearCreateParams(TypedDict, total=False):
    coverage_end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    coverage_start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    employer_id: Required[str]

    open_enrollment_end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    open_enrollment_start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    contribution_classes: Iterable[ContributionClass]

    plan_costs: Iterable[PlanCost]


class ContributionClass(TypedDict, total=False):
    compensation: Required[Literal["UNSPECIFIED", "SALARY", "HOURLY"]]

    employer_contribution_in_cents: Required[int]

    employment: Required[Literal["UNSPECIFIED", "FULL_TIME", "PART_TIME", "TEMPORARY", "SEASONAL"]]

    family_status: Required[Literal["UNSPECIFIED", "EE", "ES", "EC", "EF"]]

    location: Required[Literal["UNSPECIFIED", "STATE"]]

    location_value: str

    max_age: int

    min_age: int

    plan_id: Optional[str]


class PlanCost(TypedDict, total=False):
    dependent_cost_in_cents: Required[int]

    employee_cost_in_cents: Required[int]

    plan_id: Required[str]
