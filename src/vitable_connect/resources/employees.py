# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import employee_list_enrollments_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.employee_retrieve_response import EmployeeRetrieveResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
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
            cast_to=EmployeeRetrieveResponse,
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
            f"/v1/employees/{employee_id}/enrollments",
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

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
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
            cast_to=EmployeeRetrieveResponse,
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
            f"/v1/employees/{employee_id}/enrollments",
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
        self.list_enrollments = to_raw_response_wrapper(
            employees.list_enrollments,
        )


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_raw_response_wrapper(
            employees.retrieve,
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
        self.list_enrollments = to_streamed_response_wrapper(
            employees.list_enrollments,
        )


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.list_enrollments = async_to_streamed_response_wrapper(
            employees.list_enrollments,
        )
