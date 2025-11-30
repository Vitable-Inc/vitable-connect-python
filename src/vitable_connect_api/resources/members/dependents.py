# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ...types import Sex
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
from ...types.sex import Sex
from ..._base_client import make_request_options
from ...types.members import Relationship, dependent_list_params, dependent_create_params
from ...types.dependent import Dependent
from ...types.members.relationship import Relationship
from ...types.members.dependent_list_response import DependentListResponse

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
        member_id: str,
        *,
        date_of_birth: Union[str, date],
        first_name: str,
        last_name: str,
        relationship: Relationship,
        sex: Sex,
        gender: Optional[str] | Omit = omit,
        ssn: Optional[str] | Omit = omit,
        suffix: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """Creates a new dependent record for a member.

        Required: first name, last name,
        date of birth, sex, and relationship type. SSN is optional but recommended for
        coverage verification.

        Args:
          date_of_birth: Date of birth (YYYY-MM-DD)

          first_name: Dependent's legal first name

          last_name: Dependent's legal last name

          relationship: - `Spouse` - Spouse
              - `Child` - Child

          sex: - `Male` - Male
              - `Female` - Female
              - `Other` - Other
              - `Unknown` - Unknown

          gender: Gender identity

          ssn: Social Security Number (optional, XXX-XX-XXXX or XXXXXXXXX)

          suffix: Name suffix (Jr., Sr., III)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._post(
            f"/v1/members/{member_id}/dependents",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "relationship": relationship,
                    "sex": sex,
                    "gender": gender,
                    "ssn": ssn,
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
        member_id: str,
        *,
        active_in: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        relationship: Relationship | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DependentListResponse:
        """Retrieves a paginated list of dependents for a specific member.

        Dependents
        include spouses, children, and domestic partners who may be eligible for benefit
        coverage.

        Args:
          active_in: Filter by active status

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          relationship: Filter by relationship type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            f"/v1/members/{member_id}/dependents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_in": active_in,
                        "limit": limit,
                        "page": page,
                        "relationship": relationship,
                    },
                    dependent_list_params.DependentListParams,
                ),
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
        member_id: str,
        *,
        date_of_birth: Union[str, date],
        first_name: str,
        last_name: str,
        relationship: Relationship,
        sex: Sex,
        gender: Optional[str] | Omit = omit,
        ssn: Optional[str] | Omit = omit,
        suffix: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dependent:
        """Creates a new dependent record for a member.

        Required: first name, last name,
        date of birth, sex, and relationship type. SSN is optional but recommended for
        coverage verification.

        Args:
          date_of_birth: Date of birth (YYYY-MM-DD)

          first_name: Dependent's legal first name

          last_name: Dependent's legal last name

          relationship: - `Spouse` - Spouse
              - `Child` - Child

          sex: - `Male` - Male
              - `Female` - Female
              - `Other` - Other
              - `Unknown` - Unknown

          gender: Gender identity

          ssn: Social Security Number (optional, XXX-XX-XXXX or XXXXXXXXX)

          suffix: Name suffix (Jr., Sr., III)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._post(
            f"/v1/members/{member_id}/dependents",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "relationship": relationship,
                    "sex": sex,
                    "gender": gender,
                    "ssn": ssn,
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
        member_id: str,
        *,
        active_in: bool | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        relationship: Relationship | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DependentListResponse:
        """Retrieves a paginated list of dependents for a specific member.

        Dependents
        include spouses, children, and domestic partners who may be eligible for benefit
        coverage.

        Args:
          active_in: Filter by active status

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          relationship: Filter by relationship type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            f"/v1/members/{member_id}/dependents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_in": active_in,
                        "limit": limit,
                        "page": page,
                        "relationship": relationship,
                    },
                    dependent_list_params.DependentListParams,
                ),
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
