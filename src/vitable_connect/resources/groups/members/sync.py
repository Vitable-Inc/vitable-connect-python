# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.groups.members import sync_submit_params
from ....types.groups.members.sync_submit_response import SyncSubmitResponse
from ....types.groups.members.sync_retrieve_response import SyncRetrieveResponse

__all__ = ["SyncResource", "AsyncSyncResource"]


class SyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return SyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return SyncResourceWithStreamingResponse(self)

    def retrieve(
        self,
        request_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncRetrieveResponse:
        """
        Retrieves a previously-submitted group member sync request by its `grpmsr_` ID.
        Returns the acceptance timestamp, completion timestamp (if processing has
        finished), and the per-member `results` once available. While processing is in
        flight, `completed_at` and `results` are `null`.

        Args:
          group_id: Unique group identifier (grp\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template("/v1/groups/{group_id}/members/sync/{request_id}", group_id=group_id, request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncRetrieveResponse,
        )

    def submit(
        self,
        group_id: str,
        *,
        members: Iterable[sync_submit_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSubmitResponse:
        """Submits a member sync payload for the specified group.

        Members in the payload
        will be queued for processing asynchronously. Returns HTTP 202 with the batch ID
        and acceptance timestamp.

        Args:
          group_id: Unique group identifier (grp\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            path_template("/v1/groups/{group_id}/members/sync", group_id=group_id),
            body=maybe_transform({"members": members}, sync_submit_params.SyncSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncSubmitResponse,
        )


class AsyncSyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncSyncResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        request_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncRetrieveResponse:
        """
        Retrieves a previously-submitted group member sync request by its `grpmsr_` ID.
        Returns the acceptance timestamp, completion timestamp (if processing has
        finished), and the per-member `results` once available. While processing is in
        flight, `completed_at` and `results` are `null`.

        Args:
          group_id: Unique group identifier (grp\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template("/v1/groups/{group_id}/members/sync/{request_id}", group_id=group_id, request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncRetrieveResponse,
        )

    async def submit(
        self,
        group_id: str,
        *,
        members: Iterable[sync_submit_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSubmitResponse:
        """Submits a member sync payload for the specified group.

        Members in the payload
        will be queued for processing asynchronously. Returns HTTP 202 with the batch ID
        and acceptance timestamp.

        Args:
          group_id: Unique group identifier (grp\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            path_template("/v1/groups/{group_id}/members/sync", group_id=group_id),
            body=await async_maybe_transform({"members": members}, sync_submit_params.SyncSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncSubmitResponse,
        )


class SyncResourceWithRawResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.retrieve = to_raw_response_wrapper(
            sync.retrieve,
        )
        self.submit = to_raw_response_wrapper(
            sync.submit,
        )


class AsyncSyncResourceWithRawResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.retrieve = async_to_raw_response_wrapper(
            sync.retrieve,
        )
        self.submit = async_to_raw_response_wrapper(
            sync.submit,
        )


class SyncResourceWithStreamingResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.retrieve = to_streamed_response_wrapper(
            sync.retrieve,
        )
        self.submit = to_streamed_response_wrapper(
            sync.submit,
        )


class AsyncSyncResourceWithStreamingResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.retrieve = async_to_streamed_response_wrapper(
            sync.retrieve,
        )
        self.submit = async_to_streamed_response_wrapper(
            sync.submit,
        )
