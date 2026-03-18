# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.employee_response import EmployeeResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    """Manage employee records for employers"""

    @cached_property
    def enrollments(self) -> EnrollmentsResource:
        """Manage benefit enrollments and elections for employees"""
        return EnrollmentsResource(self._client)

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
    ) -> EmployeeResponse:
        """Retrieves detailed information for a specific employee by ID.

        Returns employee
        details including personal information and employment status.

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
            f"/v1/employees/{employee_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeResponse,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    """Manage employee records for employers"""

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResource:
        """Manage benefit enrollments and elections for employees"""
        return AsyncEnrollmentsResource(self._client)

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
    ) -> EmployeeResponse:
        """Retrieves detailed information for a specific employee by ID.

        Returns employee
        details including personal information and employment status.

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
            f"/v1/employees/{employee_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeResponse,
        )


class EmployeesResourceWithRawResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_raw_response_wrapper(
            employees.retrieve,
        )

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithRawResponse:
        """Manage benefit enrollments and elections for employees"""
        return EnrollmentsResourceWithRawResponse(self._employees.enrollments)


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_raw_response_wrapper(
            employees.retrieve,
        )

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithRawResponse:
        """Manage benefit enrollments and elections for employees"""
        return AsyncEnrollmentsResourceWithRawResponse(self._employees.enrollments)


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_streamed_response_wrapper(
            employees.retrieve,
        )

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithStreamingResponse:
        """Manage benefit enrollments and elections for employees"""
        return EnrollmentsResourceWithStreamingResponse(self._employees.enrollments)


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_streamed_response_wrapper(
            employees.retrieve,
        )

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        """Manage benefit enrollments and elections for employees"""
        return AsyncEnrollmentsResourceWithStreamingResponse(self._employees.enrollments)
