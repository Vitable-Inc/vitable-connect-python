# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    employer_list_params,
    employer_create_params,
    employer_list_employees_params,
    employer_update_settings_params,
    employer_submit_census_sync_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.employer_update_settings_response import EmployerUpdateSettingsResponse
from ..types.employer_submit_census_sync_response import EmployerSubmitCensusSyncResponse

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

    def list(
        self,
        *,
        benefit_family: List[Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]] | Omit = omit,
        benefit_lifecycle_stage: List[Literal["open_enrollment", "renewal", "active", "onboarding", "cancelled"]]
        | Omit = omit,
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
        Returns the caller's organization book — every employer with its computed
        columns (enrollment-rate summary, benefit-family tags, HRIS connection,
        benefit-lifecycle stage) merged with the employer's flat CRM fields (legal name,
        EIN, contact, address, timestamps). The organization is derived from the
        authenticated principal. Supports name search, benefit-family/lifecycle/HRIS
        filters, and page/limit pagination.

        Args:
          benefit_family: Filter to employers with at least one active benefit in these families.

          benefit_lifecycle_stage: Filter to employers in one of these computed benefit-lifecycle stages.

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

    def list_employees(
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
    ) -> SyncPageNumberPage[Employee]:
        """Retrieves a paginated list of all employees for a specific employer.

        Results are
        paginated using page and limit parameters. Each employee includes payroll
        deductions from the most recent statement period. When a new deduction statement
        is generated, previous period deductions are replaced.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

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
                        "limit": limit,
                        "page": page,
                    },
                    employer_list_employees_params.EmployerListEmployeesParams,
                ),
            ),
            model=Employee,
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

          pay_frequency: - `weekly` - weekly
              - `bi_weekly` - bi_weekly
              - `semi_monthly` - semi_monthly
              - `monthly` - monthly

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

    def list(
        self,
        *,
        benefit_family: List[Literal["mec", "mvp", "ichra", "vpc", "dental", "vision"]] | Omit = omit,
        benefit_lifecycle_stage: List[Literal["open_enrollment", "renewal", "active", "onboarding", "cancelled"]]
        | Omit = omit,
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
        Returns the caller's organization book — every employer with its computed
        columns (enrollment-rate summary, benefit-family tags, HRIS connection,
        benefit-lifecycle stage) merged with the employer's flat CRM fields (legal name,
        EIN, contact, address, timestamps). The organization is derived from the
        authenticated principal. Supports name search, benefit-family/lifecycle/HRIS
        filters, and page/limit pagination.

        Args:
          benefit_family: Filter to employers with at least one active benefit in these families.

          benefit_lifecycle_stage: Filter to employers in one of these computed benefit-lifecycle stages.

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

    def list_employees(
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
    ) -> AsyncPaginator[Employee, AsyncPageNumberPage[Employee]]:
        """Retrieves a paginated list of all employees for a specific employer.

        Results are
        paginated using page and limit parameters. Each employee includes payroll
        deductions from the most recent statement period. When a new deduction statement
        is generated, previous period deductions are replaced.

        Args:
          employer_id: Unique employer identifier (empr\\__\\**)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

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
                        "limit": limit,
                        "page": page,
                    },
                    employer_list_employees_params.EmployerListEmployeesParams,
                ),
            ),
            model=Employee,
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

          pay_frequency: - `weekly` - weekly
              - `bi_weekly` - bi_weekly
              - `semi_monthly` - semi_monthly
              - `monthly` - monthly

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
        self.list = to_raw_response_wrapper(
            employers.list,
        )
        self.list_employees = to_raw_response_wrapper(
            employers.list_employees,
        )
        self.submit_census_sync = to_raw_response_wrapper(
            employers.submit_census_sync,
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
        self.list = async_to_raw_response_wrapper(
            employers.list,
        )
        self.list_employees = async_to_raw_response_wrapper(
            employers.list_employees,
        )
        self.submit_census_sync = async_to_raw_response_wrapper(
            employers.submit_census_sync,
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
        self.list = to_streamed_response_wrapper(
            employers.list,
        )
        self.list_employees = to_streamed_response_wrapper(
            employers.list_employees,
        )
        self.submit_census_sync = to_streamed_response_wrapper(
            employers.submit_census_sync,
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
        self.list = async_to_streamed_response_wrapper(
            employers.list,
        )
        self.list_employees = async_to_streamed_response_wrapper(
            employers.list_employees,
        )
        self.submit_census_sync = async_to_streamed_response_wrapper(
            employers.submit_census_sync,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            employers.update_settings,
        )
