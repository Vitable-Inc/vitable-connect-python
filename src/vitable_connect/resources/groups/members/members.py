# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sync import (
    SyncResource,
    AsyncSyncResource,
    SyncResourceWithRawResponse,
    AsyncSyncResourceWithRawResponse,
    SyncResourceWithStreamingResponse,
    AsyncSyncResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def sync(self) -> SyncResource:
        return SyncResource(self._client)

    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def sync(self) -> AsyncSyncResource:
        return AsyncSyncResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

    @cached_property
    def sync(self) -> SyncResourceWithRawResponse:
        return SyncResourceWithRawResponse(self._members.sync)


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

    @cached_property
    def sync(self) -> AsyncSyncResourceWithRawResponse:
        return AsyncSyncResourceWithRawResponse(self._members.sync)


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

    @cached_property
    def sync(self) -> SyncResourceWithStreamingResponse:
        return SyncResourceWithStreamingResponse(self._members.sync)


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

    @cached_property
    def sync(self) -> AsyncSyncResourceWithStreamingResponse:
        return AsyncSyncResourceWithStreamingResponse(self._members.sync)
