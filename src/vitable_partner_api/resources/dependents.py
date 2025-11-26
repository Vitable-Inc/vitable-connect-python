# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

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
from ..types.dependent import Dependent

__all__ = ["DependentsResource", "AsyncDependentsResource"]


class DependentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DependentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return DependentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DependentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return DependentsResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date] | Omit = omit,
        first_name: str | Omit = omit,
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
        last_name: str | Omit = omit,
        relationship: Literal["SPOUSE", "CHILD"] | Omit = omit,
        sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"] | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """
        Updates an existing Dependent for a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/dependents/{id}",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "gender": gender,
                    "last_name": last_name,
                    "relationship": relationship,
                    "sex": sex,
                    "suffix": suffix,
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

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDependentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDependentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncDependentsResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date] | Omit = omit,
        first_name: str | Omit = omit,
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
        last_name: str | Omit = omit,
        relationship: Literal["SPOUSE", "CHILD"] | Omit = omit,
        sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"] | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """
        Updates an existing Dependent for a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/dependents/{id}",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "gender": gender,
                    "last_name": last_name,
                    "relationship": relationship,
                    "sex": sex,
                    "suffix": suffix,
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

        self.update = to_raw_response_wrapper(
            dependents.update,
        )


class AsyncDependentsResourceWithRawResponse:
    def __init__(self, dependents: AsyncDependentsResource) -> None:
        self._dependents = dependents

        self.update = async_to_raw_response_wrapper(
            dependents.update,
        )


class DependentsResourceWithStreamingResponse:
    def __init__(self, dependents: DependentsResource) -> None:
        self._dependents = dependents

        self.update = to_streamed_response_wrapper(
            dependents.update,
        )


class AsyncDependentsResourceWithStreamingResponse:
    def __init__(self, dependents: AsyncDependentsResource) -> None:
        self._dependents = dependents

        self.update = async_to_streamed_response_wrapper(
            dependents.update,
        )
