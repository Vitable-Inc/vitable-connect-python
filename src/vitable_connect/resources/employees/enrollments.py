# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.employees import enrollment_list_params
from ...types.employees.enrollment_list import EnrollmentList

__all__ = ["EnrollmentsResource", "AsyncEnrollmentsResource"]


class EnrollmentsResource(SyncAPIResource):
    """Manage benefit enrollments and elections for employees"""

    @cached_property
    def with_raw_response(self) -> EnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return EnrollmentsResourceWithStreamingResponse(self)

    def list(
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
    ) -> EnrollmentList:
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
        return self._get(
            f"/v1/employees/{employee_id}/enrollments",
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
                    enrollment_list_params.EnrollmentListParams,
                ),
            ),
            cast_to=EnrollmentList,
        )


class AsyncEnrollmentsResource(AsyncAPIResource):
    """Manage benefit enrollments and elections for employees"""

    @cached_property
    def with_raw_response(self) -> AsyncEnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncEnrollmentsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> EnrollmentList:
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
        return await self._get(
            f"/v1/employees/{employee_id}/enrollments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    enrollment_list_params.EnrollmentListParams,
                ),
            ),
            cast_to=EnrollmentList,
        )


class EnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = to_raw_response_wrapper(
            enrollments.list,
        )


class AsyncEnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = async_to_raw_response_wrapper(
            enrollments.list,
        )


class EnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = to_streamed_response_wrapper(
            enrollments.list,
        )


class AsyncEnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = async_to_streamed_response_wrapper(
            enrollments.list,
        )
