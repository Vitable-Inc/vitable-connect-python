# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import EmployeeClass, employee_update_params, employee_list_enrollments_params
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
from ..types.enrollment import Enrollment
from ..types.employee_class import EmployeeClass
from ..types.employee_update_response import EmployeeUpdateResponse
from ..types.employee_retrieve_response import EmployeeRetrieveResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return EmployeesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        employee_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeRetrieveResponse:
        """Retrieves detailed information for a specific employee by ID.

        Returns employee
        details including personal information, employment status, classification and
        compensation-type effective dates, compensation type, and payroll deductions
        from the most recent statement period. Deductions reflect a snapshot of the
        current period and are replaced when a new statement is generated.

        Args:
          employee_id: Unique employee identifier (empl\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._get(
            path_template("/v1/employees/{employee_id}", employee_id=employee_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeRetrieveResponse,
        )

    def update(
        self,
        employee_id: str,
        *,
        effective_date: Union[str, date],
        address: Optional[employee_update_params.Address] | Omit = omit,
        compensation_type: Optional[Literal["Salary", "Hourly"]] | Omit = omit,
        email: Optional[str] | Omit = omit,
        employee_class: Optional[EmployeeClass] | Omit = omit,
        gender: Optional[Literal["Male", "Female", "Transgender", "Non-binary", "Prefer not to respond"]] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeUpdateResponse:
        """Updates employee personal, contact, address, and employment fields.

        This
        endpoint currently supports email, phone, gender, address, employee_class,
        start_date, and compensation_type. effective_date is required and applies to
        employee_class and compensation_type when those fields are included in the
        request.

        Args:
          employee_id: Unique employee identifier (empl\\__\\**)

          effective_date: Past or present date applied to each tracked employment field included in this
              request

          address: Employee's residential address

          compensation_type: - `Salary` - Salary
              - `Hourly` - Hourly

          email: Email address

          employee_class: - `Full Time` - Full Time
              - `Part Time` - Part Time
              - `Temporary` - Temporary
              - `Intern` - Intern
              - `Seasonal` - Seasonal
              - `Individual Contractor` - Individual Contractor

          gender: - `Male` - Male
              - `Female` - Female
              - `Transgender` - Transgender
              - `Non-binary` - Non-binary
              - `Prefer not to respond` - Prefer not to respond

          phone: Phone number

          start_date: Employment start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._patch(
            path_template("/v1/employees/{employee_id}", employee_id=employee_id),
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "address": address,
                    "compensation_type": compensation_type,
                    "email": email,
                    "employee_class": employee_class,
                    "gender": gender,
                    "phone": phone,
                    "start_date": start_date,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeUpdateResponse,
        )

    def list_enrollments(
        self,
        employee_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[Enrollment]:
        """
        Retrieves a paginated list of benefit enrollments for an employee.

        Args:
          employee_id: Unique employee identifier (empl\\__\\**)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._get_api_list(
            path_template("/v1/employees/{employee_id}/enrollments", employee_id=employee_id),
            page=SyncPageNumberPage[Enrollment],
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
                    employee_list_enrollments_params.EmployeeListEnrollmentsParams,
                ),
            ),
            model=Enrollment,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncEmployeesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        employee_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeRetrieveResponse:
        """Retrieves detailed information for a specific employee by ID.

        Returns employee
        details including personal information, employment status, classification and
        compensation-type effective dates, compensation type, and payroll deductions
        from the most recent statement period. Deductions reflect a snapshot of the
        current period and are replaced when a new statement is generated.

        Args:
          employee_id: Unique employee identifier (empl\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return await self._get(
            path_template("/v1/employees/{employee_id}", employee_id=employee_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeRetrieveResponse,
        )

    async def update(
        self,
        employee_id: str,
        *,
        effective_date: Union[str, date],
        address: Optional[employee_update_params.Address] | Omit = omit,
        compensation_type: Optional[Literal["Salary", "Hourly"]] | Omit = omit,
        email: Optional[str] | Omit = omit,
        employee_class: Optional[EmployeeClass] | Omit = omit,
        gender: Optional[Literal["Male", "Female", "Transgender", "Non-binary", "Prefer not to respond"]] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeUpdateResponse:
        """Updates employee personal, contact, address, and employment fields.

        This
        endpoint currently supports email, phone, gender, address, employee_class,
        start_date, and compensation_type. effective_date is required and applies to
        employee_class and compensation_type when those fields are included in the
        request.

        Args:
          employee_id: Unique employee identifier (empl\\__\\**)

          effective_date: Past or present date applied to each tracked employment field included in this
              request

          address: Employee's residential address

          compensation_type: - `Salary` - Salary
              - `Hourly` - Hourly

          email: Email address

          employee_class: - `Full Time` - Full Time
              - `Part Time` - Part Time
              - `Temporary` - Temporary
              - `Intern` - Intern
              - `Seasonal` - Seasonal
              - `Individual Contractor` - Individual Contractor

          gender: - `Male` - Male
              - `Female` - Female
              - `Transgender` - Transgender
              - `Non-binary` - Non-binary
              - `Prefer not to respond` - Prefer not to respond

          phone: Phone number

          start_date: Employment start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return await self._patch(
            path_template("/v1/employees/{employee_id}", employee_id=employee_id),
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "address": address,
                    "compensation_type": compensation_type,
                    "email": email,
                    "employee_class": employee_class,
                    "gender": gender,
                    "phone": phone,
                    "start_date": start_date,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeUpdateResponse,
        )

    def list_enrollments(
        self,
        employee_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Enrollment, AsyncPageNumberPage[Enrollment]]:
        """
        Retrieves a paginated list of benefit enrollments for an employee.

        Args:
          employee_id: Unique employee identifier (empl\\__\\**)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._get_api_list(
            path_template("/v1/employees/{employee_id}/enrollments", employee_id=employee_id),
            page=AsyncPageNumberPage[Enrollment],
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
                    employee_list_enrollments_params.EmployeeListEnrollmentsParams,
                ),
            ),
            model=Enrollment,
        )


class EmployeesResourceWithRawResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employees.update,
        )
        self.list_enrollments = to_raw_response_wrapper(
            employees.list_enrollments,
        )


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employees.update,
        )
        self.list_enrollments = async_to_raw_response_wrapper(
            employees.list_enrollments,
        )


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employees.update,
        )
        self.list_enrollments = to_streamed_response_wrapper(
            employees.list_enrollments,
        )


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employees.update,
        )
        self.list_enrollments = async_to_streamed_response_wrapper(
            employees.list_enrollments,
        )
