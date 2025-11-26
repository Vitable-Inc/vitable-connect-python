# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    employer_list_params,
    employer_create_params,
    employer_update_params,
    employer_create_eligibility_policy_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .employees import (
    EmployeesResource,
    AsyncEmployeesResource,
    EmployeesResourceWithRawResponse,
    AsyncEmployeesResourceWithRawResponse,
    EmployeesResourceWithStreamingResponse,
    AsyncEmployeesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.employer import Employer
from ...types.eligibility_policy import EligibilityPolicy
from ...types.employer_list_response import EmployerListResponse

__all__ = ["EmployersResource", "AsyncEmployersResource"]


class EmployersResource(SyncAPIResource):
    @cached_property
    def employees(self) -> EmployeesResource:
        return EmployeesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmployersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return EmployersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return EmployersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        legal_name: str,
        name: str,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employer:
        """
        Creates a new Employer for an Organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/employers",
            body=maybe_transform(
                {
                    "legal_name": legal_name,
                    "name": name,
                    "active": active,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employer,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employer:
        """
        Gets a specific Employer an Organization has access to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employer,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        legal_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employer:
        """
        Updates a specific Employer an Organization has access to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/employers/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employer,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListResponse:
        """
        Lists all Employers an Organization has access to.

        Args:
          limit: Number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/employers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    employer_list_params.EmployerListParams,
                ),
            ),
            cast_to=EmployerListResponse,
        )

    def create_eligibility_policy(
        self,
        id: str,
        *,
        classification: Literal["FULL_TIME", "PART_TIME", "ALL"],
        waiting_period: Literal["FIRST_OF_FOLLOWING_MONTH", "THIRTY_DAYS", "SIXTY_DAYS", "NONE"],
        policy_to_replace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EligibilityPolicy:
        """
        Creates a new Benefit Eligibility Policy for a specific Employer an Organization
        has access to.

        Args:
          policy_to_replace_id: ID of the policy to replace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/employers/{id}/benefit-eligibility-policy",
            body=maybe_transform(
                {
                    "classification": classification,
                    "waiting_period": waiting_period,
                },
                employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"policy_to_replace_id": policy_to_replace_id},
                    employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
                ),
            ),
            cast_to=EligibilityPolicy,
        )


class AsyncEmployersResource(AsyncAPIResource):
    @cached_property
    def employees(self) -> AsyncEmployeesResource:
        return AsyncEmployeesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmployersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncEmployersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        legal_name: str,
        name: str,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employer:
        """
        Creates a new Employer for an Organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/employers",
            body=await async_maybe_transform(
                {
                    "legal_name": legal_name,
                    "name": name,
                    "active": active,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employer,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employer:
        """
        Gets a specific Employer an Organization has access to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employer,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        legal_name: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employer:
        """
        Updates a specific Employer an Organization has access to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/employers/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employer,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListResponse:
        """
        Lists all Employers an Organization has access to.

        Args:
          limit: Number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/employers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    employer_list_params.EmployerListParams,
                ),
            ),
            cast_to=EmployerListResponse,
        )

    async def create_eligibility_policy(
        self,
        id: str,
        *,
        classification: Literal["FULL_TIME", "PART_TIME", "ALL"],
        waiting_period: Literal["FIRST_OF_FOLLOWING_MONTH", "THIRTY_DAYS", "SIXTY_DAYS", "NONE"],
        policy_to_replace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EligibilityPolicy:
        """
        Creates a new Benefit Eligibility Policy for a specific Employer an Organization
        has access to.

        Args:
          policy_to_replace_id: ID of the policy to replace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/employers/{id}/benefit-eligibility-policy",
            body=await async_maybe_transform(
                {
                    "classification": classification,
                    "waiting_period": waiting_period,
                },
                employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"policy_to_replace_id": policy_to_replace_id},
                    employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
                ),
            ),
            cast_to=EligibilityPolicy,
        )


class EmployersResourceWithRawResponse:
    def __init__(self, employers: EmployersResource) -> None:
        self._employers = employers

        self.create = to_raw_response_wrapper(
            employers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employers.update,
        )
        self.list = to_raw_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = to_raw_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> EmployeesResourceWithRawResponse:
        return EmployeesResourceWithRawResponse(self._employers.employees)


class AsyncEmployersResourceWithRawResponse:
    def __init__(self, employers: AsyncEmployersResource) -> None:
        self._employers = employers

        self.create = async_to_raw_response_wrapper(
            employers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employers.update,
        )
        self.list = async_to_raw_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = async_to_raw_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> AsyncEmployeesResourceWithRawResponse:
        return AsyncEmployeesResourceWithRawResponse(self._employers.employees)


class EmployersResourceWithStreamingResponse:
    def __init__(self, employers: EmployersResource) -> None:
        self._employers = employers

        self.create = to_streamed_response_wrapper(
            employers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employers.update,
        )
        self.list = to_streamed_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = to_streamed_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> EmployeesResourceWithStreamingResponse:
        return EmployeesResourceWithStreamingResponse(self._employers.employees)


class AsyncEmployersResourceWithStreamingResponse:
    def __init__(self, employers: AsyncEmployersResource) -> None:
        self._employers = employers

        self.create = async_to_streamed_response_wrapper(
            employers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = async_to_streamed_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> AsyncEmployeesResourceWithStreamingResponse:
        return AsyncEmployeesResourceWithStreamingResponse(self._employers.employees)
