# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .dependents import (
    DependentsResource,
    AsyncDependentsResource,
    DependentsResourceWithRawResponse,
    AsyncDependentsResourceWithRawResponse,
    DependentsResourceWithStreamingResponse,
    AsyncDependentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .qualifying_life_events import (
    QualifyingLifeEventsResource,
    AsyncQualifyingLifeEventsResource,
    QualifyingLifeEventsResourceWithRawResponse,
    AsyncQualifyingLifeEventsResourceWithRawResponse,
    QualifyingLifeEventsResourceWithStreamingResponse,
    AsyncQualifyingLifeEventsResourceWithStreamingResponse,
)

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def dependents(self) -> DependentsResource:
        return DependentsResource(self._client)

    @cached_property
    def qualifying_life_events(self) -> QualifyingLifeEventsResource:
        return QualifyingLifeEventsResource(self._client)

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
    def dependents(self) -> AsyncDependentsResource:
        return AsyncDependentsResource(self._client)

    @cached_property
    def qualifying_life_events(self) -> AsyncQualifyingLifeEventsResource:
        return AsyncQualifyingLifeEventsResource(self._client)

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
    def dependents(self) -> DependentsResourceWithRawResponse:
        return DependentsResourceWithRawResponse(self._members.dependents)

    @cached_property
    def qualifying_life_events(self) -> QualifyingLifeEventsResourceWithRawResponse:
        return QualifyingLifeEventsResourceWithRawResponse(self._members.qualifying_life_events)


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

    @cached_property
    def dependents(self) -> AsyncDependentsResourceWithRawResponse:
        return AsyncDependentsResourceWithRawResponse(self._members.dependents)

    @cached_property
    def qualifying_life_events(self) -> AsyncQualifyingLifeEventsResourceWithRawResponse:
        return AsyncQualifyingLifeEventsResourceWithRawResponse(self._members.qualifying_life_events)


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

    @cached_property
    def dependents(self) -> DependentsResourceWithStreamingResponse:
        return DependentsResourceWithStreamingResponse(self._members.dependents)

    @cached_property
    def qualifying_life_events(self) -> QualifyingLifeEventsResourceWithStreamingResponse:
        return QualifyingLifeEventsResourceWithStreamingResponse(self._members.qualifying_life_events)


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

    @cached_property
    def dependents(self) -> AsyncDependentsResourceWithStreamingResponse:
        return AsyncDependentsResourceWithStreamingResponse(self._members.dependents)

    @cached_property
    def qualifying_life_events(self) -> AsyncQualifyingLifeEventsResourceWithStreamingResponse:
        return AsyncQualifyingLifeEventsResourceWithStreamingResponse(self._members.qualifying_life_events)
