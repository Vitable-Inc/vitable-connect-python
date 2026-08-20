# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    employer_list_params,
    employer_create_params,
    employer_update_params,
    employer_list_invoices_params,
    employer_list_employees_params,
    employer_update_settings_params,
    employer_submit_census_sync_params,
    employer_submit_payroll_access_setup_params,
    employer_list_payroll_deduction_statements_params,
    employer_list_benefit_plan_year_enrollments_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPageNumberPage, AsyncPageNumberPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.employee import Employee
from ..types.employer_response import EmployerResponse
from ..types.employer_list_response import EmployerListResponse
from ..types.employer_list_invoices_response import EmployerListInvoicesResponse
from ..types.employer_retrieve_hris_response import EmployerRetrieveHRISResponse
from ..types.employer_update_settings_response import EmployerUpdateSettingsResponse
from ..types.employer_submit_census_sync_response import EmployerSubmitCensusSyncResponse
from ..types.employer_list_hris_providers_response import EmployerListHRISProvidersResponse
from ..types.employer_retrieve_invoice_pdf_response import EmployerRetrieveInvoicePdfResponse
from ..types.employer_list_benefit_plan_years_response import EmployerListBenefitPlanYearsResponse
from ..types.employer_retrieve_benefit_plan_year_response import EmployerRetrieveBenefitPlanYearResponse
from ..types.employer_submit_payroll_access_setup_response import EmployerSubmitPayrollAccessSetupResponse
from ..types.employer_retrieve_payroll_access_setup_response import EmployerRetrievePayrollAccessSetupResponse
from ..types.employer_ensure_payroll_integration_email_response import EmployerEnsurePayrollIntegrationEmailResponse
from ..types.employer_list_payroll_deduction_statements_response import EmployerListPayrollDeductionStatementsResponse
from ..types.employer_list_benefit_plan_year_enrollments_response import EmployerListBenefitPlanYearEnrollmentsResponse

__all__ = ["EmployersResource", "AsyncEmployersResource"]


class EmployersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EmployersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return EmployersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: employer_create_params.Address,
        ein: str,
        email: str,
        legal_name: str,
        name: str,
        phone_number: Optional[str] | Omit = omit,
        reference_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Creates a new employer for the authenticated organization.

        Requires employer
        name, legal name, EIN, email, and address information. Returns the created
        employer with its assigned ID.

        Args:
          address: Employer address

          ein: Employer Identification Number (format: XX-XXXXXXX)

          email: Email address for billing and communications

          legal_name: Legal business name

          name: Employer display name

          phone_number: Employer phone number (10-digit US format, e.g. 5551234567)

          reference_id: External reference ID for this employer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/employers",
            body=maybe_transform(
                {
                    "address": address,
                    "ein": ein,
                    "email": email,
                    "legal_name": legal_name,
                    "name": name,
                    "phone_number": phone_number,
                    "reference_id": reference_id,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def retrieve(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Retrieves detailed information for a specific employer by ID.

        The employer must
        belong to the authenticated organization.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            path_template("/v1/employers/{employer_id}", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def update(
        self,
        employer_id: str,
        *,
        active: Optional[bool] | Omit = omit,
        address: Optional[employer_update_params.Address] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Updates an existing employer.

        All fields are optional — only provided fields are
        updated. PO Box addresses are rejected.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          active: Whether the employer is active

          address: Employer address

          legal_name: Legal business name

          name: Employer display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._put(
            path_template("/v1/employers/{employer_id}", employer_id=employer_id),
            body=maybe_transform(
                {
                    "active": active,
                    "address": address,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def list(
        self,
        *,
        benefit_family: List[Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]] | Omit = omit,
        benefit_lifecycle_stage: List[Literal["open_enrollment", "renewal", "active", "onboarding", "cancelled"]]
        | Omit = omit,
        hris_provider: SequenceNotStr[str] | Omit = omit,
        hris_status: List[Literal["Pending", "Active", "Inactive", "Paused", "Terminated"]] | Omit = omit,
        include_cancelled: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[EmployerListResponse]:
        """
        Returns the caller's employer book — every employer with its computed columns
        (enrollment-rate summary, benefit-family tags, HRIS connection,
        benefit-lifecycle stage) merged with the employer's flat CRM fields (legal name,
        EIN, contact, address, timestamps). The book is derived from the authenticated
        principal: one organization's employers, or every organization's for a caller
        whose reach is not a single organization. Supports name search,
        benefit-family/lifecycle/HRIS filters, and page/limit pagination.

        Args:
          benefit_family: Filter to employers with at least one active benefit in these families.

          benefit_lifecycle_stage: Filter to employers in one of these computed benefit-lifecycle stages.

          hris_provider: Filter to employers whose HRIS connection is with one of these payroll providers
              (e.g. `ADP RUN`). Matched case-insensitively; free text, so read the available
              values from the HRIS-providers endpoint rather than assuming a fixed set.

          hris_status: Filter to employers whose HRIS connection is in one of these statuses.

          include_cancelled: Include cancelled employers (hidden by default unless their stage is explicitly
              requested).

          limit: Items per page.

          page: Page number.

          search: Case-insensitive employer-name substring filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/employers",
            page=SyncPageNumberPage[EmployerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "benefit_family": benefit_family,
                        "benefit_lifecycle_stage": benefit_lifecycle_stage,
                        "hris_provider": hris_provider,
                        "hris_status": hris_status,
                        "include_cancelled": include_cancelled,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    employer_list_params.EmployerListParams,
                ),
            ),
            model=EmployerListResponse,
        )

    def ensure_payroll_integration_email(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerEnsurePayrollIntegrationEmailResponse:
        """
        Provision and return the employer's payroll integration email.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._put(
            path_template("/v1/employers/{employer_id}/payroll-integration-email", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerEnsurePayrollIntegrationEmailResponse,
        )

    def list_benefit_plan_year_enrollments(
        self,
        benefit_plan_year_id: str,
        *,
        employer_id: str,
        election_status: List[Literal["Enrolled", "Expired", "Pending", "Waived"]] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse]:
        """
        Returns a paginated list of every member with an enrollment in one of an
        employer's plan years, any election status: what they elected, where their
        coverage stands, dependent count, carrier, plan, tier, and the plan's total
        monthly cost. The caller must be authorized for the employer `empr_<...>`; an
        unknown or unauthorized employer, or an unknown plan year `plyr_<...>`,
        returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          benefit_plan_year_id: Unique benefit-plan-year identifier (plyr\\__\\**).

          election_status: Filter by election status. Repeat the parameter to match several.

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          search: Case-insensitive search. Matches member name partially, and the `member_id`
              exactly — either your own reference id or the prefixed `grpmbr_<...>` id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        if not benefit_plan_year_id:
            raise ValueError(
                f"Expected a non-empty value for `benefit_plan_year_id` but received {benefit_plan_year_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/v1/employers/{employer_id}/benefit-plan-years/{benefit_plan_year_id}/enrollments",
                employer_id=employer_id,
                benefit_plan_year_id=benefit_plan_year_id,
            ),
            page=SyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "election_status": election_status,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    employer_list_benefit_plan_year_enrollments_params.EmployerListBenefitPlanYearEnrollmentsParams,
                ),
            ),
            model=EmployerListBenefitPlanYearEnrollmentsResponse,
        )

    def list_benefit_plan_years(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListBenefitPlanYearsResponse:
        """
        Returns the employer's benefit plan years (all years, or one when `year` is
        given), each with its benefits, offered states, benefit families, and the
        year-level enrollment roll-up. The caller must be authorized for the employer;
        an unknown or unauthorized employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            path_template("/v1/employers/{employer_id}/benefit-plan-years", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerListBenefitPlanYearsResponse,
        )

    def list_employees(
        self,
        employer_id: str,
        *,
        employment_status: Literal["active", "terminated"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[Employee]:
        """Retrieves a paginated list of employees for a specific employer.

        The caller must
        be authorized for the employer; an unknown or unauthorized employer returns 404.
        Results are paginated using page and limit parameters and can be narrowed with a
        case-insensitive `search` (first name, last name, or email) and an
        `employment_status` filter (active or terminated). Each employee includes
        payroll deductions from the most recent statement period. When a new deduction
        statement is generated, previous period deductions are replaced.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          employment_status: Filter by employment status (active or terminated)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          search: Case-insensitive search across employee first name, last name, and email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get_api_list(
            path_template("/v1/employers/{employer_id}/employees", employer_id=employer_id),
            page=SyncPageNumberPage[Employee],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employment_status": employment_status,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    employer_list_employees_params.EmployerListEmployeesParams,
                ),
            ),
            model=Employee,
        )

    def list_hris_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListHRISProvidersResponse:
        """
        Returns the distinct HRIS/payroll providers across the same book
        `GET /v1/employers` returns, sorted for display. Use these as the values for the
        employers list's `hris_provider` filter — the providers are free text, so they
        cannot be enumerated in advance.
        """
        return self._get(
            "/v1/employers/hris-providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerListHRISProvidersResponse,
        )

    def list_invoices(
        self,
        employer_id: str,
        *,
        limit: int | Omit = omit,
        offset: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListInvoicesResponse:
        """Returns a cursor-paginated page of the employer's billing invoices, newest
        first.

        Pass the `next_offset` from a previous page as `offset` to fetch the next
        page. The caller must be authorized for the employer; an unknown or unauthorized
        employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          limit: Maximum number of invoices per page

          offset: Opaque cursor from a previous page's next_offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            path_template("/v1/employers/{employer_id}/invoices", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    employer_list_invoices_params.EmployerListInvoicesParams,
                ),
            ),
            cast_to=EmployerListInvoicesResponse,
        )

    def list_payroll_deduction_statements(
        self,
        employer_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse]:
        """
        Returns a paginated list of the employer's payroll-deduction statements, newest
        period first, each with its period, generation date, distinct employee count,
        total deduction, change-file link, and deduction frequency. Statements
        superseded by a later correction are excluded. The caller must be authorized for
        the employer; an unknown or unauthorized employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          limit: Maximum number of statements per page

          page: Page number to retrieve (starts at 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get_api_list(
            path_template("/v1/employers/{employer_id}/payroll-deduction-statements", employer_id=employer_id),
            page=SyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    employer_list_payroll_deduction_statements_params.EmployerListPayrollDeductionStatementsParams,
                ),
            ),
            model=EmployerListPayrollDeductionStatementsResponse,
        )

    def retrieve_benefit_plan_year(
        self,
        benefit_plan_year_id: str,
        *,
        employer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrieveBenefitPlanYearResponse:
        """
        Returns one benefit plan year in full — its benefit details plus the per-benefit
        enrollment rate and SPD link — addressed by its `benefit_plan_year_id`. The
        caller must be authorized for the employer; an unknown or unauthorized plan year
        returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          benefit_plan_year_id: Unique benefit-plan-year identifier (plyr\\__\\**).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        if not benefit_plan_year_id:
            raise ValueError(
                f"Expected a non-empty value for `benefit_plan_year_id` but received {benefit_plan_year_id!r}"
            )
        return self._get(
            path_template(
                "/v1/employers/{employer_id}/benefit-plan-years/{benefit_plan_year_id}",
                employer_id=employer_id,
                benefit_plan_year_id=benefit_plan_year_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveBenefitPlanYearResponse,
        )

    def retrieve_hris(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrieveHRISResponse:
        """
        Returns the employer's HRIS connection — provider, status, last sync, and synced
        row count — or null when the employer has no integration. The caller must be
        authorized for the employer; an unknown or unauthorized employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            path_template("/v1/employers/{employer_id}/hris", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveHRISResponse,
        )

    def retrieve_invoice_pdf(
        self,
        invoice_id: str,
        *,
        employer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrieveInvoicePdfResponse:
        """
        Returns the time-limited PDF download link for a single invoice belonging to the
        employer's billing customer. `invoice_id` is the external Chargebee id (not a
        prefixed UUID). The caller must be authorized for the employer; an unknown or
        unauthorized employer or invoice returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          invoice_id: External Chargebee invoice id (not a prefixed UUID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get(
            path_template(
                "/v1/employers/{employer_id}/invoices/{invoice_id}/pdf", employer_id=employer_id, invoice_id=invoice_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveInvoicePdfResponse,
        )

    def retrieve_payroll_access_setup(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrievePayrollAccessSetupResponse:
        """
        Return whether the employer has submitted payroll access setup.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            path_template("/v1/employers/{employer_id}/payroll-access-setup", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrievePayrollAccessSetupResponse,
        )

    def submit_census_sync(
        self,
        employer_id: str,
        *,
        employees: Iterable[employer_submit_census_sync_params.Employee],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerSubmitCensusSyncResponse:
        """Submits a census sync payload for the specified employer.

        The employees in the
        payload will be queued for processing. Returns an accepted response with the
        timestamp of acceptance.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._post(
            path_template("/v1/employers/{employer_id}/census-sync", employer_id=employer_id),
            body=maybe_transform(
                {"employees": employees}, employer_submit_census_sync_params.EmployerSubmitCensusSyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerSubmitCensusSyncResponse,
        )

    def submit_payroll_access_setup(
        self,
        employer_id: str,
        *,
        access_method: Literal["SELF_SETUP", "NEEDS_HELP"],
        all_benefit_eligible_employees_present: bool,
        classifications_accurate: bool,
        employees_in_payroll_acknowledged: bool,
        has_additional_payroll_system: bool,
        is_controlled_group: bool,
        payroll_data_impacts_eligibility_acknowledged: bool,
        additional_access_method: Optional[Literal["SELF_SETUP", "NEEDS_HELP"]] | Omit = omit,
        additional_integration_confirmed: Optional[bool] | Omit = omit,
        additional_login_url: Optional[str] | Omit = omit,
        additional_password: Optional[str] | Omit = omit,
        additional_phone: Optional[str] | Omit = omit,
        additional_username: Optional[str] | Omit = omit,
        classification_correction_source: Optional[Literal["ENTER_NAMES", "EMAIL_LIST"]] | Omit = omit,
        integration_confirmed: Optional[bool] | Omit = omit,
        login_url: Optional[str] | Omit = omit,
        misclassified_employee_names: SequenceNotStr[str] | Omit = omit,
        missing_employee_resolution: Optional[Literal["EMAIL_CENSUS", "SECOND_SYSTEM_ACCESS"]] | Omit = omit,
        password: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        remaining_employee_action: Optional[Literal["VITABLE_UPDATE", "EMPLOYER_UPDATE"]] | Omit = omit,
        same_payroll_covers_other_eins: Optional[bool] | Omit = omit,
        username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerSubmitPayrollAccessSetupResponse:
        """
        Submit the employer's payroll access setup answers.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          access_method: - `SELF_SETUP` - SELF_SETUP
              - `NEEDS_HELP` - NEEDS_HELP

          additional_access_method: - `SELF_SETUP` - SELF_SETUP
              - `NEEDS_HELP` - NEEDS_HELP

          classification_correction_source: - `ENTER_NAMES` - ENTER_NAMES
              - `EMAIL_LIST` - EMAIL_LIST

          missing_employee_resolution: - `EMAIL_CENSUS` - EMAIL_CENSUS
              - `SECOND_SYSTEM_ACCESS` - SECOND_SYSTEM_ACCESS

          remaining_employee_action: - `VITABLE_UPDATE` - VITABLE_UPDATE
              - `EMPLOYER_UPDATE` - EMPLOYER_UPDATE

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._put(
            path_template("/v1/employers/{employer_id}/payroll-access-setup", employer_id=employer_id),
            body=maybe_transform(
                {
                    "access_method": access_method,
                    "all_benefit_eligible_employees_present": all_benefit_eligible_employees_present,
                    "classifications_accurate": classifications_accurate,
                    "employees_in_payroll_acknowledged": employees_in_payroll_acknowledged,
                    "has_additional_payroll_system": has_additional_payroll_system,
                    "is_controlled_group": is_controlled_group,
                    "payroll_data_impacts_eligibility_acknowledged": payroll_data_impacts_eligibility_acknowledged,
                    "additional_access_method": additional_access_method,
                    "additional_integration_confirmed": additional_integration_confirmed,
                    "additional_login_url": additional_login_url,
                    "additional_password": additional_password,
                    "additional_phone": additional_phone,
                    "additional_username": additional_username,
                    "classification_correction_source": classification_correction_source,
                    "integration_confirmed": integration_confirmed,
                    "login_url": login_url,
                    "misclassified_employee_names": misclassified_employee_names,
                    "missing_employee_resolution": missing_employee_resolution,
                    "password": password,
                    "phone": phone,
                    "remaining_employee_action": remaining_employee_action,
                    "same_payroll_covers_other_eins": same_payroll_covers_other_eins,
                    "username": username,
                },
                employer_submit_payroll_access_setup_params.EmployerSubmitPayrollAccessSetupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerSubmitPayrollAccessSetupResponse,
        )

    def update_settings(
        self,
        employer_id: str,
        *,
        pay_frequency: Literal["weekly", "bi_weekly", "semi_monthly", "monthly"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerUpdateSettingsResponse:
        """Updates configuration settings for a specific employer.

        The employer must belong
        to the authenticated organization.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          pay_frequency: - `weekly` - Weekly
              - `bi_weekly` - Bi Weekly
              - `semi_monthly` - Semi Monthly
              - `monthly` - Monthly

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._put(
            path_template("/v1/employers/{employer_id}/settings", employer_id=employer_id),
            body=maybe_transform(
                {"pay_frequency": pay_frequency}, employer_update_settings_params.EmployerUpdateSettingsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerUpdateSettingsResponse,
        )


class AsyncEmployersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncEmployersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: employer_create_params.Address,
        ein: str,
        email: str,
        legal_name: str,
        name: str,
        phone_number: Optional[str] | Omit = omit,
        reference_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Creates a new employer for the authenticated organization.

        Requires employer
        name, legal name, EIN, email, and address information. Returns the created
        employer with its assigned ID.

        Args:
          address: Employer address

          ein: Employer Identification Number (format: XX-XXXXXXX)

          email: Email address for billing and communications

          legal_name: Legal business name

          name: Employer display name

          phone_number: Employer phone number (10-digit US format, e.g. 5551234567)

          reference_id: External reference ID for this employer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/employers",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "ein": ein,
                    "email": email,
                    "legal_name": legal_name,
                    "name": name,
                    "phone_number": phone_number,
                    "reference_id": reference_id,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    async def retrieve(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Retrieves detailed information for a specific employer by ID.

        The employer must
        belong to the authenticated organization.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            path_template("/v1/employers/{employer_id}", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    async def update(
        self,
        employer_id: str,
        *,
        active: Optional[bool] | Omit = omit,
        address: Optional[employer_update_params.Address] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Updates an existing employer.

        All fields are optional — only provided fields are
        updated. PO Box addresses are rejected.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          active: Whether the employer is active

          address: Employer address

          legal_name: Legal business name

          name: Employer display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._put(
            path_template("/v1/employers/{employer_id}", employer_id=employer_id),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "address": address,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def list(
        self,
        *,
        benefit_family: List[Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]] | Omit = omit,
        benefit_lifecycle_stage: List[Literal["open_enrollment", "renewal", "active", "onboarding", "cancelled"]]
        | Omit = omit,
        hris_provider: SequenceNotStr[str] | Omit = omit,
        hris_status: List[Literal["Pending", "Active", "Inactive", "Paused", "Terminated"]] | Omit = omit,
        include_cancelled: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmployerListResponse, AsyncPageNumberPage[EmployerListResponse]]:
        """
        Returns the caller's employer book — every employer with its computed columns
        (enrollment-rate summary, benefit-family tags, HRIS connection,
        benefit-lifecycle stage) merged with the employer's flat CRM fields (legal name,
        EIN, contact, address, timestamps). The book is derived from the authenticated
        principal: one organization's employers, or every organization's for a caller
        whose reach is not a single organization. Supports name search,
        benefit-family/lifecycle/HRIS filters, and page/limit pagination.

        Args:
          benefit_family: Filter to employers with at least one active benefit in these families.

          benefit_lifecycle_stage: Filter to employers in one of these computed benefit-lifecycle stages.

          hris_provider: Filter to employers whose HRIS connection is with one of these payroll providers
              (e.g. `ADP RUN`). Matched case-insensitively; free text, so read the available
              values from the HRIS-providers endpoint rather than assuming a fixed set.

          hris_status: Filter to employers whose HRIS connection is in one of these statuses.

          include_cancelled: Include cancelled employers (hidden by default unless their stage is explicitly
              requested).

          limit: Items per page.

          page: Page number.

          search: Case-insensitive employer-name substring filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/employers",
            page=AsyncPageNumberPage[EmployerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "benefit_family": benefit_family,
                        "benefit_lifecycle_stage": benefit_lifecycle_stage,
                        "hris_provider": hris_provider,
                        "hris_status": hris_status,
                        "include_cancelled": include_cancelled,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    employer_list_params.EmployerListParams,
                ),
            ),
            model=EmployerListResponse,
        )

    async def ensure_payroll_integration_email(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerEnsurePayrollIntegrationEmailResponse:
        """
        Provision and return the employer's payroll integration email.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._put(
            path_template("/v1/employers/{employer_id}/payroll-integration-email", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerEnsurePayrollIntegrationEmailResponse,
        )

    def list_benefit_plan_year_enrollments(
        self,
        benefit_plan_year_id: str,
        *,
        employer_id: str,
        election_status: List[Literal["Enrolled", "Expired", "Pending", "Waived"]] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        EmployerListBenefitPlanYearEnrollmentsResponse,
        AsyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse],
    ]:
        """
        Returns a paginated list of every member with an enrollment in one of an
        employer's plan years, any election status: what they elected, where their
        coverage stands, dependent count, carrier, plan, tier, and the plan's total
        monthly cost. The caller must be authorized for the employer `empr_<...>`; an
        unknown or unauthorized employer, or an unknown plan year `plyr_<...>`,
        returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          benefit_plan_year_id: Unique benefit-plan-year identifier (plyr\\__\\**).

          election_status: Filter by election status. Repeat the parameter to match several.

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          search: Case-insensitive search. Matches member name partially, and the `member_id`
              exactly — either your own reference id or the prefixed `grpmbr_<...>` id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        if not benefit_plan_year_id:
            raise ValueError(
                f"Expected a non-empty value for `benefit_plan_year_id` but received {benefit_plan_year_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/v1/employers/{employer_id}/benefit-plan-years/{benefit_plan_year_id}/enrollments",
                employer_id=employer_id,
                benefit_plan_year_id=benefit_plan_year_id,
            ),
            page=AsyncPageNumberPage[EmployerListBenefitPlanYearEnrollmentsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "election_status": election_status,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    employer_list_benefit_plan_year_enrollments_params.EmployerListBenefitPlanYearEnrollmentsParams,
                ),
            ),
            model=EmployerListBenefitPlanYearEnrollmentsResponse,
        )

    async def list_benefit_plan_years(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListBenefitPlanYearsResponse:
        """
        Returns the employer's benefit plan years (all years, or one when `year` is
        given), each with its benefits, offered states, benefit families, and the
        year-level enrollment roll-up. The caller must be authorized for the employer;
        an unknown or unauthorized employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            path_template("/v1/employers/{employer_id}/benefit-plan-years", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerListBenefitPlanYearsResponse,
        )

    def list_employees(
        self,
        employer_id: str,
        *,
        employment_status: Literal["active", "terminated"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Employee, AsyncPageNumberPage[Employee]]:
        """Retrieves a paginated list of employees for a specific employer.

        The caller must
        be authorized for the employer; an unknown or unauthorized employer returns 404.
        Results are paginated using page and limit parameters and can be narrowed with a
        case-insensitive `search` (first name, last name, or email) and an
        `employment_status` filter (active or terminated). Each employee includes
        payroll deductions from the most recent statement period. When a new deduction
        statement is generated, previous period deductions are replaced.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          employment_status: Filter by employment status (active or terminated)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          search: Case-insensitive search across employee first name, last name, and email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get_api_list(
            path_template("/v1/employers/{employer_id}/employees", employer_id=employer_id),
            page=AsyncPageNumberPage[Employee],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employment_status": employment_status,
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    employer_list_employees_params.EmployerListEmployeesParams,
                ),
            ),
            model=Employee,
        )

    async def list_hris_providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListHRISProvidersResponse:
        """
        Returns the distinct HRIS/payroll providers across the same book
        `GET /v1/employers` returns, sorted for display. Use these as the values for the
        employers list's `hris_provider` filter — the providers are free text, so they
        cannot be enumerated in advance.
        """
        return await self._get(
            "/v1/employers/hris-providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerListHRISProvidersResponse,
        )

    async def list_invoices(
        self,
        employer_id: str,
        *,
        limit: int | Omit = omit,
        offset: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListInvoicesResponse:
        """Returns a cursor-paginated page of the employer's billing invoices, newest
        first.

        Pass the `next_offset` from a previous page as `offset` to fetch the next
        page. The caller must be authorized for the employer; an unknown or unauthorized
        employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          limit: Maximum number of invoices per page

          offset: Opaque cursor from a previous page's next_offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            path_template("/v1/employers/{employer_id}/invoices", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    employer_list_invoices_params.EmployerListInvoicesParams,
                ),
            ),
            cast_to=EmployerListInvoicesResponse,
        )

    def list_payroll_deduction_statements(
        self,
        employer_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        EmployerListPayrollDeductionStatementsResponse,
        AsyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse],
    ]:
        """
        Returns a paginated list of the employer's payroll-deduction statements, newest
        period first, each with its period, generation date, distinct employee count,
        total deduction, change-file link, and deduction frequency. Statements
        superseded by a later correction are excluded. The caller must be authorized for
        the employer; an unknown or unauthorized employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          limit: Maximum number of statements per page

          page: Page number to retrieve (starts at 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get_api_list(
            path_template("/v1/employers/{employer_id}/payroll-deduction-statements", employer_id=employer_id),
            page=AsyncPageNumberPage[EmployerListPayrollDeductionStatementsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    employer_list_payroll_deduction_statements_params.EmployerListPayrollDeductionStatementsParams,
                ),
            ),
            model=EmployerListPayrollDeductionStatementsResponse,
        )

    async def retrieve_benefit_plan_year(
        self,
        benefit_plan_year_id: str,
        *,
        employer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrieveBenefitPlanYearResponse:
        """
        Returns one benefit plan year in full — its benefit details plus the per-benefit
        enrollment rate and SPD link — addressed by its `benefit_plan_year_id`. The
        caller must be authorized for the employer; an unknown or unauthorized plan year
        returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          benefit_plan_year_id: Unique benefit-plan-year identifier (plyr\\__\\**).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        if not benefit_plan_year_id:
            raise ValueError(
                f"Expected a non-empty value for `benefit_plan_year_id` but received {benefit_plan_year_id!r}"
            )
        return await self._get(
            path_template(
                "/v1/employers/{employer_id}/benefit-plan-years/{benefit_plan_year_id}",
                employer_id=employer_id,
                benefit_plan_year_id=benefit_plan_year_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveBenefitPlanYearResponse,
        )

    async def retrieve_hris(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrieveHRISResponse:
        """
        Returns the employer's HRIS connection — provider, status, last sync, and synced
        row count — or null when the employer has no integration. The caller must be
        authorized for the employer; an unknown or unauthorized employer returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            path_template("/v1/employers/{employer_id}/hris", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveHRISResponse,
        )

    async def retrieve_invoice_pdf(
        self,
        invoice_id: str,
        *,
        employer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrieveInvoicePdfResponse:
        """
        Returns the time-limited PDF download link for a single invoice belonging to the
        employer's billing customer. `invoice_id` is the external Chargebee id (not a
        prefixed UUID). The caller must be authorized for the employer; an unknown or
        unauthorized employer or invoice returns 404.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          invoice_id: External Chargebee invoice id (not a prefixed UUID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._get(
            path_template(
                "/v1/employers/{employer_id}/invoices/{invoice_id}/pdf", employer_id=employer_id, invoice_id=invoice_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrieveInvoicePdfResponse,
        )

    async def retrieve_payroll_access_setup(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerRetrievePayrollAccessSetupResponse:
        """
        Return whether the employer has submitted payroll access setup.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            path_template("/v1/employers/{employer_id}/payroll-access-setup", employer_id=employer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerRetrievePayrollAccessSetupResponse,
        )

    async def submit_census_sync(
        self,
        employer_id: str,
        *,
        employees: Iterable[employer_submit_census_sync_params.Employee],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerSubmitCensusSyncResponse:
        """Submits a census sync payload for the specified employer.

        The employees in the
        payload will be queued for processing. Returns an accepted response with the
        timestamp of acceptance.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._post(
            path_template("/v1/employers/{employer_id}/census-sync", employer_id=employer_id),
            body=await async_maybe_transform(
                {"employees": employees}, employer_submit_census_sync_params.EmployerSubmitCensusSyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerSubmitCensusSyncResponse,
        )

    async def submit_payroll_access_setup(
        self,
        employer_id: str,
        *,
        access_method: Literal["SELF_SETUP", "NEEDS_HELP"],
        all_benefit_eligible_employees_present: bool,
        classifications_accurate: bool,
        employees_in_payroll_acknowledged: bool,
        has_additional_payroll_system: bool,
        is_controlled_group: bool,
        payroll_data_impacts_eligibility_acknowledged: bool,
        additional_access_method: Optional[Literal["SELF_SETUP", "NEEDS_HELP"]] | Omit = omit,
        additional_integration_confirmed: Optional[bool] | Omit = omit,
        additional_login_url: Optional[str] | Omit = omit,
        additional_password: Optional[str] | Omit = omit,
        additional_phone: Optional[str] | Omit = omit,
        additional_username: Optional[str] | Omit = omit,
        classification_correction_source: Optional[Literal["ENTER_NAMES", "EMAIL_LIST"]] | Omit = omit,
        integration_confirmed: Optional[bool] | Omit = omit,
        login_url: Optional[str] | Omit = omit,
        misclassified_employee_names: SequenceNotStr[str] | Omit = omit,
        missing_employee_resolution: Optional[Literal["EMAIL_CENSUS", "SECOND_SYSTEM_ACCESS"]] | Omit = omit,
        password: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        remaining_employee_action: Optional[Literal["VITABLE_UPDATE", "EMPLOYER_UPDATE"]] | Omit = omit,
        same_payroll_covers_other_eins: Optional[bool] | Omit = omit,
        username: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerSubmitPayrollAccessSetupResponse:
        """
        Submit the employer's payroll access setup answers.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          access_method: - `SELF_SETUP` - SELF_SETUP
              - `NEEDS_HELP` - NEEDS_HELP

          additional_access_method: - `SELF_SETUP` - SELF_SETUP
              - `NEEDS_HELP` - NEEDS_HELP

          classification_correction_source: - `ENTER_NAMES` - ENTER_NAMES
              - `EMAIL_LIST` - EMAIL_LIST

          missing_employee_resolution: - `EMAIL_CENSUS` - EMAIL_CENSUS
              - `SECOND_SYSTEM_ACCESS` - SECOND_SYSTEM_ACCESS

          remaining_employee_action: - `VITABLE_UPDATE` - VITABLE_UPDATE
              - `EMPLOYER_UPDATE` - EMPLOYER_UPDATE

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._put(
            path_template("/v1/employers/{employer_id}/payroll-access-setup", employer_id=employer_id),
            body=await async_maybe_transform(
                {
                    "access_method": access_method,
                    "all_benefit_eligible_employees_present": all_benefit_eligible_employees_present,
                    "classifications_accurate": classifications_accurate,
                    "employees_in_payroll_acknowledged": employees_in_payroll_acknowledged,
                    "has_additional_payroll_system": has_additional_payroll_system,
                    "is_controlled_group": is_controlled_group,
                    "payroll_data_impacts_eligibility_acknowledged": payroll_data_impacts_eligibility_acknowledged,
                    "additional_access_method": additional_access_method,
                    "additional_integration_confirmed": additional_integration_confirmed,
                    "additional_login_url": additional_login_url,
                    "additional_password": additional_password,
                    "additional_phone": additional_phone,
                    "additional_username": additional_username,
                    "classification_correction_source": classification_correction_source,
                    "integration_confirmed": integration_confirmed,
                    "login_url": login_url,
                    "misclassified_employee_names": misclassified_employee_names,
                    "missing_employee_resolution": missing_employee_resolution,
                    "password": password,
                    "phone": phone,
                    "remaining_employee_action": remaining_employee_action,
                    "same_payroll_covers_other_eins": same_payroll_covers_other_eins,
                    "username": username,
                },
                employer_submit_payroll_access_setup_params.EmployerSubmitPayrollAccessSetupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerSubmitPayrollAccessSetupResponse,
        )

    async def update_settings(
        self,
        employer_id: str,
        *,
        pay_frequency: Literal["weekly", "bi_weekly", "semi_monthly", "monthly"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerUpdateSettingsResponse:
        """Updates configuration settings for a specific employer.

        The employer must belong
        to the authenticated organization.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          pay_frequency: - `weekly` - Weekly
              - `bi_weekly` - Bi Weekly
              - `semi_monthly` - Semi Monthly
              - `monthly` - Monthly

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._put(
            path_template("/v1/employers/{employer_id}/settings", employer_id=employer_id),
            body=await async_maybe_transform(
                {"pay_frequency": pay_frequency}, employer_update_settings_params.EmployerUpdateSettingsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerUpdateSettingsResponse,
        )


class EmployersResourceWithRawResponse:
    def __init__(self, employers: EmployersResource) -> None:
        self._employers = employers

        self.create = to_raw_response_wrapper(
            employers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employers.update,
        )
        self.list = to_raw_response_wrapper(
            employers.list,
        )
        self.ensure_payroll_integration_email = to_raw_response_wrapper(
            employers.ensure_payroll_integration_email,
        )
        self.list_benefit_plan_year_enrollments = to_raw_response_wrapper(
            employers.list_benefit_plan_year_enrollments,
        )
        self.list_benefit_plan_years = to_raw_response_wrapper(
            employers.list_benefit_plan_years,
        )
        self.list_employees = to_raw_response_wrapper(
            employers.list_employees,
        )
        self.list_hris_providers = to_raw_response_wrapper(
            employers.list_hris_providers,
        )
        self.list_invoices = to_raw_response_wrapper(
            employers.list_invoices,
        )
        self.list_payroll_deduction_statements = to_raw_response_wrapper(
            employers.list_payroll_deduction_statements,
        )
        self.retrieve_benefit_plan_year = to_raw_response_wrapper(
            employers.retrieve_benefit_plan_year,
        )
        self.retrieve_hris = to_raw_response_wrapper(
            employers.retrieve_hris,
        )
        self.retrieve_invoice_pdf = to_raw_response_wrapper(
            employers.retrieve_invoice_pdf,
        )
        self.retrieve_payroll_access_setup = to_raw_response_wrapper(
            employers.retrieve_payroll_access_setup,
        )
        self.submit_census_sync = to_raw_response_wrapper(
            employers.submit_census_sync,
        )
        self.submit_payroll_access_setup = to_raw_response_wrapper(
            employers.submit_payroll_access_setup,
        )
        self.update_settings = to_raw_response_wrapper(
            employers.update_settings,
        )


class AsyncEmployersResourceWithRawResponse:
    def __init__(self, employers: AsyncEmployersResource) -> None:
        self._employers = employers

        self.create = async_to_raw_response_wrapper(
            employers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employers.update,
        )
        self.list = async_to_raw_response_wrapper(
            employers.list,
        )
        self.ensure_payroll_integration_email = async_to_raw_response_wrapper(
            employers.ensure_payroll_integration_email,
        )
        self.list_benefit_plan_year_enrollments = async_to_raw_response_wrapper(
            employers.list_benefit_plan_year_enrollments,
        )
        self.list_benefit_plan_years = async_to_raw_response_wrapper(
            employers.list_benefit_plan_years,
        )
        self.list_employees = async_to_raw_response_wrapper(
            employers.list_employees,
        )
        self.list_hris_providers = async_to_raw_response_wrapper(
            employers.list_hris_providers,
        )
        self.list_invoices = async_to_raw_response_wrapper(
            employers.list_invoices,
        )
        self.list_payroll_deduction_statements = async_to_raw_response_wrapper(
            employers.list_payroll_deduction_statements,
        )
        self.retrieve_benefit_plan_year = async_to_raw_response_wrapper(
            employers.retrieve_benefit_plan_year,
        )
        self.retrieve_hris = async_to_raw_response_wrapper(
            employers.retrieve_hris,
        )
        self.retrieve_invoice_pdf = async_to_raw_response_wrapper(
            employers.retrieve_invoice_pdf,
        )
        self.retrieve_payroll_access_setup = async_to_raw_response_wrapper(
            employers.retrieve_payroll_access_setup,
        )
        self.submit_census_sync = async_to_raw_response_wrapper(
            employers.submit_census_sync,
        )
        self.submit_payroll_access_setup = async_to_raw_response_wrapper(
            employers.submit_payroll_access_setup,
        )
        self.update_settings = async_to_raw_response_wrapper(
            employers.update_settings,
        )


class EmployersResourceWithStreamingResponse:
    def __init__(self, employers: EmployersResource) -> None:
        self._employers = employers

        self.create = to_streamed_response_wrapper(
            employers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employers.update,
        )
        self.list = to_streamed_response_wrapper(
            employers.list,
        )
        self.ensure_payroll_integration_email = to_streamed_response_wrapper(
            employers.ensure_payroll_integration_email,
        )
        self.list_benefit_plan_year_enrollments = to_streamed_response_wrapper(
            employers.list_benefit_plan_year_enrollments,
        )
        self.list_benefit_plan_years = to_streamed_response_wrapper(
            employers.list_benefit_plan_years,
        )
        self.list_employees = to_streamed_response_wrapper(
            employers.list_employees,
        )
        self.list_hris_providers = to_streamed_response_wrapper(
            employers.list_hris_providers,
        )
        self.list_invoices = to_streamed_response_wrapper(
            employers.list_invoices,
        )
        self.list_payroll_deduction_statements = to_streamed_response_wrapper(
            employers.list_payroll_deduction_statements,
        )
        self.retrieve_benefit_plan_year = to_streamed_response_wrapper(
            employers.retrieve_benefit_plan_year,
        )
        self.retrieve_hris = to_streamed_response_wrapper(
            employers.retrieve_hris,
        )
        self.retrieve_invoice_pdf = to_streamed_response_wrapper(
            employers.retrieve_invoice_pdf,
        )
        self.retrieve_payroll_access_setup = to_streamed_response_wrapper(
            employers.retrieve_payroll_access_setup,
        )
        self.submit_census_sync = to_streamed_response_wrapper(
            employers.submit_census_sync,
        )
        self.submit_payroll_access_setup = to_streamed_response_wrapper(
            employers.submit_payroll_access_setup,
        )
        self.update_settings = to_streamed_response_wrapper(
            employers.update_settings,
        )


class AsyncEmployersResourceWithStreamingResponse:
    def __init__(self, employers: AsyncEmployersResource) -> None:
        self._employers = employers

        self.create = async_to_streamed_response_wrapper(
            employers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            employers.list,
        )
        self.ensure_payroll_integration_email = async_to_streamed_response_wrapper(
            employers.ensure_payroll_integration_email,
        )
        self.list_benefit_plan_year_enrollments = async_to_streamed_response_wrapper(
            employers.list_benefit_plan_year_enrollments,
        )
        self.list_benefit_plan_years = async_to_streamed_response_wrapper(
            employers.list_benefit_plan_years,
        )
        self.list_employees = async_to_streamed_response_wrapper(
            employers.list_employees,
        )
        self.list_hris_providers = async_to_streamed_response_wrapper(
            employers.list_hris_providers,
        )
        self.list_invoices = async_to_streamed_response_wrapper(
            employers.list_invoices,
        )
        self.list_payroll_deduction_statements = async_to_streamed_response_wrapper(
            employers.list_payroll_deduction_statements,
        )
        self.retrieve_benefit_plan_year = async_to_streamed_response_wrapper(
            employers.retrieve_benefit_plan_year,
        )
        self.retrieve_hris = async_to_streamed_response_wrapper(
            employers.retrieve_hris,
        )
        self.retrieve_invoice_pdf = async_to_streamed_response_wrapper(
            employers.retrieve_invoice_pdf,
        )
        self.retrieve_payroll_access_setup = async_to_streamed_response_wrapper(
            employers.retrieve_payroll_access_setup,
        )
        self.submit_census_sync = async_to_streamed_response_wrapper(
            employers.submit_census_sync,
        )
        self.submit_payroll_access_setup = async_to_streamed_response_wrapper(
            employers.submit_payroll_access_setup,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            employers.update_settings,
        )
