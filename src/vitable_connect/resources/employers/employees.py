# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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
from ...types.employers import Sex, EmployeeClass, employee_list_params, employee_create_params
from ...types.employers.sex import Sex
from ...types.employee_response import EmployeeResponse
from ...types.employers.employee_class import EmployeeClass
from ...types.employers.employee_list_response import EmployeeListResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    """Manage employee records for employers"""

    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return EmployeesResourceWithStreamingResponse(self)

    def create(
        self,
        employer_id: str,
        *,
        date_of_birth: Union[str, date],
        email: str,
        first_name: str,
        last_name: str,
        sex: Sex,
        ssn: str,
        start_date: Union[str, date],
        address: Optional[employee_create_params.Address] | Omit = omit,
        employee_class: Optional[EmployeeClass] | Omit = omit,
        gender: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        suffix: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeResponse:
        """Creates a new employee for a specific employer.

        Requires personal information
        (name, DOB, SSN) and employment details (start date). Note: SSN can only be
        specified at creation time and cannot be updated later. Returns the created
        employee with assigned ID.

        Args:
          employer_id: Filter by employer ID

          date_of_birth: Date of birth (YYYY-MM-DD)

          email: Email address

          first_name: Employee's legal first name

          last_name: Employee's legal last name

          sex: - `Male` - Male
              - `Female` - Female
              - `Other` - Other
              - `Unknown` - Unknown

          ssn: Social Security Number (XXX-XX-XXXX or XXXXXXXXX). Only accepted on create.

          start_date: Employment start/hire date

          address: Employee's residential address

          employee_class: - `Full Time` - Full Time
              - `Part Time` - Part Time
              - `Temporary` - Temporary
              - `Intern` - Intern
              - `Seasonal` - Seasonal
              - `Individual Contractor` - Individual Contractor

          gender: Gender identity

          phone: Phone number

          suffix: Name suffix (Jr., Sr., III)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._post(
            f"/v1/employers/{employer_id}/employees",
            body=maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "sex": sex,
                    "ssn": ssn,
                    "start_date": start_date,
                    "address": address,
                    "employee_class": employee_class,
                    "gender": gender,
                    "phone": phone,
                    "suffix": suffix,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeResponse,
        )

    def list(
        self,
        employer_id: str,
        *,
        active_in: bool | Omit = omit,
        employee_class: EmployeeClass | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeListResponse:
        """Retrieves a paginated list of all employees for a specific employer.

        Use query
        parameters to filter by active status or employment classification. Results are
        paginated using page and limit parameters.

        Args:
          employer_id: Filter by employer ID

          active_in: Filter by active status

          employee_class: Filter by employment classification

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            f"/v1/employers/{employer_id}/employees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_in": active_in,
                        "employee_class": employee_class,
                        "limit": limit,
                        "page": page,
                    },
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    """Manage employee records for employers"""

    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncEmployeesResourceWithStreamingResponse(self)

    async def create(
        self,
        employer_id: str,
        *,
        date_of_birth: Union[str, date],
        email: str,
        first_name: str,
        last_name: str,
        sex: Sex,
        ssn: str,
        start_date: Union[str, date],
        address: Optional[employee_create_params.Address] | Omit = omit,
        employee_class: Optional[EmployeeClass] | Omit = omit,
        gender: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        suffix: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeResponse:
        """Creates a new employee for a specific employer.

        Requires personal information
        (name, DOB, SSN) and employment details (start date). Note: SSN can only be
        specified at creation time and cannot be updated later. Returns the created
        employee with assigned ID.

        Args:
          employer_id: Filter by employer ID

          date_of_birth: Date of birth (YYYY-MM-DD)

          email: Email address

          first_name: Employee's legal first name

          last_name: Employee's legal last name

          sex: - `Male` - Male
              - `Female` - Female
              - `Other` - Other
              - `Unknown` - Unknown

          ssn: Social Security Number (XXX-XX-XXXX or XXXXXXXXX). Only accepted on create.

          start_date: Employment start/hire date

          address: Employee's residential address

          employee_class: - `Full Time` - Full Time
              - `Part Time` - Part Time
              - `Temporary` - Temporary
              - `Intern` - Intern
              - `Seasonal` - Seasonal
              - `Individual Contractor` - Individual Contractor

          gender: Gender identity

          phone: Phone number

          suffix: Name suffix (Jr., Sr., III)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._post(
            f"/v1/employers/{employer_id}/employees",
            body=await async_maybe_transform(
                {
                    "date_of_birth": date_of_birth,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "sex": sex,
                    "ssn": ssn,
                    "start_date": start_date,
                    "address": address,
                    "employee_class": employee_class,
                    "gender": gender,
                    "phone": phone,
                    "suffix": suffix,
                },
                employee_create_params.EmployeeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployeeResponse,
        )

    async def list(
        self,
        employer_id: str,
        *,
        active_in: bool | Omit = omit,
        employee_class: EmployeeClass | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployeeListResponse:
        """Retrieves a paginated list of all employees for a specific employer.

        Use query
        parameters to filter by active status or employment classification. Results are
        paginated using page and limit parameters.

        Args:
          employer_id: Filter by employer ID

          active_in: Filter by active status

          employee_class: Filter by employment classification

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            f"/v1/employers/{employer_id}/employees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_in": active_in,
                        "employee_class": employee_class,
                        "limit": limit,
                        "page": page,
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
