# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
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
from ..types.benefit_products.plan_year_response import PlanYearResponse

__all__ = ["PlanYearsResource", "AsyncPlanYearsResource"]


class PlanYearsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlanYearsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return PlanYearsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanYearsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return PlanYearsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        plan_year_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYearResponse:
        """Retrieves detailed configuration for a specific plan year by ID.

        Returns
        coverage dates, open enrollment period, available plans, and contribution
        structure.

        Args:
          plan_year_id: Unique plan year identifier (plyr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_year_id:
            raise ValueError(f"Expected a non-empty value for `plan_year_id` but received {plan_year_id!r}")
        return self._get(
            f"/v1/plan-years/{plan_year_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYearResponse,
        )

    def update(
        self,
        plan_year_id: str,
        *,
        contribution_classes: Optional[Iterable[plan_year_update_params.ContributionClass]] | Omit = omit,
        open_enrollment_end: Union[str, date, None] | Omit = omit,
        open_enrollment_start: Union[str, date, None] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYearResponse:
        """Updates an existing plan year's configuration.

        Important: Plan years can only be
        edited until open enrollment starts. All fields are optional. Monetary values
        must be in cents.

        Args:
          plan_year_id: Unique plan year identifier (plyr\\__\\**)

          contribution_classes: Updated contribution classes

          open_enrollment_end: Open enrollment end date

          open_enrollment_start: Open enrollment start date

          status: Plan year status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_year_id:
            raise ValueError(f"Expected a non-empty value for `plan_year_id` but received {plan_year_id!r}")
        return self._put(
            f"/v1/plan-years/{plan_year_id}",
            body=maybe_transform(
                {
                    "contribution_classes": contribution_classes,
                    "open_enrollment_end": open_enrollment_end,
                    "open_enrollment_start": open_enrollment_start,
                    "status": status,
                },
                plan_year_update_params.PlanYearUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYearResponse,
        )


class AsyncPlanYearsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlanYearsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlanYearsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanYearsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-connect-python#with_streaming_response
        """
        return AsyncPlanYearsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        plan_year_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYearResponse:
        """Retrieves detailed configuration for a specific plan year by ID.

        Returns
        coverage dates, open enrollment period, available plans, and contribution
        structure.

        Args:
          plan_year_id: Unique plan year identifier (plyr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_year_id:
            raise ValueError(f"Expected a non-empty value for `plan_year_id` but received {plan_year_id!r}")
        return await self._get(
            f"/v1/plan-years/{plan_year_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYearResponse,
        )

    async def update(
        self,
        plan_year_id: str,
        *,
        contribution_classes: Optional[Iterable[plan_year_update_params.ContributionClass]] | Omit = omit,
        open_enrollment_end: Union[str, date, None] | Omit = omit,
        open_enrollment_start: Union[str, date, None] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanYearResponse:
        """Updates an existing plan year's configuration.

        Important: Plan years can only be
        edited until open enrollment starts. All fields are optional. Monetary values
        must be in cents.

        Args:
          plan_year_id: Unique plan year identifier (plyr\\__\\**)

          contribution_classes: Updated contribution classes

          open_enrollment_end: Open enrollment end date

          open_enrollment_start: Open enrollment start date

          status: Plan year status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_year_id:
            raise ValueError(f"Expected a non-empty value for `plan_year_id` but received {plan_year_id!r}")
        return await self._put(
            f"/v1/plan-years/{plan_year_id}",
            body=await async_maybe_transform(
                {
                    "contribution_classes": contribution_classes,
                    "open_enrollment_end": open_enrollment_end,
                    "open_enrollment_start": open_enrollment_start,
                    "status": status,
                },
                plan_year_update_params.PlanYearUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanYearResponse,
        )


class PlanYearsResourceWithRawResponse:
    def __init__(self, plan_years: PlanYearsResource) -> None:
        self._plan_years = plan_years

        self.retrieve = to_raw_response_wrapper(
            plan_years.retrieve,
        )
        self.update = to_raw_response_wrapper(
            plan_years.update,
        )


class AsyncPlanYearsResourceWithRawResponse:
    def __init__(self, plan_years: AsyncPlanYearsResource) -> None:
        self._plan_years = plan_years

        self.retrieve = async_to_raw_response_wrapper(
            plan_years.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            plan_years.update,
        )


class PlanYearsResourceWithStreamingResponse:
    def __init__(self, plan_years: PlanYearsResource) -> None:
        self._plan_years = plan_years

        self.retrieve = to_streamed_response_wrapper(
            plan_years.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            plan_years.update,
        )


class AsyncPlanYearsResourceWithStreamingResponse:
    def __init__(self, plan_years: AsyncPlanYearsResource) -> None:
        self._plan_years = plan_years

        self.retrieve = async_to_streamed_response_wrapper(
            plan_years.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            plan_years.update,
        )
