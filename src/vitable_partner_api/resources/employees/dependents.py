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
from ...types.dependent import Dependent
from ...types.employees import dependent_create_params
from ...types.employees.dependent_list_response import DependentListResponse

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

    def create(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date],
        first_name: str,
        last_name: str,
        relationship: Literal["SPOUSE", "CHILD"],
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
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
        Creates a new Dependent for a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/employees/{id}/dependents",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "relationship": relationship,
                    "gender": gender,
                    "sex": sex,
                    "suffix": suffix,
                },
                dependent_create_params.DependentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dependent,
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
    ) -> DependentListResponse:
        """
        Lists all existing Dependents for a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employees/{id}/dependents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DependentListResponse,
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

    async def create(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date],
        first_name: str,
        last_name: str,
        relationship: Literal["SPOUSE", "CHILD"],
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
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
        Creates a new Dependent for a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/employees/{id}/dependents",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "relationship": relationship,
                    "gender": gender,
                    "sex": sex,
                    "suffix": suffix,
                },
                dependent_create_params.DependentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dependent,
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
    ) -> DependentListResponse:
        """
        Lists all existing Dependents for a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employees/{id}/dependents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DependentListResponse,
        )


class DependentsResourceWithRawResponse:
    def __init__(self, dependents: DependentsResource) -> None:
        self._dependents = dependents

        self.create = to_raw_response_wrapper(
            dependents.create,
        )
        self.list = to_raw_response_wrapper(
            dependents.list,
        )


class AsyncDependentsResourceWithRawResponse:
    def __init__(self, dependents: AsyncDependentsResource) -> None:
        self._dependents = dependents

        self.create = async_to_raw_response_wrapper(
            dependents.create,
        )
        self.list = async_to_raw_response_wrapper(
            dependents.list,
        )


class DependentsResourceWithStreamingResponse:
    def __init__(self, dependents: DependentsResource) -> None:
        self._dependents = dependents

        self.create = to_streamed_response_wrapper(
            dependents.create,
        )
        self.list = to_streamed_response_wrapper(
            dependents.list,
        )


class AsyncDependentsResourceWithStreamingResponse:
    def __init__(self, dependents: AsyncDependentsResource) -> None:
        self._dependents = dependents

        self.create = async_to_streamed_response_wrapper(
            dependents.create,
        )
        self.list = async_to_streamed_response_wrapper(
            dependents.list,
        )
