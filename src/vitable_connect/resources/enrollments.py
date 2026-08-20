# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import enrollment_reissue_params, enrollment_terminate_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.enrollment_reissue_response import EnrollmentReissueResponse
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
            path_template("/v1/enrollments/{enrollment_id}", enrollment_id=enrollment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentRetrieveResponse,
        )

    def reissue(
        self,
        enrollment_id: str,
        *,
        qualifying_life_event_id: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        ticket_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentReissueResponse:
        """
        Closes the targeted enrollment and creates a new unanswered enrollment for the
        same member and plan year. VPC never requires a qualifying life event; other
        products require an accepted, member-owned event outside open enrollment.
        User-backed callers must provide a reason; it is optional for userless
        organization callers. API keys and unbound access tokens may act across the
        caller organization's book. Employer-bound access tokens may act only on that
        employer's enrollments, and employee-bound access tokens may act only on that
        employee's enrollment. Tenant or token-scope mismatches return the same
        non-disclosing 404 before the request body is validated.

        Args:
          enrollment_id: Unique enrollment identifier (enrl\\__\\**)

          qualifying_life_event_id: Accepted member qualifying life event identifier (qle\\__\\**)

          reason: Audit reason for the reissue; required for user-backed callers and optional for
              userless organization callers

          ticket_number: Optional support or operational ticket number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enrollment_id:
            raise ValueError(f"Expected a non-empty value for `enrollment_id` but received {enrollment_id!r}")
        return self._post(
            path_template("/v1/enrollments/{enrollment_id}/reissue", enrollment_id=enrollment_id),
            body=maybe_transform(
                {
                    "qualifying_life_event_id": qualifying_life_event_id,
                    "reason": reason,
                    "ticket_number": ticket_number,
                },
                enrollment_reissue_params.EnrollmentReissueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentReissueResponse,
        )

    def terminate(
        self,
        enrollment_id: str,
        *,
        qualifying_life_event_id: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        ticket_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Terminates enrolled coverage immediately.

        An accepted qualifying life event
        owned by the enrollment member is required unless the plan is VPC or ICHRA.
        User-backed callers must provide a reason; it is optional for userless
        organization callers. API keys may act across the caller organization's book.
        Tenant mismatches return the same non-disclosing 404 before the request body is
        validated.

        Args:
          enrollment_id: Unique enrollment identifier (enrl\\__\\**)

          qualifying_life_event_id: Accepted member qualifying life event identifier (qle\\__\\**)

          reason: Audit reason for the termination; required for user-backed callers and optional
              for userless organization callers

          ticket_number: Optional support or operational ticket number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enrollment_id:
            raise ValueError(f"Expected a non-empty value for `enrollment_id` but received {enrollment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v1/enrollments/{enrollment_id}/terminate", enrollment_id=enrollment_id),
            body=maybe_transform(
                {
                    "qualifying_life_event_id": qualifying_life_event_id,
                    "reason": reason,
                    "ticket_number": ticket_number,
                },
                enrollment_terminate_params.EnrollmentTerminateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            path_template("/v1/enrollments/{enrollment_id}", enrollment_id=enrollment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentRetrieveResponse,
        )

    async def reissue(
        self,
        enrollment_id: str,
        *,
        qualifying_life_event_id: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        ticket_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrollmentReissueResponse:
        """
        Closes the targeted enrollment and creates a new unanswered enrollment for the
        same member and plan year. VPC never requires a qualifying life event; other
        products require an accepted, member-owned event outside open enrollment.
        User-backed callers must provide a reason; it is optional for userless
        organization callers. API keys and unbound access tokens may act across the
        caller organization's book. Employer-bound access tokens may act only on that
        employer's enrollments, and employee-bound access tokens may act only on that
        employee's enrollment. Tenant or token-scope mismatches return the same
        non-disclosing 404 before the request body is validated.

        Args:
          enrollment_id: Unique enrollment identifier (enrl\\__\\**)

          qualifying_life_event_id: Accepted member qualifying life event identifier (qle\\__\\**)

          reason: Audit reason for the reissue; required for user-backed callers and optional for
              userless organization callers

          ticket_number: Optional support or operational ticket number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enrollment_id:
            raise ValueError(f"Expected a non-empty value for `enrollment_id` but received {enrollment_id!r}")
        return await self._post(
            path_template("/v1/enrollments/{enrollment_id}/reissue", enrollment_id=enrollment_id),
            body=await async_maybe_transform(
                {
                    "qualifying_life_event_id": qualifying_life_event_id,
                    "reason": reason,
                    "ticket_number": ticket_number,
                },
                enrollment_reissue_params.EnrollmentReissueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnrollmentReissueResponse,
        )

    async def terminate(
        self,
        enrollment_id: str,
        *,
        qualifying_life_event_id: Optional[str] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        ticket_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Terminates enrolled coverage immediately.

        An accepted qualifying life event
        owned by the enrollment member is required unless the plan is VPC or ICHRA.
        User-backed callers must provide a reason; it is optional for userless
        organization callers. API keys may act across the caller organization's book.
        Tenant mismatches return the same non-disclosing 404 before the request body is
        validated.

        Args:
          enrollment_id: Unique enrollment identifier (enrl\\__\\**)

          qualifying_life_event_id: Accepted member qualifying life event identifier (qle\\__\\**)

          reason: Audit reason for the termination; required for user-backed callers and optional
              for userless organization callers

          ticket_number: Optional support or operational ticket number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enrollment_id:
            raise ValueError(f"Expected a non-empty value for `enrollment_id` but received {enrollment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/enrollments/{enrollment_id}/terminate", enrollment_id=enrollment_id),
            body=await async_maybe_transform(
                {
                    "qualifying_life_event_id": qualifying_life_event_id,
                    "reason": reason,
                    "ticket_number": ticket_number,
                },
                enrollment_terminate_params.EnrollmentTerminateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = to_raw_response_wrapper(
            enrollments.retrieve,
        )
        self.reissue = to_raw_response_wrapper(
            enrollments.reissue,
        )
        self.terminate = to_raw_response_wrapper(
            enrollments.terminate,
        )


class AsyncEnrollmentsResourceWithRawResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = async_to_raw_response_wrapper(
            enrollments.retrieve,
        )
        self.reissue = async_to_raw_response_wrapper(
            enrollments.reissue,
        )
        self.terminate = async_to_raw_response_wrapper(
            enrollments.terminate,
        )


class EnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: EnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = to_streamed_response_wrapper(
            enrollments.retrieve,
        )
        self.reissue = to_streamed_response_wrapper(
            enrollments.reissue,
        )
        self.terminate = to_streamed_response_wrapper(
            enrollments.terminate,
        )


class AsyncEnrollmentsResourceWithStreamingResponse:
    def __init__(self, enrollments: AsyncEnrollmentsResource) -> None:
        self._enrollments = enrollments

        self.retrieve = async_to_streamed_response_wrapper(
            enrollments.retrieve,
        )
        self.reissue = async_to_streamed_response_wrapper(
            enrollments.reissue,
        )
        self.terminate = async_to_streamed_response_wrapper(
            enrollments.terminate,
        )
