# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import Category, ProductCode, benefit_product_list_params
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
from ..._base_client import make_request_options
from ...types.category import Category
from ...types.product_code import ProductCode
from ...types.benefit_product_list_response import BenefitProductListResponse

__all__ = ["BenefitProductsResource", "AsyncBenefitProductsResource"]


class BenefitProductsResource(SyncAPIResource):
    """Browse available benefit products that can be offered to employers"""

    @cached_property
    def plan_years(self) -> PlanYearsResource:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        return PlanYearsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BenefitProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return BenefitProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenefitProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return BenefitProductsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        active_in: bool | Omit = omit,
        category: Category | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        product_code: ProductCode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenefitProductListResponse:
        """
        Retrieves a paginated list of all benefit products that the authenticated
        organization has access to and can offer to their employers. Use query
        parameters to filter by category, product code, or active status.

        Args:
          active_in: Filter by active status

          category: Filter by product category

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          product_code: Filter by product code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/benefit-products",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_in": active_in,
                        "category": category,
                        "limit": limit,
                        "page": page,
                        "product_code": product_code,
                    },
                    benefit_product_list_params.BenefitProductListParams,
                ),
            ),
            cast_to=BenefitProductListResponse,
        )


class AsyncBenefitProductsResource(AsyncAPIResource):
    """Browse available benefit products that can be offered to employers"""

    @cached_property
    def plan_years(self) -> AsyncPlanYearsResource:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        return AsyncPlanYearsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenefitProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBenefitProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenefitProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncBenefitProductsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        active_in: bool | Omit = omit,
        category: Category | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        product_code: ProductCode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenefitProductListResponse:
        """
        Retrieves a paginated list of all benefit products that the authenticated
        organization has access to and can offer to their employers. Use query
        parameters to filter by category, product code, or active status.

        Args:
          active_in: Filter by active status

          category: Filter by product category

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          product_code: Filter by product code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/benefit-products",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_in": active_in,
                        "category": category,
                        "limit": limit,
                        "page": page,
                        "product_code": product_code,
                    },
                    benefit_product_list_params.BenefitProductListParams,
                ),
            ),
            cast_to=BenefitProductListResponse,
        )


class BenefitProductsResourceWithRawResponse:
    def __init__(self, benefit_products: BenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = to_raw_response_wrapper(
            benefit_products.list,
        )

    @cached_property
    def plan_years(self) -> PlanYearsResourceWithRawResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        return PlanYearsResourceWithRawResponse(self._benefit_products.plan_years)


class AsyncBenefitProductsResourceWithRawResponse:
    def __init__(self, benefit_products: AsyncBenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = async_to_raw_response_wrapper(
            benefit_products.list,
        )

    @cached_property
    def plan_years(self) -> AsyncPlanYearsResourceWithRawResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        return AsyncPlanYearsResourceWithRawResponse(self._benefit_products.plan_years)


class BenefitProductsResourceWithStreamingResponse:
    def __init__(self, benefit_products: BenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = to_streamed_response_wrapper(
            benefit_products.list,
        )

    @cached_property
    def plan_years(self) -> PlanYearsResourceWithStreamingResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        return PlanYearsResourceWithStreamingResponse(self._benefit_products.plan_years)


class AsyncBenefitProductsResourceWithStreamingResponse:
    def __init__(self, benefit_products: AsyncBenefitProductsResource) -> None:
        self._benefit_products = benefit_products

        self.list = async_to_streamed_response_wrapper(
            benefit_products.list,
        )

    @cached_property
    def plan_years(self) -> AsyncPlanYearsResourceWithStreamingResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        return AsyncPlanYearsResourceWithStreamingResponse(self._benefit_products.plan_years)
