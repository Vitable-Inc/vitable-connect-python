# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.enrollment_retrieve_response import EnrollmentRetrieveResponse

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

    def retrieve(
        self,
        enrollment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentRetrieveResponse:
        """
        Retrieves detailed information for a specific enrollment by ID.

        Args:
          enrollment_id: Unique enrollment identifier (enrl\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enrollment_id:
            raise ValueError(f"Expected a non-empty value for `enrollment_id` but received {enrollment_id!r}")
        return self._get(
            f"/v1/enrollments/{enrollment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentRetrieveResponse,
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

    async def retrieve(
        self,
        enrollment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentRetrieveResponse:
        """
        Retrieves detailed information for a specific enrollment by ID.

        Args:
          enrollment_id: Unique enrollment identifier (enrl\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enrollment_id:
            raise ValueError(f"Expected a non-empty value for `enrollment_id` but received {enrollment_id!r}")
        return await self._get(
            f"/v1/enrollments/{enrollment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentRetrieveResponse,
        )


class EnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = to_raw_response_wrapper(
            enrollments.retrieve,
        )


class AsyncEnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = async_to_raw_response_wrapper(
            enrollments.retrieve,
        )


class EnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = to_streamed_response_wrapper(
            enrollments.retrieve,
        )


class AsyncEnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = async_to_streamed_response_wrapper(
            enrollments.retrieve,
        )
