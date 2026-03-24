# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookEventListParams"]


class WebhookEventListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    event_name: Literal[
        "enrollment.accepted",
        "enrollment.terminated",
        "enrollment.elected",
        "enrollment.granted",
        "enrollment.waived",
        "enrollment.started",
        "employee.eligibility_granted",
        "employee.eligibility_terminated",
        "employee.deactivated",
        "payroll_deduction.created",
        "employer.eligibility_policy_created",
    ]
    """
    - `enrollment.accepted` - Enrollment Accepted
    - `enrollment.terminated` - Enrollment Terminated
    - `enrollment.elected` - Enrollment Elected
    - `enrollment.granted` - Enrollment Granted
    - `enrollment.waived` - Enrollment Waived
    - `enrollment.started` - Enrollment Started
    - `employee.eligibility_granted` - Employee Eligibility Granted
    - `employee.eligibility_terminated` - Employee Eligibility Terminated
    - `employee.deactivated` - Employee Deactivated
    - `payroll_deduction.created` - Payroll Deduction Created
    - `employer.eligibility_policy_created` - Employer Eligibility Policy Created
    """

    limit: int
    """Items per page (default: 20, max: 100)"""

    page: int
    """Page number (default: 1)"""

    resource_id: str

    resource_type: Literal["enrollment", "employee", "employer", "dependent", "plan_year", "payroll_deduction"]
    """
    - `enrollment` - Enrollment
    - `employee` - Employee
    - `employer` - Employer
    - `dependent` - Dependent
    - `plan_year` - Plan Year
    - `payroll_deduction` - Payroll Deduction
    """
