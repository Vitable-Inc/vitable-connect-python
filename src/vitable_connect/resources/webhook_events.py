# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import webhook_event_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPageNumberPage, AsyncPageNumberPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.webhook_event import WebhookEvent
from ..types.webhook_event_retrieve_response import WebhookEventRetrieveResponse
from ..types.webhook_event_list_deliveries_response import WebhookEventListDeliveriesResponse

__all__ = ["WebhookEventsResource", "AsyncWebhookEventsResource"]


class WebhookEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return WebhookEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return WebhookEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEventRetrieveResponse:
        """Retrieves a single webhook event by its prefixed ID.

        Returns 404 if the event
        does not exist or belongs to a different organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/v1/webhook-events/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEventRetrieveResponse,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        event_name: Literal[
            "enrollment.accepted",
            "enrollment.terminated",
            "enrollment.elected",
            "enrollment.granted",
            "enrollment.waived",
            "enrollment.started",
            "employee.eligibility_granted",
            "employee.eligibility_terminated",
            "employee.deactivated",
            "payroll_deduction.created",
            "plan_year.eligibility_policy_created",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: Literal["enrollment", "employee", "employer", "dependent", "plan_year", "payroll_deduction"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[WebhookEvent]:
        """
        Retrieves a paginated list of webhook events for the authenticated organization.
        Supports filtering by event name, resource type, resource ID, and date range.

        Args:
          event_name: - `enrollment.accepted` - Enrollment Accepted
              - `enrollment.terminated` - Enrollment Terminated
              - `enrollment.elected` - Enrollment Elected
              - `enrollment.granted` - Enrollment Granted
              - `enrollment.waived` - Enrollment Waived
              - `enrollment.started` - Enrollment Started
              - `employee.eligibility_granted` - Employee Eligibility Granted
              - `employee.eligibility_terminated` - Employee Eligibility Terminated
              - `employee.deactivated` - Employee Deactivated
              - `payroll_deduction.created` - Payroll Deduction Created
              - `plan_year.eligibility_policy_created` - Plan Year Eligibility Policy Created

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          resource_type: - `enrollment` - Enrollment
              - `employee` - Employee
              - `employer` - Employer
              - `dependent` - Dependent
              - `plan_year` - Plan Year
              - `payroll_deduction` - Payroll Deduction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/webhook-events",
            page=SyncPageNumberPage[WebhookEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "event_name": event_name,
                        "limit": limit,
                        "page": page,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                    },
                    webhook_event_list_params.WebhookEventListParams,
                ),
            ),
            model=WebhookEvent,
        )

    def list_deliveries(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEventListDeliveriesResponse:
        """Retrieves all delivery attempts for a webhook event.

        Returns up to 100
        deliveries. Each delivery includes a computed status field (Pending, In
        Progress, Delivered, or Failed).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/v1/webhook-events/{event_id}/deliveries", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEventListDeliveriesResponse,
        )


class AsyncWebhookEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncWebhookEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEventRetrieveResponse:
        """Retrieves a single webhook event by its prefixed ID.

        Returns 404 if the event
        does not exist or belongs to a different organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/v1/webhook-events/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEventRetrieveResponse,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        event_name: Literal[
            "enrollment.accepted",
            "enrollment.terminated",
            "enrollment.elected",
            "enrollment.granted",
            "enrollment.waived",
            "enrollment.started",
            "employee.eligibility_granted",
            "employee.eligibility_terminated",
            "employee.deactivated",
            "payroll_deduction.created",
            "plan_year.eligibility_policy_created",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: Literal["enrollment", "employee", "employer", "dependent", "plan_year", "payroll_deduction"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookEvent, AsyncPageNumberPage[WebhookEvent]]:
        """
        Retrieves a paginated list of webhook events for the authenticated organization.
        Supports filtering by event name, resource type, resource ID, and date range.

        Args:
          event_name: - `enrollment.accepted` - Enrollment Accepted
              - `enrollment.terminated` - Enrollment Terminated
              - `enrollment.elected` - Enrollment Elected
              - `enrollment.granted` - Enrollment Granted
              - `enrollment.waived` - Enrollment Waived
              - `enrollment.started` - Enrollment Started
              - `employee.eligibility_granted` - Employee Eligibility Granted
              - `employee.eligibility_terminated` - Employee Eligibility Terminated
              - `employee.deactivated` - Employee Deactivated
              - `payroll_deduction.created` - Payroll Deduction Created
              - `plan_year.eligibility_policy_created` - Plan Year Eligibility Policy Created

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          resource_type: - `enrollment` - Enrollment
              - `employee` - Employee
              - `employer` - Employer
              - `dependent` - Dependent
              - `plan_year` - Plan Year
              - `payroll_deduction` - Payroll Deduction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/webhook-events",
            page=AsyncPageNumberPage[WebhookEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "event_name": event_name,
                        "limit": limit,
                        "page": page,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                    },
                    webhook_event_list_params.WebhookEventListParams,
                ),
            ),
            model=WebhookEvent,
        )

    async def list_deliveries(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEventListDeliveriesResponse:
        """Retrieves all delivery attempts for a webhook event.

        Returns up to 100
        deliveries. Each delivery includes a computed status field (Pending, In
        Progress, Delivered, or Failed).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/v1/webhook-events/{event_id}/deliveries", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEventListDeliveriesResponse,
        )


class WebhookEventsResourceWithRawResponse:
    def __init__(self, webhook_events: WebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = to_raw_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            webhook_events.list,
        )
        self.list_deliveries = to_raw_response_wrapper(
            webhook_events.list_deliveries,
        )


class AsyncWebhookEventsResourceWithRawResponse:
    def __init__(self, webhook_events: AsyncWebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = async_to_raw_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            webhook_events.list,
        )
        self.list_deliveries = async_to_raw_response_wrapper(
            webhook_events.list_deliveries,
        )


class WebhookEventsResourceWithStreamingResponse:
    def __init__(self, webhook_events: WebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = to_streamed_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            webhook_events.list,
        )
        self.list_deliveries = to_streamed_response_wrapper(
            webhook_events.list_deliveries,
        )


class AsyncWebhookEventsResourceWithStreamingResponse:
    def __init__(self, webhook_events: AsyncWebhookEventsResource) -> None:
        self._webhook_events = webhook_events

        self.retrieve = async_to_streamed_response_wrapper(
            webhook_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_events.list,
        )
        self.list_deliveries = async_to_streamed_response_wrapper(
            webhook_events.list_deliveries,
        )
