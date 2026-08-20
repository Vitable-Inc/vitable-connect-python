# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmployerListPayrollDeductionStatementsResponse"]


class EmployerListPayrollDeductionStatementsResponse(BaseModel):
    """One payroll-deduction statement row.

    Reads a :class:`PayrollDeductionStatementDTO` by attribute: the ``statement_id`` character field renders the
    prefixed id via ``str()``, and the date/datetime fields emit ISO-8601 strings.
    """

    csv_file_url: Optional[str] = None
    """Download link for the change CSV, or null."""

    deduction_frequency: Literal["weekly", "bi_weekly", "semi_monthly", "monthly"]
    """
    - `weekly` - Weekly
    - `bi_weekly` - Bi Weekly
    - `semi_monthly` - Semi Monthly
    - `monthly` - Monthly
    """

    deduction_frequency_label: str
    """Human-readable deduction frequency (e.g. `Monthly`)."""

    employee_count: int
    """Distinct employees covered by the statement's entries."""

    period_end: date
    """Deduction period end date."""

    period_start: date
    """Deduction period start date."""

    run_date: datetime
    """When the statement was generated."""

    statement_id: str
    """
    Prefixed payroll-deduction-statement identifier (`pstmt_<base64-encoded-uuid>`).
    """

    total_deduction_cents: int
    """Total payroll deduction for the period, in cents."""
