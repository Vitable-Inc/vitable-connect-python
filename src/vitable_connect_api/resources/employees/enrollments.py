# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.employees import EnrollmentStatus, enrollment_list_params, enrollment_submit_elections_params
from ...types.employees.enrollment_status import EnrollmentStatus
from ...types.employees.enrollment_list_response import EnrollmentListResponse
from ...types.employees.enrollment_submit_elections_response import EnrollmentSubmitElectionsResponse

__all__ = ["EnrollmentsResource", "AsyncEnrollmentsResource"]


class EnrollmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return EnrollmentsResourceWithStreamingResponse(self)

    def list(
        self,
        employee_id: str,
        *,
        coverage_effective_start_year: int | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        plan_year: int | Omit = omit,
        status: EnrollmentStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentListResponse:
        """Retrieves a paginated list of benefit enrollments for an employee.

        Enrollments
        have statuses: 'pending' (in enrollment period), 'enrolled' (active coverage),
        or 'inactive' (terminated, expired, or unanswered). Filter by status, plan year,
        or coverage year.

        Args:
          coverage_effective_start_year: Filter by coverage year

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          plan_year: Filter by plan year start (YYYY)

          status: Filter by enrollment status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._get(
            f"/v1/employees/{employee_id}/enrollments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coverage_effective_start_year": coverage_effective_start_year,
                        "limit": limit,
                        "page": page,
                        "plan_year": plan_year,
                        "status": status,
                    },
                    enrollment_list_params.EnrollmentListParams,
                ),
            ),
            cast_to=EnrollmentListResponse,
        )

    def submit_elections(
        self,
        employee_id: str,
        *,
        elections: Iterable[enrollment_submit_elections_params.Election],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentSubmitElectionsResponse:
        """
        Completes the benefits election process for all pending enrollments for an
        employee. Processes enrollment decisions: which benefits to enroll/waive, plan
        selections, and dependent coverage. Pending enrollments transition to enrolled
        or waived status based on elections.

        Args:
          elections: List of enrollment elections

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return self._post(
            f"/v1/employees/{employee_id}/enrollments/elect",
            body=maybe_transform(
                {"elections": elections}, enrollment_submit_elections_params.EnrollmentSubmitElectionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentSubmitElectionsResponse,
        )


class AsyncEnrollmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return AsyncEnrollmentsResourceWithStreamingResponse(self)

    async def list(
        self,
        employee_id: str,
        *,
        coverage_effective_start_year: int | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        plan_year: int | Omit = omit,
        status: EnrollmentStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentListResponse:
        """Retrieves a paginated list of benefit enrollments for an employee.

        Enrollments
        have statuses: 'pending' (in enrollment period), 'enrolled' (active coverage),
        or 'inactive' (terminated, expired, or unanswered). Filter by status, plan year,
        or coverage year.

        Args:
          coverage_effective_start_year: Filter by coverage year

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          plan_year: Filter by plan year start (YYYY)

          status: Filter by enrollment status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return await self._get(
            f"/v1/employees/{employee_id}/enrollments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coverage_effective_start_year": coverage_effective_start_year,
                        "limit": limit,
                        "page": page,
                        "plan_year": plan_year,
                        "status": status,
                    },
                    enrollment_list_params.EnrollmentListParams,
                ),
            ),
            cast_to=EnrollmentListResponse,
        )

    async def submit_elections(
        self,
        employee_id: str,
        *,
        elections: Iterable[enrollment_submit_elections_params.Election],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentSubmitElectionsResponse:
        """
        Completes the benefits election process for all pending enrollments for an
        employee. Processes enrollment decisions: which benefits to enroll/waive, plan
        selections, and dependent coverage. Pending enrollments transition to enrolled
        or waived status based on elections.

        Args:
          elections: List of enrollment elections

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employee_id:
            raise ValueError(f"Expected a non-empty value for `employee_id` but received {employee_id!r}")
        return await self._post(
            f"/v1/employees/{employee_id}/enrollments/elect",
            body=await async_maybe_transform(
                {"elections": elections}, enrollment_submit_elections_params.EnrollmentSubmitElectionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentSubmitElectionsResponse,
        )


class EnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = to_raw_response_wrapper(
            enrollments.list,
        )
        self.submit_elections = to_raw_response_wrapper(
            enrollments.submit_elections,
        )


class AsyncEnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = async_to_raw_response_wrapper(
            enrollments.list,
        )
        self.submit_elections = async_to_raw_response_wrapper(
            enrollments.submit_elections,
        )


class EnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = to_streamed_response_wrapper(
            enrollments.list,
        )
        self.submit_elections = to_streamed_response_wrapper(
            enrollments.submit_elections,
        )


class AsyncEnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = async_to_streamed_response_wrapper(
            enrollments.list,
        )
        self.submit_elections = async_to_streamed_response_wrapper(
            enrollments.submit_elections,
        )
