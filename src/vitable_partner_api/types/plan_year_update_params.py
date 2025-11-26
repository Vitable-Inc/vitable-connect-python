# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PlanYearUpdateParams", "ContributionClass", "PlanCost"]


class PlanYearUpdateParams(TypedDict, total=False):
    contribution_classes: Iterable[ContributionClass]

    coverage_end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    coverage_start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    open_enrollment_end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    open_enrollment_start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    plan_costs: Iterable[PlanCost]


class ContributionClass(TypedDict, total=False):
    compensation: str

    employer_contribution_in_cents: int

    employment: str

    family_status: str

    location: str

    location_value: str

    max_age: int

    min_age: int

    plan_id: str


class PlanCost(TypedDict, total=False):
    dependent_cost_in_cents: int

    employee_cost_in_cents: int

    plan_id: str
