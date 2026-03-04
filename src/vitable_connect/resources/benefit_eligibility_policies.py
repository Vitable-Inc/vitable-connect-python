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

__all__ = ["BenefitEligibilityPoliciesResource", "AsyncBenefitEligibilityPoliciesResource"]


class BenefitEligibilityPoliciesResource(SyncAPIResource):
    """Define rules that determine which employees qualify for benefits"""

    @cached_property
    def with_raw_response(self) -> BenefitEligibilityPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return BenefitEligibilityPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenefitEligibilityPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return BenefitEligibilityPoliciesResourceWithStreamingResponse(self)

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
          policy_id: Unique benefit eligibility policy identifier (epol\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/v1/benefit-eligibility-policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenefitEligibilityPolicy,
        )


class AsyncBenefitEligibilityPoliciesResource(AsyncAPIResource):
    """Define rules that determine which employees qualify for benefits"""

    @cached_property
    def with_raw_response(self) -> AsyncBenefitEligibilityPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenefitEligibilityPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenefitEligibilityPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncBenefitEligibilityPoliciesResourceWithStreamingResponse(self)

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
          policy_id: Unique benefit eligibility policy identifier (epol\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/v1/benefit-eligibility-policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BenefitEligibilityPolicy,
        )


class BenefitEligibilityPoliciesResourceWithRawResponse:
    def __init__(self, benefit_eligibility_policies: BenefitEligibilityPoliciesResource) -> None:
        self._benefit_eligibility_policies = benefit_eligibility_policies

        self.retrieve = to_raw_response_wrapper(
            benefit_eligibility_policies.retrieve,
        )


class AsyncBenefitEligibilityPoliciesResourceWithRawResponse:
    def __init__(self, benefit_eligibility_policies: AsyncBenefitEligibilityPoliciesResource) -> None:
        self._benefit_eligibility_policies = benefit_eligibility_policies

        self.retrieve = async_to_raw_response_wrapper(
            benefit_eligibility_policies.retrieve,
        )


class BenefitEligibilityPoliciesResourceWithStreamingResponse:
    def __init__(self, benefit_eligibility_policies: BenefitEligibilityPoliciesResource) -> None:
        self._benefit_eligibility_policies = benefit_eligibility_policies

        self.retrieve = to_streamed_response_wrapper(
            benefit_eligibility_policies.retrieve,
        )


class AsyncBenefitEligibilityPoliciesResourceWithStreamingResponse:
    def __init__(self, benefit_eligibility_policies: AsyncBenefitEligibilityPoliciesResource) -> None:
        self._benefit_eligibility_policies = benefit_eligibility_policies

        self.retrieve = async_to_streamed_response_wrapper(
            benefit_eligibility_policies.retrieve,
        )
