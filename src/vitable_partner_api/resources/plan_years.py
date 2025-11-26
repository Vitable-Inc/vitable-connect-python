# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..types import plan_year_update_params
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
from ..types.plan_year import PlanYear

__all__ = ["PlanYearsResource", "AsyncPlanYearsResource"]


class PlanYearsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlanYearsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return PlanYearsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanYearsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return PlanYearsResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        contribution_classes: Iterable[plan_year_update_params.ContributionClass] | Omit = omit,
        coverage_end_date: Union[str, date] | Omit = omit,
        coverage_start_date: Union[str, date] | Omit = omit,
        open_enrollment_end_date: Union[str, date] | Omit = omit,
        open_enrollment_start_date: Union[str, date] | Omit = omit,
        plan_costs: Iterable[plan_year_update_params.PlanCost] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYear:
        """
        Updates a specific Plan Year with configuration details for a Benefit Product
        for an Employer. Can only be edited up until open enrollment starts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/plan-years/{id}",
            body=maybe_transform(
                {
                    "contribution_classes": contribution_classes,
                    "coverage_end_date": coverage_end_date,
                    "coverage_start_date": coverage_start_date,
                    "open_enrollment_end_date": open_enrollment_end_date,
                    "open_enrollment_start_date": open_enrollment_start_date,
                    "plan_costs": plan_costs,
                },
                plan_year_update_params.PlanYearUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYear,
        )


class AsyncPlanYearsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlanYearsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlanYearsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanYearsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncPlanYearsResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        contribution_classes: Iterable[plan_year_update_params.ContributionClass] | Omit = omit,
        coverage_end_date: Union[str, date] | Omit = omit,
        coverage_start_date: Union[str, date] | Omit = omit,
        open_enrollment_end_date: Union[str, date] | Omit = omit,
        open_enrollment_start_date: Union[str, date] | Omit = omit,
        plan_costs: Iterable[plan_year_update_params.PlanCost] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYear:
        """
        Updates a specific Plan Year with configuration details for a Benefit Product
        for an Employer. Can only be edited up until open enrollment starts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/plan-years/{id}",
            body=await async_maybe_transform(
                {
                    "contribution_classes": contribution_classes,
                    "coverage_end_date": coverage_end_date,
                    "coverage_start_date": coverage_start_date,
                    "open_enrollment_end_date": open_enrollment_end_date,
                    "open_enrollment_start_date": open_enrollment_start_date,
                    "plan_costs": plan_costs,
                },
                plan_year_update_params.PlanYearUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYear,
        )


class PlanYearsResourceWithRawResponse:
    def __init__(self, plan_years: PlanYearsResource) -> None:
        self._plan_years = plan_years

        self.update = to_raw_response_wrapper(
            plan_years.update,
        )


class AsyncPlanYearsResourceWithRawResponse:
    def __init__(self, plan_years: AsyncPlanYearsResource) -> None:
        self._plan_years = plan_years

        self.update = async_to_raw_response_wrapper(
            plan_years.update,
        )


class PlanYearsResourceWithStreamingResponse:
    def __init__(self, plan_years: PlanYearsResource) -> None:
        self._plan_years = plan_years

        self.update = to_streamed_response_wrapper(
            plan_years.update,
        )


class AsyncPlanYearsResourceWithStreamingResponse:
    def __init__(self, plan_years: AsyncPlanYearsResource) -> None:
        self._plan_years = plan_years

        self.update = async_to_streamed_response_wrapper(
            plan_years.update,
        )
