# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
from ...types.employees import qualifying_life_event_create_params
from ...types.qualifying_life_event import QualifyingLifeEvent
from ...types.employees.qualifying_life_event_list_response import QualifyingLifeEventListResponse

__all__ = ["QualifyingLifeEventsResource", "AsyncQualifyingLifeEventsResource"]


class QualifyingLifeEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QualifyingLifeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return QualifyingLifeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualifyingLifeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return QualifyingLifeEventsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        event_date: Union[str, date],
        event_type: Literal[
            "MARRIAGE",
            "BIRTH",
            "ADOPTION",
            "DIVORCE",
            "DEATH",
            "JOB_LOSS",
            "REDUCTION_IN_HOURS",
            "EMPLOYER_BANKRUPTCY",
            "MEDICARE_ENTITLEMENT",
            "TERMINATION",
            "OTHER",
        ],
        description: str | Omit = omit,
        proof_document_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEvent:
        """
        Creates a new Qualifying Life Event for an Employee.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/employees/{id}/qualifying-life-events",
            body=maybe_transform(
                {
                    "event_date": event_date,
                    "event_type": event_type,
                    "description": description,
                    "proof_document_url": proof_document_url,
                },
                qualifying_life_event_create_params.QualifyingLifeEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEvent,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventListResponse:
        """
        Gets all Qualifying Life Events for an Employee.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employees/{id}/qualifying-life-events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEventListResponse,
        )


class AsyncQualifyingLifeEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQualifyingLifeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualifyingLifeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualifyingLifeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncQualifyingLifeEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        event_date: Union[str, date],
        event_type: Literal[
            "MARRIAGE",
            "BIRTH",
            "ADOPTION",
            "DIVORCE",
            "DEATH",
            "JOB_LOSS",
            "REDUCTION_IN_HOURS",
            "EMPLOYER_BANKRUPTCY",
            "MEDICARE_ENTITLEMENT",
            "TERMINATION",
            "OTHER",
        ],
        description: str | Omit = omit,
        proof_document_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEvent:
        """
        Creates a new Qualifying Life Event for an Employee.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/employees/{id}/qualifying-life-events",
            body=await async_maybe_transform(
                {
                    "event_date": event_date,
                    "event_type": event_type,
                    "description": description,
                    "proof_document_url": proof_document_url,
                },
                qualifying_life_event_create_params.QualifyingLifeEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEvent,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventListResponse:
        """
        Gets all Qualifying Life Events for an Employee.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employees/{id}/qualifying-life-events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEventListResponse,
        )


class QualifyingLifeEventsResourceWithRawResponse:
    def __init__(self, qualifying_life_events: QualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.create = to_raw_response_wrapper(
            qualifying_life_events.create,
        )
        self.list = to_raw_response_wrapper(
            qualifying_life_events.list,
        )


class AsyncQualifyingLifeEventsResourceWithRawResponse:
    def __init__(self, qualifying_life_events: AsyncQualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.create = async_to_raw_response_wrapper(
            qualifying_life_events.create,
        )
        self.list = async_to_raw_response_wrapper(
            qualifying_life_events.list,
        )


class QualifyingLifeEventsResourceWithStreamingResponse:
    def __init__(self, qualifying_life_events: QualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.create = to_streamed_response_wrapper(
            qualifying_life_events.create,
        )
        self.list = to_streamed_response_wrapper(
            qualifying_life_events.list,
        )


class AsyncQualifyingLifeEventsResourceWithStreamingResponse:
    def __init__(self, qualifying_life_events: AsyncQualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.create = async_to_streamed_response_wrapper(
            qualifying_life_events.create,
        )
        self.list = async_to_streamed_response_wrapper(
            qualifying_life_events.list,
        )
