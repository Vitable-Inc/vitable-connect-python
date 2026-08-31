# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import member_list_params, member_list_qualifying_life_events_params
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
from ..types.member_list_response import MemberListResponse
from ..types.member_retrieve_response import MemberRetrieveResponse
from ..types.member_list_id_cards_response import MemberListIDCardsResponse
from ..types.member_list_dependents_response import MemberListDependentsResponse
from ..types.member_list_employments_response import MemberListEmploymentsResponse
from ..types.member_list_enrollments_response import MemberListEnrollmentsResponse
from ..types.member_retrieve_household_response import MemberRetrieveHouseholdResponse
from ..types.member_list_qualifying_life_events_response import MemberListQualifyingLifeEventsResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    """Browse the members covered across your book and read a member's profile"""

    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRetrieveResponse:
        """
        Retrieves a member's profile by ID — identity, demographics, address, contact
        details, tobacco status, and profile status. Access is scoped to the
        authenticated principal; a member not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template("/v1/members/{member_id}", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[MemberListResponse]:
        """
        Retrieves a paginated list of the members in the authenticated organization's
        book — identity, contact details, and address. The book covers members reached
        through an employer in the organization's book as well as members of a group it
        owns. Supports free-text search (name, email, or exact member id).

        Args:
          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          search: Case-insensitive search across member name and email; exact match on member id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/members",
            page=SyncPageNumberPage[MemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MemberListResponse,
        )

    def list_dependents(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListDependentsResponse:
        """
        Lists a member's active legal dependents — name, relationship, date of birth,
        age, and sex at birth. Access is scoped to the authenticated principal; a member
        not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template("/v1/members/{member_id}/dependents", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListDependentsResponse,
        )

    def list_employments(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListEmploymentsResponse:
        """
        Lists a member's employment across every employer — the same employee record
        shape as the employer's employees list, plus the employer name. For an
        organization caller the rows are scoped to companies in that organization's
        book; a member (self/household) or Vitable Admin sees all employments. A member
        not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template("/v1/members/{member_id}/employments", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListEmploymentsResponse,
        )

    def list_enrollments(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListEnrollmentsResponse:
        """
        Lists a member's benefit enrollments across every employer — benefit type and
        product, employer, carrier, plan, tier, employee deduction, employer
        contribution and total premium, the individual enrollment coverage boundary
        (`coverage_end`), the separate pre-effective cancellation boundary
        (`cancelled_date`), and the distinct benefit plan-year boundary
        (`plan_year_coverage_end`) used to determine whether the plan year itself has
        ended, the date the enrollment record was created (`issued_date`, the value Ops
        labels Issued on, reported for every row whatever the member answered), whether
        a qualifying life event would currently be required for reissue under the
        product/open-enrollment rule, enrollment/open-enrollment window, and two
        statuses: `election_status` (what the member answered) and `policy_status` (what
        became of their coverage, null unless they enrolled). Every row includes a
        stable enrollment ID and the exact employer and benefit plan-year IDs used to
        fetch that row's plan-year detail. The full list is returned across all states
        so the client derives active plans (effective and upcoming) and the enrollment
        history from those per-row statuses. For an organization caller the rows are
        scoped to companies in that organization's book; a member (self/household) or
        Vitable Admin sees all enrollments. A member not visible to the caller returns
        a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template("/v1/members/{member_id}/enrollments", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListEnrollmentsResponse,
        )

    def list_id_cards(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListIDCardsResponse:
        """
        Lists a member's benefit ID cards — card type (medical, dental, vision, or rx),
        employer, plan, provider network, claims payer, carrier contact details, and the
        disclaimers printed on the card. Medical, dental and vision cards come from the
        member's active digital benefit cards; the rx card from the member's Ventegra
        pharmacy benefit (omitted when the member has no free-medication coverage),
        which carries no plan, network, or carrier details. Access is scoped to the
        authenticated principal, and an organization caller sees only cards from
        employers in its book; a member not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template("/v1/members/{member_id}/id-cards", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListIDCardsResponse,
        )

    def list_qualifying_life_events(
        self,
        member_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: Literal["approved", "denied", "pending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPage[MemberListQualifyingLifeEventsResponse]:
        """
        Lists a member's qualifying life events, including events already used for
        another enrollment. Returns all statuses by default; pass the status query param
        to filter to one (e.g. approved). Events are ordered newest submission first
        with stable paging. Custom text is present only when submitted and is otherwise
        null. A member not visible to the caller returns a 404. API keys and unbound
        access tokens have organization-wide access. Employer-bound tokens require
        employment at the bound employer, and employee-bound tokens require the exact
        employee-member relationship. Organization or scope mismatches return a 404
        before pagination is validated.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          status: Optional. Filter to a single QLE status; omit to return all statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get_api_list(
            path_template("/v1/members/{member_id}/qualifying-life-events", member_id=member_id),
            page=SyncPageNumberPage[MemberListQualifyingLifeEventsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    member_list_qualifying_life_events_params.MemberListQualifyingLifeEventsParams,
                ),
            ),
            model=MemberListQualifyingLifeEventsResponse,
        )

    def retrieve_household(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRetrieveHouseholdResponse:
        """
        Lists a member's household as a per-participant table — the account holder plus
        each active household member, with name, relationship, member type, date of
        birth, and household-admin flag. Access is scoped to the authenticated
        principal; a member not visible to the caller (or with no household) returns
        a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get(
            path_template("/v1/members/{member_id}/household", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveHouseholdResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    """Browse the members covered across your book and read a member's profile"""

    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRetrieveResponse:
        """
        Retrieves a member's profile by ID — identity, demographics, address, contact
        details, tobacco status, and profile status. Access is scoped to the
        authenticated principal; a member not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template("/v1/members/{member_id}", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MemberListResponse, AsyncPageNumberPage[MemberListResponse]]:
        """
        Retrieves a paginated list of the members in the authenticated organization's
        book — identity, contact details, and address. The book covers members reached
        through an employer in the organization's book as well as members of a group it
        owns. Supports free-text search (name, email, or exact member id).

        Args:
          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          search: Case-insensitive search across member name and email; exact match on member id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/members",
            page=AsyncPageNumberPage[MemberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "search": search,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MemberListResponse,
        )

    async def list_dependents(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListDependentsResponse:
        """
        Lists a member's active legal dependents — name, relationship, date of birth,
        age, and sex at birth. Access is scoped to the authenticated principal; a member
        not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template("/v1/members/{member_id}/dependents", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListDependentsResponse,
        )

    async def list_employments(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListEmploymentsResponse:
        """
        Lists a member's employment across every employer — the same employee record
        shape as the employer's employees list, plus the employer name. For an
        organization caller the rows are scoped to companies in that organization's
        book; a member (self/household) or Vitable Admin sees all employments. A member
        not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template("/v1/members/{member_id}/employments", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListEmploymentsResponse,
        )

    async def list_enrollments(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListEnrollmentsResponse:
        """
        Lists a member's benefit enrollments across every employer — benefit type and
        product, employer, carrier, plan, tier, employee deduction, employer
        contribution and total premium, the individual enrollment coverage boundary
        (`coverage_end`), the separate pre-effective cancellation boundary
        (`cancelled_date`), and the distinct benefit plan-year boundary
        (`plan_year_coverage_end`) used to determine whether the plan year itself has
        ended, the date the enrollment record was created (`issued_date`, the value Ops
        labels Issued on, reported for every row whatever the member answered), whether
        a qualifying life event would currently be required for reissue under the
        product/open-enrollment rule, enrollment/open-enrollment window, and two
        statuses: `election_status` (what the member answered) and `policy_status` (what
        became of their coverage, null unless they enrolled). Every row includes a
        stable enrollment ID and the exact employer and benefit plan-year IDs used to
        fetch that row's plan-year detail. The full list is returned across all states
        so the client derives active plans (effective and upcoming) and the enrollment
        history from those per-row statuses. For an organization caller the rows are
        scoped to companies in that organization's book; a member (self/household) or
        Vitable Admin sees all enrollments. A member not visible to the caller returns
        a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template("/v1/members/{member_id}/enrollments", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListEnrollmentsResponse,
        )

    async def list_id_cards(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberListIDCardsResponse:
        """
        Lists a member's benefit ID cards — card type (medical, dental, vision, or rx),
        employer, plan, provider network, claims payer, carrier contact details, and the
        disclaimers printed on the card. Medical, dental and vision cards come from the
        member's active digital benefit cards; the rx card from the member's Ventegra
        pharmacy benefit (omitted when the member has no free-medication coverage),
        which carries no plan, network, or carrier details. Access is scoped to the
        authenticated principal, and an organization caller sees only cards from
        employers in its book; a member not visible to the caller returns a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template("/v1/members/{member_id}/id-cards", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberListIDCardsResponse,
        )

    def list_qualifying_life_events(
        self,
        member_id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: Literal["approved", "denied", "pending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        MemberListQualifyingLifeEventsResponse, AsyncPageNumberPage[MemberListQualifyingLifeEventsResponse]
    ]:
        """
        Lists a member's qualifying life events, including events already used for
        another enrollment. Returns all statuses by default; pass the status query param
        to filter to one (e.g. approved). Events are ordered newest submission first
        with stable paging. Custom text is present only when submitted and is otherwise
        null. A member not visible to the caller returns a 404. API keys and unbound
        access tokens have organization-wide access. Employer-bound tokens require
        employment at the bound employer, and employee-bound tokens require the exact
        employee-member relationship. Organization or scope mismatches return a 404
        before pagination is validated.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          limit: Items per page (default: 20, max: 100)

          page: Page number (default: 1)

          status: Optional. Filter to a single QLE status; omit to return all statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return self._get_api_list(
            path_template("/v1/members/{member_id}/qualifying-life-events", member_id=member_id),
            page=AsyncPageNumberPage[MemberListQualifyingLifeEventsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    member_list_qualifying_life_events_params.MemberListQualifyingLifeEventsParams,
                ),
            ),
            model=MemberListQualifyingLifeEventsResponse,
        )

    async def retrieve_household(
        self,
        member_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberRetrieveHouseholdResponse:
        """
        Lists a member's household as a per-participant table — the account holder plus
        each active household member, with name, relationship, member type, date of
        birth, and household-admin flag. Access is scoped to the authenticated
        principal; a member not visible to the caller (or with no household) returns
        a 404.

        Args:
          member_id: Unique member identifier (mbr\\__\\**)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not member_id:
            raise ValueError(f"Expected a non-empty value for `member_id` but received {member_id!r}")
        return await self._get(
            path_template("/v1/members/{member_id}/household", member_id=member_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberRetrieveHouseholdResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.retrieve = to_raw_response_wrapper(
            members.retrieve,
        )
        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.list_dependents = to_raw_response_wrapper(
            members.list_dependents,
        )
        self.list_employments = to_raw_response_wrapper(
            members.list_employments,
        )
        self.list_enrollments = to_raw_response_wrapper(
            members.list_enrollments,
        )
        self.list_id_cards = to_raw_response_wrapper(
            members.list_id_cards,
        )
        self.list_qualifying_life_events = to_raw_response_wrapper(
            members.list_qualifying_life_events,
        )
        self.retrieve_household = to_raw_response_wrapper(
            members.retrieve_household,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.retrieve = async_to_raw_response_wrapper(
            members.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.list_dependents = async_to_raw_response_wrapper(
            members.list_dependents,
        )
        self.list_employments = async_to_raw_response_wrapper(
            members.list_employments,
        )
        self.list_enrollments = async_to_raw_response_wrapper(
            members.list_enrollments,
        )
        self.list_id_cards = async_to_raw_response_wrapper(
            members.list_id_cards,
        )
        self.list_qualifying_life_events = async_to_raw_response_wrapper(
            members.list_qualifying_life_events,
        )
        self.retrieve_household = async_to_raw_response_wrapper(
            members.retrieve_household,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.retrieve = to_streamed_response_wrapper(
            members.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.list_dependents = to_streamed_response_wrapper(
            members.list_dependents,
        )
        self.list_employments = to_streamed_response_wrapper(
            members.list_employments,
        )
        self.list_enrollments = to_streamed_response_wrapper(
            members.list_enrollments,
        )
        self.list_id_cards = to_streamed_response_wrapper(
            members.list_id_cards,
        )
        self.list_qualifying_life_events = to_streamed_response_wrapper(
            members.list_qualifying_life_events,
        )
        self.retrieve_household = to_streamed_response_wrapper(
            members.retrieve_household,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.retrieve = async_to_streamed_response_wrapper(
            members.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.list_dependents = async_to_streamed_response_wrapper(
            members.list_dependents,
        )
        self.list_employments = async_to_streamed_response_wrapper(
            members.list_employments,
        )
        self.list_enrollments = async_to_streamed_response_wrapper(
            members.list_enrollments,
        )
        self.list_id_cards = async_to_streamed_response_wrapper(
            members.list_id_cards,
        )
        self.list_qualifying_life_events = async_to_streamed_response_wrapper(
            members.list_qualifying_life_events,
        )
        self.retrieve_household = async_to_streamed_response_wrapper(
            members.retrieve_household,
        )
