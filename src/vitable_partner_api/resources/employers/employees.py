# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

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
from ...types.employee import Employee
from ...types.employers import employee_list_params, employee_create_params
from ...types.employers.employee_list_response import EmployeeListResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
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

    def create(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date],
        first_name: str,
        last_name: str,
        start_date: Union[str, date],
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
        sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"] | Omit = omit,
        ssn: str | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """Creates a new Employee for an Employer.

        Only the create Employee endpoint allows
        specifying the SSN.

        Args:
          ssn: Social Security Number (only allowed on create)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/employers/{id}/employees",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "start_date": start_date,
                    "gender": gender,
                    "sex": sex,
                    "ssn": ssn,
                    "suffix": suffix,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    def list(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeListResponse:
        """
        Lists all Employees for an Employer.

        Args:
          limit: Number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/employers/{id}/employees",
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
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
        )


class AsyncEmployeesResource(AsyncAPIResource):
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

    async def create(
        self,
        id: str,
        *,
        date_of_birth: Union[str, date],
        first_name: str,
        last_name: str,
        start_date: Union[str, date],
        gender: Literal["MALE", "FEMALE", "TRANSGENDER", "NON_BINARY", "PREFER_NOT_TO_RESPOND"] | Omit = omit,
        sex: Literal["MALE", "FEMALE", "OTHER", "UNKNOWN"] | Omit = omit,
        ssn: str | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Employee:
        """Creates a new Employee for an Employer.

        Only the create Employee endpoint allows
        specifying the SSN.

        Args:
          ssn: Social Security Number (only allowed on create)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/employers/{id}/employees",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "first_name": first_name,
                    "last_name": last_name,
                    "start_date": start_date,
                    "gender": gender,
                    "sex": sex,
                    "ssn": ssn,
                    "suffix": suffix,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Employee,
        )

    async def list(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeListResponse:
        """
        Lists all Employees for an Employer.

        Args:
          limit: Number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/employers/{id}/employees",
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
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
        )


class EmployeesResourceWithRawResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.create = to_raw_response_wrapper(
            employees.create,
        )
        self.list = to_raw_response_wrapper(
            employees.list,
        )


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.create = async_to_raw_response_wrapper(
            employees.create,
        )
        self.list = async_to_raw_response_wrapper(
            employees.list,
        )


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.create = to_streamed_response_wrapper(
            employees.create,
        )
        self.list = to_streamed_response_wrapper(
            employees.list,
        )


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.create = async_to_streamed_response_wrapper(
            employees.create,
        )
        self.list = async_to_streamed_response_wrapper(
            employees.list,
        )
