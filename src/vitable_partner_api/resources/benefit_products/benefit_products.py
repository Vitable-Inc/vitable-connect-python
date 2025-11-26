# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...types import benefit_product_list_params, benefit_product_generate_quote_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .plan_years import (
    PlanYearsResource,
    AsyncPlanYearsResource,
    PlanYearsResourceWithRawResponse,
    AsyncPlanYearsResourceWithRawResponse,
    PlanYearsResourceWithStreamingResponse,
    AsyncPlanYearsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.quote import Quote
from ..._base_client import make_request_options
from ...types.benefit_product_list_response import BenefitProductListResponse

__all__ = ["BenefitProductsResource", "AsyncBenefitProductsResource"]


class BenefitProductsResource(SyncAPIResource):
    @cached_property
    def plan_years(self) -> PlanYearsResource:
        return PlanYearsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BenefitProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return BenefitProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenefitProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return BenefitProductsResourceWithStreamingResponse(self)

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
    ) -> BenefitProductListResponse:
        """
        Lists all Benefit Products that an Organization has access to that they can
        offer to their Employers.

        Args:
          limit: Number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/benefit-products",
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
                    benefit_product_list_params.BenefitProductListParams,
                ),
            ),
            cast_to=BenefitProductListResponse,
        )

    def generate_quote(
        self,
        id: str,
        *,
        employer_id: str,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Generates a quote with pricing for an Employer with metadata for a specific
        Product. Employer/metadata would be in request body.

        Args:
          metadata: Additional metadata for quote generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/benefit-products/{id}/quote",
            body=maybe_transform(
                {
                    "employer_id": employer_id,
                    "metadata": metadata,
                },
                benefit_product_generate_quote_params.BenefitProductGenerateQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )


class AsyncBenefitProductsResource(AsyncAPIResource):
    @cached_property
    def plan_years(self) -> AsyncPlanYearsResource:
        return AsyncPlanYearsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenefitProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenefitProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenefitProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncBenefitProductsResourceWithStreamingResponse(self)

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
    ) -> BenefitProductListResponse:
        """
        Lists all Benefit Products that an Organization has access to that they can
        offer to their Employers.

        Args:
          limit: Number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/benefit-products",
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
                    benefit_product_list_params.BenefitProductListParams,
                ),
            ),
            cast_to=BenefitProductListResponse,
        )

    async def generate_quote(
        self,
        id: str,
        *,
        employer_id: str,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Quote:
        """
        Generates a quote with pricing for an Employer with metadata for a specific
        Product. Employer/metadata would be in request body.

        Args:
          metadata: Additional metadata for quote generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/benefit-products/{id}/quote",
            body=await async_maybe_transform(
                {
                    "employer_id": employer_id,
                    "metadata": metadata,
                },
                benefit_product_generate_quote_params.BenefitProductGenerateQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Quote,
        )


class BenefitProductsResourceWithRawResponse:
    def __init__(self, benefit_products: BenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = to_raw_response_wrapper(
            benefit_products.list,
        )
        self.generate_quote = to_raw_response_wrapper(
            benefit_products.generate_quote,
        )

    @cached_property
    def plan_years(self) -> PlanYearsResourceWithRawResponse:
        return PlanYearsResourceWithRawResponse(self._benefit_products.plan_years)


class AsyncBenefitProductsResourceWithRawResponse:
    def __init__(self, benefit_products: AsyncBenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = async_to_raw_response_wrapper(
            benefit_products.list,
        )
        self.generate_quote = async_to_raw_response_wrapper(
            benefit_products.generate_quote,
        )

    @cached_property
    def plan_years(self) -> AsyncPlanYearsResourceWithRawResponse:
        return AsyncPlanYearsResourceWithRawResponse(self._benefit_products.plan_years)


class BenefitProductsResourceWithStreamingResponse:
    def __init__(self, benefit_products: BenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = to_streamed_response_wrapper(
            benefit_products.list,
        )
        self.generate_quote = to_streamed_response_wrapper(
            benefit_products.generate_quote,
        )

    @cached_property
    def plan_years(self) -> PlanYearsResourceWithStreamingResponse:
        return PlanYearsResourceWithStreamingResponse(self._benefit_products.plan_years)


class AsyncBenefitProductsResourceWithStreamingResponse:
    def __init__(self, benefit_products: AsyncBenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = async_to_streamed_response_wrapper(
            benefit_products.list,
        )
        self.generate_quote = async_to_streamed_response_wrapper(
            benefit_products.generate_quote,
        )

    @cached_property
    def plan_years(self) -> AsyncPlanYearsResourceWithStreamingResponse:
        return AsyncPlanYearsResourceWithStreamingResponse(self._benefit_products.plan_years)
