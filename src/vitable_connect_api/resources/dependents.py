# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import dependent_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.members import Relationship
from ..types.dependent import Dependent
from ..types.members.relationship import Relationship

__all__ = ["DependentsResource", "AsyncDependentsResource"]


class DependentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DependentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return DependentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DependentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return DependentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dependent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """Retrieves detailed information for a specific dependent by ID.

        Returns dependent
        profile including name, date of birth, and relationship type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dependent_id:
            raise ValueError(f"Expected a non-empty value for `dependent_id` but received {dependent_id!r}")
        return self._get(
            f"/v1/dependents/{dependent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dependent,
        )

    def update(
        self,
        dependent_id: str,
        *,
        active: Optional[bool] | Omit = omit,
        gender: Optional[str] | Omit = omit,
        relationship: Optional[Relationship] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """Updates an existing dependent's mutable information.

        Allows modification of
        relationship type and active status. Name, DOB, and sex cannot be modified after
        creation.

        Args:
          active: Whether the dependent is active

          gender: Gender identity

          relationship: - `Spouse` - Spouse
              - `Child` - Child

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dependent_id:
            raise ValueError(f"Expected a non-empty value for `dependent_id` but received {dependent_id!r}")
        return self._put(
            f"/v1/dependents/{dependent_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "gender": gender,
                    "relationship": relationship,
                },
                dependent_update_params.DependentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dependent,
        )


class AsyncDependentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDependentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDependentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDependentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return AsyncDependentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dependent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """Retrieves detailed information for a specific dependent by ID.

        Returns dependent
        profile including name, date of birth, and relationship type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dependent_id:
            raise ValueError(f"Expected a non-empty value for `dependent_id` but received {dependent_id!r}")
        return await self._get(
            f"/v1/dependents/{dependent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dependent,
        )

    async def update(
        self,
        dependent_id: str,
        *,
        active: Optional[bool] | Omit = omit,
        gender: Optional[str] | Omit = omit,
        relationship: Optional[Relationship] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """Updates an existing dependent's mutable information.

        Allows modification of
        relationship type and active status. Name, DOB, and sex cannot be modified after
        creation.

        Args:
          active: Whether the dependent is active

          gender: Gender identity

          relationship: - `Spouse` - Spouse
              - `Child` - Child

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dependent_id:
            raise ValueError(f"Expected a non-empty value for `dependent_id` but received {dependent_id!r}")
        return await self._put(
            f"/v1/dependents/{dependent_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "gender": gender,
                    "relationship": relationship,
                },
                dependent_update_params.DependentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dependent,
        )


class DependentsResourceWithRawResponse:
    def __init__(self, dependents: DependentsResource) -> None:
        self._dependents = dependents

        self.retrieve = to_raw_response_wrapper(
            dependents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dependents.update,
        )


class AsyncDependentsResourceWithRawResponse:
    def __init__(self, dependents: AsyncDependentsResource) -> None:
        self._dependents = dependents

        self.retrieve = async_to_raw_response_wrapper(
            dependents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dependents.update,
        )


class DependentsResourceWithStreamingResponse:
    def __init__(self, dependents: DependentsResource) -> None:
        self._dependents = dependents

        self.retrieve = to_streamed_response_wrapper(
            dependents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dependents.update,
        )


class AsyncDependentsResourceWithStreamingResponse:
    def __init__(self, dependents: AsyncDependentsResource) -> None:
        self._dependents = dependents

        self.retrieve = async_to_streamed_response_wrapper(
            dependents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dependents.update,
        )
