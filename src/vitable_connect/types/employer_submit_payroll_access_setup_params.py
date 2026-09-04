# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmployerSubmitPayrollAccessSetupParams"]


class EmployerSubmitPayrollAccessSetupParams(TypedDict, total=False):
    access_method: Required[Literal["SELF_SETUP", "NEEDS_HELP"]]
    """
    - `SELF_SETUP` - SELF_SETUP
    - `NEEDS_HELP` - NEEDS_HELP
    """

    all_benefit_eligible_employees_present: Required[bool]

    classifications_accurate: Required[bool]

    employees_in_payroll_acknowledged: Required[bool]

    has_additional_payroll_system: Required[bool]

    is_controlled_group: Required[bool]

    payroll_data_impacts_eligibility_acknowledged: Required[bool]

    additional_access_method: Optional[Literal["SELF_SETUP", "NEEDS_HELP"]]
    """
    - `SELF_SETUP` - SELF_SETUP
    - `NEEDS_HELP` - NEEDS_HELP
    """

    additional_integration_confirmed: Optional[bool]

    additional_login_url: Optional[str]

    additional_password: Optional[str]

    additional_phone: Optional[str]

    additional_username: Optional[str]

    classification_correction_source: Optional[Literal["ENTER_NAMES", "EMAIL_LIST"]]
    """
    - `ENTER_NAMES` - ENTER_NAMES
    - `EMAIL_LIST` - EMAIL_LIST
    """

    integration_confirmed: Optional[bool]

    login_url: Optional[str]

    misclassified_employee_names: SequenceNotStr[str]

    missing_employee_resolution: Optional[Literal["EMAIL_CENSUS", "SECOND_SYSTEM_ACCESS"]]
    """
    - `EMAIL_CENSUS` - EMAIL_CENSUS
    - `SECOND_SYSTEM_ACCESS` - SECOND_SYSTEM_ACCESS
    """

    password: Optional[str]

    phone: Optional[str]

    remaining_employee_action: Optional[Literal["VITABLE_UPDATE", "EMPLOYER_UPDATE"]]
    """
    - `VITABLE_UPDATE` - VITABLE_UPDATE
    - `EMPLOYER_UPDATE` - EMPLOYER_UPDATE
    """

    same_payroll_covers_other_eins: Optional[bool]

    username: Optional[str]
