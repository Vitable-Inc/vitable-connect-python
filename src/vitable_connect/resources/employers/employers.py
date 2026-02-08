# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date

import httpx

from ...types import (
    employer_list_params,
    employer_create_params,
    employer_update_params,
    employer_create_eligibility_policy_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .employees import (
    EmployeesResource,
    AsyncEmployeesResource,
    EmployeesResourceWithRawResponse,
    AsyncEmployeesResourceWithRawResponse,
    EmployeesResourceWithStreamingResponse,
    AsyncEmployeesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.employer_response import EmployerResponse
from ...types.employer_list_response import EmployerListResponse
from ...types.benefit_eligibility_policy import BenefitEligibilityPolicy

__all__ = ["EmployersResource", "AsyncEmployersResource"]


class EmployersResource(SyncAPIResource):
    @cached_property
    def employees(self) -> EmployeesResource:
        return EmployeesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmployersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return EmployersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return EmployersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: employer_create_params.Address,
        ein: str,
        email: str,
        legal_name: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Creates a new employer for the authenticated organization.

        Requires employer
        name, legal name, EIN, email, and address information. Returns the created
        employer with its assigned ID.

        Args:
          address: Employer address

          ein: Employer Identification Number (format: XX-XXXXXXX)

          email: Email address for billing and communications

          legal_name: Legal business name

          name: Employer display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/employers",
            body=maybe_transform(
                {
                    "address": address,
                    "ein": ein,
                    "email": email,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def retrieve(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Retrieves detailed information for a specific employer by ID.

        The employer must
        belong to the authenticated organization.

        Args:
          employer_id: Filter by employer ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._get(
            f"/v1/employers/{employer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def update(
        self,
        employer_id: str,
        *,
        active: Optional[bool] | Omit = omit,
        address: Optional[employer_update_params.Address] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Updates an existing employer's information.

        All fields are optional - only
        provided fields will be updated. Note: EIN cannot be changed after creation.

        Args:
          employer_id: Filter by employer ID

          active: Whether the employer is active

          address: Employer address

          legal_name: Legal business name

          name: Employer display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._put(
            f"/v1/employers/{employer_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "address": address,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    def list(
        self,
        *,
        active_in: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListResponse:
        """
        Retrieves a paginated list of all employers that the authenticated organization
        has access to. Use query parameters to filter by name or active status. Results
        are paginated using page and limit parameters.

        Args:
          active_in: Filter by active status

          limit: Items per page (default: 20, max: 100)

          name: Filter by employer name (partial match)

          page: Page number (default: 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/employers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_in": active_in,
                        "limit": limit,
                        "name": name,
                        "page": page,
                    },
                    employer_list_params.EmployerListParams,
                ),
            ),
            cast_to=EmployerListResponse,
        )

    def create_eligibility_policy(
        self,
        employer_id: str,
        *,
        effective_date: Union[str, date],
        name: str,
        rules: Iterable[employer_create_eligibility_policy_params.Rule],
        policy_to_replace_id: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenefitEligibilityPolicy:
        """Creates a new benefit eligibility policy for a specific employer.

        Eligibility
        policies define rules that determine which employees qualify for benefits based
        on criteria such as employment status (full-time, part-time), hours worked per
        week, waiting periods after hire date, or other custom requirements. Optionally
        provide 'policy_to_replace_id' as a query parameter to replace an existing
        policy.

        Args:
          employer_id: Filter by employer ID

          effective_date: Date when policy becomes effective

          name: Display name for the policy

          rules: List of eligibility rules (at least one required)

          policy_to_replace_id: ID of existing policy to replace (epol\\__\\**)

          description: Detailed description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return self._post(
            f"/v1/employers/{employer_id}/benefit-eligibility-policies",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "name": name,
                    "rules": rules,
                    "description": description,
                },
                employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"policy_to_replace_id": policy_to_replace_id},
                    employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
                ),
            ),
            cast_to=BenefitEligibilityPolicy,
        )


class AsyncEmployersResource(AsyncAPIResource):
    @cached_property
    def employees(self) -> AsyncEmployeesResource:
        return AsyncEmployeesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmployersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncEmployersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: employer_create_params.Address,
        ein: str,
        email: str,
        legal_name: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Creates a new employer for the authenticated organization.

        Requires employer
        name, legal name, EIN, email, and address information. Returns the created
        employer with its assigned ID.

        Args:
          address: Employer address

          ein: Employer Identification Number (format: XX-XXXXXXX)

          email: Email address for billing and communications

          legal_name: Legal business name

          name: Employer display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/employers",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "ein": ein,
                    "email": email,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_create_params.EmployerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    async def retrieve(
        self,
        employer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Retrieves detailed information for a specific employer by ID.

        The employer must
        belong to the authenticated organization.

        Args:
          employer_id: Filter by employer ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._get(
            f"/v1/employers/{employer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    async def update(
        self,
        employer_id: str,
        *,
        active: Optional[bool] | Omit = omit,
        address: Optional[employer_update_params.Address] | Omit = omit,
        legal_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerResponse:
        """Updates an existing employer's information.

        All fields are optional - only
        provided fields will be updated. Note: EIN cannot be changed after creation.

        Args:
          employer_id: Filter by employer ID

          active: Whether the employer is active

          address: Employer address

          legal_name: Legal business name

          name: Employer display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._put(
            f"/v1/employers/{employer_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "address": address,
                    "legal_name": legal_name,
                    "name": name,
                },
                employer_update_params.EmployerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmployerResponse,
        )

    async def list(
        self,
        *,
        active_in: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmployerListResponse:
        """
        Retrieves a paginated list of all employers that the authenticated organization
        has access to. Use query parameters to filter by name or active status. Results
        are paginated using page and limit parameters.

        Args:
          active_in: Filter by active status

          limit: Items per page (default: 20, max: 100)

          name: Filter by employer name (partial match)

          page: Page number (default: 1)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/employers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_in": active_in,
                        "limit": limit,
                        "name": name,
                        "page": page,
                    },
                    employer_list_params.EmployerListParams,
                ),
            ),
            cast_to=EmployerListResponse,
        )

    async def create_eligibility_policy(
        self,
        employer_id: str,
        *,
        effective_date: Union[str, date],
        name: str,
        rules: Iterable[employer_create_eligibility_policy_params.Rule],
        policy_to_replace_id: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BenefitEligibilityPolicy:
        """Creates a new benefit eligibility policy for a specific employer.

        Eligibility
        policies define rules that determine which employees qualify for benefits based
        on criteria such as employment status (full-time, part-time), hours worked per
        week, waiting periods after hire date, or other custom requirements. Optionally
        provide 'policy_to_replace_id' as a query parameter to replace an existing
        policy.

        Args:
          employer_id: Filter by employer ID

          effective_date: Date when policy becomes effective

          name: Display name for the policy

          rules: List of eligibility rules (at least one required)

          policy_to_replace_id: ID of existing policy to replace (epol\\__\\**)

          description: Detailed description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not employer_id:
            raise ValueError(f"Expected a non-empty value for `employer_id` but received {employer_id!r}")
        return await self._post(
            f"/v1/employers/{employer_id}/benefit-eligibility-policies",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "name": name,
                    "rules": rules,
                    "description": description,
                },
                employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"policy_to_replace_id": policy_to_replace_id},
                    employer_create_eligibility_policy_params.EmployerCreateEligibilityPolicyParams,
                ),
            ),
            cast_to=BenefitEligibilityPolicy,
        )


class EmployersResourceWithRawResponse:
    def __init__(self, employers: EmployersResource) -> None:
        self._employers = employers

        self.create = to_raw_response_wrapper(
            employers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            employers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            employers.update,
        )
        self.list = to_raw_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = to_raw_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> EmployeesResourceWithRawResponse:
        return EmployeesResourceWithRawResponse(self._employers.employees)


class AsyncEmployersResourceWithRawResponse:
    def __init__(self, employers: AsyncEmployersResource) -> None:
        self._employers = employers

        self.create = async_to_raw_response_wrapper(
            employers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            employers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            employers.update,
        )
        self.list = async_to_raw_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = async_to_raw_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> AsyncEmployeesResourceWithRawResponse:
        return AsyncEmployeesResourceWithRawResponse(self._employers.employees)


class EmployersResourceWithStreamingResponse:
    def __init__(self, employers: EmployersResource) -> None:
        self._employers = employers

        self.create = to_streamed_response_wrapper(
            employers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            employers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            employers.update,
        )
        self.list = to_streamed_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = to_streamed_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> EmployeesResourceWithStreamingResponse:
        return EmployeesResourceWithStreamingResponse(self._employers.employees)


class AsyncEmployersResourceWithStreamingResponse:
    def __init__(self, employers: AsyncEmployersResource) -> None:
        self._employers = employers

        self.create = async_to_streamed_response_wrapper(
            employers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            employers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            employers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            employers.list,
        )
        self.create_eligibility_policy = async_to_streamed_response_wrapper(
            employers.create_eligibility_policy,
        )

    @cached_property
    def employees(self) -> AsyncEmployeesResourceWithStreamingResponse:
        return AsyncEmployeesResourceWithStreamingResponse(self._employers.employees)
