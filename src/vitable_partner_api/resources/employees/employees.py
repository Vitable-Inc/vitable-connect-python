# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import employee_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .dependents import (
    DependentsResource,
    AsyncDependentsResource,
    DependentsResourceWithRawResponse,
    AsyncDependentsResourceWithRawResponse,
    DependentsResourceWithStreamingResponse,
    AsyncDependentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .enrollments import (
    EnrollmentsResource,
    AsyncEnrollmentsResource,
    EnrollmentsResourceWithRawResponse,
    AsyncEnrollmentsResourceWithRawResponse,
    EnrollmentsResourceWithStreamingResponse,
    AsyncEnrollmentsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.employee import Employee
from .qualifying_life_events import (
    QualifyingLifeEventsResource,
    AsyncQualifyingLifeEventsResource,
    QualifyingLifeEventsResourceWithRawResponse,
    AsyncQualifyingLifeEventsResourceWithRawResponse,
    QualifyingLifeEventsResourceWithStreamingResponse,
    AsyncQualifyingLifeEventsResourceWithStreamingResponse,
)

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def dependents(self) -> DependentsResource:
        return DependentsResource(self._client)

    @cached_property
    def qualifying_life_events(self) -> QualifyingLifeEventsResource:
        return QualifyingLifeEventsResource(self._client)

    @cached_property
    def enrollments(self) -> EnrollmentsResource:
        return EnrollmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return EmployeesResourceWithStreamingResponse(self)

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
    ) -> Employee:
        """
        Gets a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def update(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date] | Omit = omit,
        first_name: str | Omit = omit,
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
        last_name: str | Omit = omit,
        sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Updates a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/employees/{id}",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "gender": gender,
                    "last_name": last_name,
                    "sex": sex,
                    "start_date": start_date,
                    "suffix": suffix,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def terminate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminates a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    @cached_property
    def dependents(self) -> AsyncDependentsResource:
        return AsyncDependentsResource(self._client)

    @cached_property
    def qualifying_life_events(self) -> AsyncQualifyingLifeEventsResource:
        return AsyncQualifyingLifeEventsResource(self._client)

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResource:
        return AsyncEnrollmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/vitable-partner-api-python#with_streaming_response
        """
        return AsyncEmployeesResourceWithStreamingResponse(self)

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
    ) -> Employee:
        """
        Gets a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def update(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date] | Omit = omit,
        first_name: str | Omit = omit,
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
        last_name: str | Omit = omit,
        sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """
        Updates a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/employees/{id}",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "gender": gender,
                    "last_name": last_name,
                    "sex": sex,
                    "start_date": start_date,
                    "suffix": suffix,
                },
                employee_update_params.EmployeeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def terminate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminates a specific Employee for an Employer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmployeesResourceWithRawResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employees.update,
        )
        self.terminate = to_raw_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def dependents(self) -> DependentsResourceWithRawResponse:
        return DependentsResourceWithRawResponse(self._employees.dependents)

    @cached_property
    def qualifying_life_events(self) -> QualifyingLifeEventsResourceWithRawResponse:
        return QualifyingLifeEventsResourceWithRawResponse(self._employees.qualifying_life_events)

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithRawResponse:
        return EnrollmentsResourceWithRawResponse(self._employees.enrollments)


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_raw_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employees.update,
        )
        self.terminate = async_to_raw_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def dependents(self) -> AsyncDependentsResourceWithRawResponse:
        return AsyncDependentsResourceWithRawResponse(self._employees.dependents)

    @cached_property
    def qualifying_life_events(self) -> AsyncQualifyingLifeEventsResourceWithRawResponse:
        return AsyncQualifyingLifeEventsResourceWithRawResponse(self._employees.qualifying_life_events)

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithRawResponse:
        return AsyncEnrollmentsResourceWithRawResponse(self._employees.enrollments)


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.retrieve = to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employees.update,
        )
        self.terminate = to_streamed_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def dependents(self) -> DependentsResourceWithStreamingResponse:
        return DependentsResourceWithStreamingResponse(self._employees.dependents)

    @cached_property
    def qualifying_life_events(self) -> QualifyingLifeEventsResourceWithStreamingResponse:
        return QualifyingLifeEventsResourceWithStreamingResponse(self._employees.qualifying_life_events)

    @cached_property
    def enrollments(self) -> EnrollmentsResourceWithStreamingResponse:
        return EnrollmentsResourceWithStreamingResponse(self._employees.enrollments)


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.retrieve = async_to_streamed_response_wrapper(
            employees.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employees.update,
        )
        self.terminate = async_to_streamed_response_wrapper(
            employees.terminate,
        )

    @cached_property
    def dependents(self) -> AsyncDependentsResourceWithStreamingResponse:
        return AsyncDependentsResourceWithStreamingResponse(self._employees.dependents)

    @cached_property
    def qualifying_life_events(self) -> AsyncQualifyingLifeEventsResourceWithStreamingResponse:
        return AsyncQualifyingLifeEventsResourceWithStreamingResponse(self._employees.qualifying_life_events)

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResourceWithStreamingResponse:
        return AsyncEnrollmentsResourceWithStreamingResponse(self._employees.enrollments)
