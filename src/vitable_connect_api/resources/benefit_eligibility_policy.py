# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.benefit_eligibility_policy import BenefitEligibilityPolicy

__all__ = ["BenefitEligibilityPolicyResource", "AsyncBenefitEligibilityPolicyResource"]


class BenefitEligibilityPolicyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BenefitEligibilityPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return BenefitEligibilityPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenefitEligibilityPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return BenefitEligibilityPolicyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenefitEligibilityPolicy:
        """
        Retrieves detailed information for a specific benefit eligibility policy by ID.
        Returns the complete policy configuration including all eligibility rules,
        effective dates, associated employer information, and any waiting period
        requirements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/v1/benefit-eligibility-policy/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenefitEligibilityPolicy,
        )


class AsyncBenefitEligibilityPolicyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBenefitEligibilityPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenefitEligibilityPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenefitEligibilityPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return AsyncBenefitEligibilityPolicyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        policy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenefitEligibilityPolicy:
        """
        Retrieves detailed information for a specific benefit eligibility policy by ID.
        Returns the complete policy configuration including all eligibility rules,
        effective dates, associated employer information, and any waiting period
        requirements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/v1/benefit-eligibility-policy/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenefitEligibilityPolicy,
        )


class BenefitEligibilityPolicyResourceWithRawResponse:
    def __init__(self, benefit_eligibility_policy: BenefitEligibilityPolicyResource) -> None:
        self._benefit_eligibility_policy = benefit_eligibility_policy

        self.retrieve = to_raw_response_wrapper(
            benefit_eligibility_policy.retrieve,
        )


class AsyncBenefitEligibilityPolicyResourceWithRawResponse:
    def __init__(self, benefit_eligibility_policy: AsyncBenefitEligibilityPolicyResource) -> None:
        self._benefit_eligibility_policy = benefit_eligibility_policy

        self.retrieve = async_to_raw_response_wrapper(
            benefit_eligibility_policy.retrieve,
        )


class BenefitEligibilityPolicyResourceWithStreamingResponse:
    def __init__(self, benefit_eligibility_policy: BenefitEligibilityPolicyResource) -> None:
        self._benefit_eligibility_policy = benefit_eligibility_policy

        self.retrieve = to_streamed_response_wrapper(
            benefit_eligibility_policy.retrieve,
        )


class AsyncBenefitEligibilityPolicyResourceWithStreamingResponse:
    def __init__(self, benefit_eligibility_policy: AsyncBenefitEligibilityPolicyResource) -> None:
        self._benefit_eligibility_policy = benefit_eligibility_policy

        self.retrieve = async_to_streamed_response_wrapper(
            benefit_eligibility_policy.retrieve,
        )
