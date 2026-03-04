# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

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
from ...types.members import (
    EventType,
    QualifyingLifeEventStatus,
    qualifying_life_event_list_params,
    qualifying_life_event_record_params,
)
from ...types.members.event_type import EventType
from ...types.members.qualifying_life_event_status import QualifyingLifeEventStatus
from ...types.members.qualifying_life_event_response import QualifyingLifeEventResponse
from ...types.members.qualifying_life_event_list_response import QualifyingLifeEventListResponse

__all__ = ["QualifyingLifeEventsResource", "AsyncQualifyingLifeEventsResource"]


class QualifyingLifeEventsResource(SyncAPIResource):
    """Record life events that trigger special enrollment periods"""

    @cached_property
    def with_raw_response(self) -> QualifyingLifeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return QualifyingLifeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualifyingLifeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return QualifyingLifeEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        qle_id: str,
        *,
        member_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventResponse:
        """Retrieves detailed information for a specific QLE by ID.

        Returns event type,
        date, status, and enrollment window information.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          qle_id: Unique qualifying life event identifier (qle\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        if not qle_id:
            raise ValueError(f"Expected a non-empty value for `qle_id` but received {qle_id!r}")
        return self._get(
            f"/v1/members/{member_id}/qualifying-life-events/{qle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEventResponse,
        )

    def list(
        self,
        member_id: str,
        *,
        event_type: EventType | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: QualifyingLifeEventStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventListResponse:
        """Retrieves a paginated list of qualifying life events for a member.

        QLEs are
        significant life changes (marriage, birth, adoption, loss of coverage) that
        allow benefit enrollment changes outside open enrollment.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          event_type: Filter by QLE type

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          status: Filter by QLE status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            f"/v1/members/{member_id}/qualifying-life-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_type": event_type,
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    qualifying_life_event_list_params.QualifyingLifeEventListParams,
                ),
            ),
            cast_to=QualifyingLifeEventListResponse,
        )

    def record(
        self,
        member_id: str,
        *,
        event_date: Union[str, date],
        event_type: EventType,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventResponse:
        """Records a qualifying life event occurrence for a member.

        Opens a special
        enrollment period allowing benefit changes outside open enrollment. Employees
        typically have 30-60 days from the event date to complete enrollment changes.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          event_date: Date when the event occurred

          event_type: - `Marriage` - Marriage
              - `Birth` - Birth
              - `Adoption` - Adoption
              - `Divorce` - Divorce
              - `Death` - Death
              - `Job Loss` - Job Loss
              - `Reduction In Hours` - Reduction In Hours
              - `Employer Bankruptcy` - Employer Bankruptcy
              - `Medicare Entitlement` - Medicare Entitlement
              - `Termination` - Termination
              - `Other` - Other

          notes: Optional notes about the event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._post(
            f"/v1/members/{member_id}/qualifying-life-events",
            body=maybe_transform(
                {
                    "event_date": event_date,
                    "event_type": event_type,
                    "notes": notes,
                },
                qualifying_life_event_record_params.QualifyingLifeEventRecordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEventResponse,
        )


class AsyncQualifyingLifeEventsResource(AsyncAPIResource):
    """Record life events that trigger special enrollment periods"""

    @cached_property
    def with_raw_response(self) -> AsyncQualifyingLifeEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualifyingLifeEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualifyingLifeEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncQualifyingLifeEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        qle_id: str,
        *,
        member_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventResponse:
        """Retrieves detailed information for a specific QLE by ID.

        Returns event type,
        date, status, and enrollment window information.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          qle_id: Unique qualifying life event identifier (qle\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        if not qle_id:
            raise ValueError(f"Expected a non-empty value for `qle_id` but received {qle_id!r}")
        return await self._get(
            f"/v1/members/{member_id}/qualifying-life-events/{qle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEventResponse,
        )

    async def list(
        self,
        member_id: str,
        *,
        event_type: EventType | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: QualifyingLifeEventStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventListResponse:
        """Retrieves a paginated list of qualifying life events for a member.

        QLEs are
        significant life changes (marriage, birth, adoption, loss of coverage) that
        allow benefit enrollment changes outside open enrollment.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          event_type: Filter by QLE type

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          status: Filter by QLE status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            f"/v1/members/{member_id}/qualifying-life-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_type": event_type,
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    qualifying_life_event_list_params.QualifyingLifeEventListParams,
                ),
            ),
            cast_to=QualifyingLifeEventListResponse,
        )

    async def record(
        self,
        member_id: str,
        *,
        event_date: Union[str, date],
        event_type: EventType,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualifyingLifeEventResponse:
        """Records a qualifying life event occurrence for a member.

        Opens a special
        enrollment period allowing benefit changes outside open enrollment. Employees
        typically have 30-60 days from the event date to complete enrollment changes.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          event_date: Date when the event occurred

          event_type: - `Marriage` - Marriage
              - `Birth` - Birth
              - `Adoption` - Adoption
              - `Divorce` - Divorce
              - `Death` - Death
              - `Job Loss` - Job Loss
              - `Reduction In Hours` - Reduction In Hours
              - `Employer Bankruptcy` - Employer Bankruptcy
              - `Medicare Entitlement` - Medicare Entitlement
              - `Termination` - Termination
              - `Other` - Other

          notes: Optional notes about the event

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._post(
            f"/v1/members/{member_id}/qualifying-life-events",
            body=await async_maybe_transform(
                {
                    "event_date": event_date,
                    "event_type": event_type,
                    "notes": notes,
                },
                qualifying_life_event_record_params.QualifyingLifeEventRecordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualifyingLifeEventResponse,
        )


class QualifyingLifeEventsResourceWithRawResponse:
    def __init__(self, qualifying_life_events: QualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = to_raw_response_wrapper(
            qualifying_life_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            qualifying_life_events.list,
        )
        self.record = to_raw_response_wrapper(
            qualifying_life_events.record,
        )


class AsyncQualifyingLifeEventsResourceWithRawResponse:
    def __init__(self, qualifying_life_events: AsyncQualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = async_to_raw_response_wrapper(
            qualifying_life_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            qualifying_life_events.list,
        )
        self.record = async_to_raw_response_wrapper(
            qualifying_life_events.record,
        )


class QualifyingLifeEventsResourceWithStreamingResponse:
    def __init__(self, qualifying_life_events: QualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = to_streamed_response_wrapper(
            qualifying_life_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            qualifying_life_events.list,
        )
        self.record = to_streamed_response_wrapper(
            qualifying_life_events.record,
        )


class AsyncQualifyingLifeEventsResourceWithStreamingResponse:
    def __init__(self, qualifying_life_events: AsyncQualifyingLifeEventsResource) -> None:
        self._qualifying_life_events = qualifying_life_events

        self.retrieve = async_to_streamed_response_wrapper(
            qualifying_life_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            qualifying_life_events.list,
        )
        self.record = async_to_streamed_response_wrapper(
            qualifying_life_events.record,
        )
