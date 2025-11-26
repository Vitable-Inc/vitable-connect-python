# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

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
from ...types.employees import enrollment_list_params, enrollment_elect_params
from ...types.employees.enrollment_list_response import EnrollmentListResponse
from ...types.employees.enrollment_elect_response import EnrollmentElectResponse

__all__ = ["EnrollmentsResource", "AsyncEnrollmentsResource"]


class EnrollmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return EnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return EnrollmentsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        status: Literal["pending", "enrolled", "waived", "inactive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentListResponse:
        """
        Gets the Enrollments (pending, enrolled, or inactive) for a specific Employee
        with additional filters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employees/{id}/enrollments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, enrollment_list_params.EnrollmentListParams),
            ),
            cast_to=EnrollmentListResponse,
        )

    def elect(
        self,
        id: str,
        *,
        elections: Iterable[enrollment_elect_params.Election],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentElectResponse:
        """Benefits election process of all pending enrollments.

        Consists of all pending
        enrollments, whether enrolled/waived, and IDs of the dependents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/employees/{id}/enrollments/elect",
            body=maybe_transform({"elections": elections}, enrollment_elect_params.EnrollmentElectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentElectResponse,
        )


class AsyncEnrollmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrollmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrollmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncEnrollmentsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        status: Literal["pending", "enrolled", "waived", "inactive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentListResponse:
        """
        Gets the Enrollments (pending, enrolled, or inactive) for a specific Employee
        with additional filters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employees/{id}/enrollments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, enrollment_list_params.EnrollmentListParams),
            ),
            cast_to=EnrollmentListResponse,
        )

    async def elect(
        self,
        id: str,
        *,
        elections: Iterable[enrollment_elect_params.Election],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentElectResponse:
        """Benefits election process of all pending enrollments.

        Consists of all pending
        enrollments, whether enrolled/waived, and IDs of the dependents.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/employees/{id}/enrollments/elect",
            body=await async_maybe_transform({"elections": elections}, enrollment_elect_params.EnrollmentElectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentElectResponse,
        )


class EnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = to_raw_response_wrapper(
            enrollments.list,
        )
        self.elect = to_raw_response_wrapper(
            enrollments.elect,
        )


class AsyncEnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = async_to_raw_response_wrapper(
            enrollments.list,
        )
        self.elect = async_to_raw_response_wrapper(
            enrollments.elect,
        )


class EnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = to_streamed_response_wrapper(
            enrollments.list,
        )
        self.elect = to_streamed_response_wrapper(
            enrollments.elect,
        )


class AsyncEnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.list = async_to_streamed_response_wrapper(
            enrollments.list,
        )
        self.elect = async_to_streamed_response_wrapper(
            enrollments.elect,
        )
