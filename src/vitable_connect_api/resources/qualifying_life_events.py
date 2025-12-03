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
from ..types.members.qualifying_life_event import QualifyingLifeEvent

__all__ = ["QualifyingLifeEventsResource", "AsyncQualifyingLifeEventsResource"]


class QualifyingLifeEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QualifyingLifeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return QualifyingLifeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualifyingLifeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return QualifyingLifeEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        qle_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEvent:
        """Retrieves detailed information for a specific QLE by ID.

        Returns event type,
        date, status, and enrollment window information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not qle_id:
            raise ValueError(f"Expected a non-empty value for `qle_id` but received {qle_id!r}")
        return self._get(
            f"/v1/qualifying-life-events/{qle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEvent,
        )


class AsyncQualifyingLifeEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQualifyingLifeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualifyingLifeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualifyingLifeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return AsyncQualifyingLifeEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        qle_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEvent:
        """Retrieves detailed information for a specific QLE by ID.

        Returns event type,
        date, status, and enrollment window information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not qle_id:
            raise ValueError(f"Expected a non-empty value for `qle_id` but received {qle_id!r}")
        return await self._get(
            f"/v1/qualifying-life-events/{qle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEvent,
        )


class QualifyingLifeEventsResourceWithRawResponse:
    def __init__(self, qualifying_life_events: QualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = to_raw_response_wrapper(
            qualifying_life_events.retrieve,
        )


class AsyncQualifyingLifeEventsResourceWithRawResponse:
    def __init__(self, qualifying_life_events: AsyncQualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = async_to_raw_response_wrapper(
            qualifying_life_events.retrieve,
        )


class QualifyingLifeEventsResourceWithStreamingResponse:
    def __init__(self, qualifying_life_events: QualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = to_streamed_response_wrapper(
            qualifying_life_events.retrieve,
        )


class AsyncQualifyingLifeEventsResourceWithStreamingResponse:
    def __init__(self, qualifying_life_events: AsyncQualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = async_to_streamed_response_wrapper(
            qualifying_life_events.retrieve,
        )
