# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ...types import employee_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .enrollments import (
    EnrollmentsResource,
    AsyncEnrollmentsResource,
    EnrollmentsResourceWithRawResponse,
    AsyncEnrollmentsResourceWithRawResponse,
    EnrollmentsResourceWithStreamingResponse,
    AsyncEnrollmentsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.employee import Employee
from ...types.employers import EmployeeClass
from ...types.employers.employee_class import EmployeeClass

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def enrollments(self) -> EnrollmentsResource:
        return EnrollmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
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
    ) -> Employee:
        """Retrieves detailed information for a specific employee by ID.

        Returns employee
        details including personal information and employment status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._get(
            f"/v1/employees/{employee_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def update(
        self,
        employee_id: str,
        *,
        address: Optional[employee_update_params.Address] | Omit = omit,
        email: Optional[str] | Omit = omit,
        employee_class: Optional[EmployeeClass] | Omit = omit,
        gender: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        termination_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """Updates an existing employee's information.

        All fields are optional - only
        provided fields will be updated. Note: SSN, name, date of birth, and sex cannot
        be changed after creation.

        Args:
          address: Employee's residential address

          email: Email address

          employee_class: - `Full Time` - Full Time
              - `Part Time` - Part Time
              - `Temporary` - Temporary
              - `Intern` - Intern
              - `Seasonal` - Seasonal
              - `Individual Contractor` - Individual Contractor

          gender: Gender identity

          phone: Phone number

          termination_date: Termination date if terminating

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._put(
            f"/v1/employees/{employee_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "email": email,
                    "employee_class": employee_class,
                    "gender": gender,
                    "phone": phone,
                    "termination_date": termination_date,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def terminate(
        self,
        employee_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Terminates a specific employee.

        This sets the employee's active status to false
        and records a termination date. The employee record is not permanently deleted
        for compliance reasons.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/employees/{employee_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResource:
        return AsyncEnrollmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
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
    ) -> Employee:
        """Retrieves detailed information for a specific employee by ID.

        Returns employee
        details including personal information and employment status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return await self._get(
            f"/v1/employees/{employee_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def update(
        self,
        employee_id: str,
        *,
        address: Optional[employee_update_params.Address] | Omit = omit,
        email: Optional[str] | Omit = omit,
        employee_class: Optional[EmployeeClass] | Omit = omit,
        gender: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        termination_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """Updates an existing employee's information.

        All fields are optional - only
        provided fields will be updated. Note: SSN, name, date of birth, and sex cannot
        be changed after creation.

        Args:
          address: Employee's residential address

          email: Email address

          employee_class: - `Full Time` - Full Time
              - `Part Time` - Part Time
              - `Temporary` - Temporary
              - `Intern` - Intern
              - `Seasonal` - Seasonal
              - `Individual Contractor` - Individual Contractor

          gender: Gender identity

          phone: Phone number

          termination_date: Termination date if terminating

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return await self._put(
            f"/v1/employees/{employee_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "email": email,
                    "employee_class": employee_class,
                    "gender": gender,
                    "phone": phone,
                    "termination_date": termination_date,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def terminate(
        self,
        employee_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Terminates a specific employee.

        This sets the employee's active status to false
        and records a termination date. The employee record is not permanently deleted
        for compliance reasons.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/employees/{employee_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        self.terminate = to_raw_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithRawResponse:
        return EnrollmentsResourceWithRawResponse(self._employees.enrollments)


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employees.update,
        )
        self.terminate = async_to_raw_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithRawResponse:
        return AsyncEnrollmentsResourceWithRawResponse(self._employees.enrollments)


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employees.update,
        )
        self.terminate = to_streamed_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithStreamingResponse:
        return EnrollmentsResourceWithStreamingResponse(self._employees.enrollments)


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employees.update,
        )
        self.terminate = async_to_streamed_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        return AsyncEnrollmentsResourceWithStreamingResponse(self._employees.enrollments)
