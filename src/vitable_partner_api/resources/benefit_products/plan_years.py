# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

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
from ...types.plan_year import PlanYear
from ...types.benefit_products import plan_year_list_params, plan_year_create_params
from ...types.benefit_products.plan_year_list_response import PlanYearListResponse

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

    def create(
        self,
        id: str,
        *,
        coverage_end_date: Union[str, date],
        coverage_start_date: Union[str, date],
        employer_id: str,
        open_enrollment_end_date: Union[str, date],
        open_enrollment_start_date: Union[str, date],
        contribution_classes: Iterable[plan_year_create_params.ContributionClass] | Omit = omit,
        plan_costs: Iterable[plan_year_create_params.PlanCost] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYear:
        """Creates a new Plan Year with configuration for a Benefit Product for an
        Employer.

        Employer would be in request body. Configures Open Enrollment Period,
        Coverage Period, Deductions Per-Plan. Deductions per-plan are tier agnostic –
        costs only for employee and dependent defined.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/benefit-products/{id}/plan-years",
            body=maybe_transform(
                {
                    "coverage_end_date": coverage_end_date,
                    "coverage_start_date": coverage_start_date,
                    "employer_id": employer_id,
                    "open_enrollment_end_date": open_enrollment_end_date,
                    "open_enrollment_start_date": open_enrollment_start_date,
                    "contribution_classes": contribution_classes,
                    "plan_costs": plan_costs,
                },
                plan_year_create_params.PlanYearCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYear,
        )

    def list(
        self,
        id: str,
        *,
        employer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYearListResponse:
        """
        Gets all Plan Years with configuration details for a Benefit Product for an
        Employer. Will be sorted by most recent Plan Year (first Plan Year is the
        latest).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/benefit-products/{id}/plan-years",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"employer_id": employer_id}, plan_year_list_params.PlanYearListParams),
            ),
            cast_to=PlanYearListResponse,
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

    async def create(
        self,
        id: str,
        *,
        coverage_end_date: Union[str, date],
        coverage_start_date: Union[str, date],
        employer_id: str,
        open_enrollment_end_date: Union[str, date],
        open_enrollment_start_date: Union[str, date],
        contribution_classes: Iterable[plan_year_create_params.ContributionClass] | Omit = omit,
        plan_costs: Iterable[plan_year_create_params.PlanCost] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYear:
        """Creates a new Plan Year with configuration for a Benefit Product for an
        Employer.

        Employer would be in request body. Configures Open Enrollment Period,
        Coverage Period, Deductions Per-Plan. Deductions per-plan are tier agnostic –
        costs only for employee and dependent defined.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/benefit-products/{id}/plan-years",
            body=await async_maybe_transform(
                {
                    "coverage_end_date": coverage_end_date,
                    "coverage_start_date": coverage_start_date,
                    "employer_id": employer_id,
                    "open_enrollment_end_date": open_enrollment_end_date,
                    "open_enrollment_start_date": open_enrollment_start_date,
                    "contribution_classes": contribution_classes,
                    "plan_costs": plan_costs,
                },
                plan_year_create_params.PlanYearCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYear,
        )

    async def list(
        self,
        id: str,
        *,
        employer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYearListResponse:
        """
        Gets all Plan Years with configuration details for a Benefit Product for an
        Employer. Will be sorted by most recent Plan Year (first Plan Year is the
        latest).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/benefit-products/{id}/plan-years",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"employer_id": employer_id}, plan_year_list_params.PlanYearListParams
                ),
            ),
            cast_to=PlanYearListResponse,
        )


class PlanYearsResourceWithRawResponse:
    def __init__(self, plan_years: PlanYearsResource) -> None:
        self._plan_years = plan_years

        self.create = to_raw_response_wrapper(
            plan_years.create,
        )
        self.list = to_raw_response_wrapper(
            plan_years.list,
        )


class AsyncPlanYearsResourceWithRawResponse:
    def __init__(self, plan_years: AsyncPlanYearsResource) -> None:
        self._plan_years = plan_years

        self.create = async_to_raw_response_wrapper(
            plan_years.create,
        )
        self.list = async_to_raw_response_wrapper(
            plan_years.list,
        )


class PlanYearsResourceWithStreamingResponse:
    def __init__(self, plan_years: PlanYearsResource) -> None:
        self._plan_years = plan_years

        self.create = to_streamed_response_wrapper(
            plan_years.create,
        )
        self.list = to_streamed_response_wrapper(
            plan_years.list,
        )


class AsyncPlanYearsResourceWithStreamingResponse:
    def __init__(self, plan_years: AsyncPlanYearsResource) -> None:
        self._plan_years = plan_years

        self.create = async_to_streamed_response_wrapper(
            plan_years.create,
        )
        self.list = async_to_streamed_response_wrapper(
            plan_years.list,
        )
