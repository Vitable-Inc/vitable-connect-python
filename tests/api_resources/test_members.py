# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import (
    MemberListResponse,
    MemberRetrieveResponse,
    MemberListIDCardsResponse,
    MemberListDependentsResponse,
    MemberListEmploymentsResponse,
    MemberListEnrollmentsResponse,
    MemberRetrieveHouseholdResponse,
    MemberListQualifyingLifeEventsResponse,
)
from vitable_connect.pagination import SyncPageNumberPage, AsyncPageNumberPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        member = client.members.retrieve(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberRetrieveResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.retrieve(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberRetrieveResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.retrieve(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberRetrieveResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        member = client.members.list()
        assert_matches_type(SyncPageNumberPage[MemberListResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        member = client.members.list(
            limit=20,
            page=1,
            search="search",
        )
        assert_matches_type(SyncPageNumberPage[MemberListResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(SyncPageNumberPage[MemberListResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(SyncPageNumberPage[MemberListResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_dependents(self, client: VitableConnect) -> None:
        member = client.members.list_dependents(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListDependentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_dependents(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.list_dependents(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberListDependentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_dependents(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.list_dependents(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberListDependentsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_dependents(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.list_dependents(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_employments(self, client: VitableConnect) -> None:
        member = client.members.list_employments(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListEmploymentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_employments(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.list_employments(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberListEmploymentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_employments(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.list_employments(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberListEmploymentsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_employments(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.list_employments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enrollments(self, client: VitableConnect) -> None:
        member = client.members.list_enrollments(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListEnrollmentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_enrollments(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.list_enrollments(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberListEnrollmentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_enrollments(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.list_enrollments(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberListEnrollmentsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_enrollments(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.list_enrollments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_id_cards(self, client: VitableConnect) -> None:
        member = client.members.list_id_cards(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListIDCardsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_id_cards(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.list_id_cards(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberListIDCardsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_id_cards(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.list_id_cards(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberListIDCardsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_id_cards(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.list_id_cards(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_qualifying_life_events(self, client: VitableConnect) -> None:
        member = client.members.list_qualifying_life_events(
            member_id="mbr_abc123def456",
        )
        assert_matches_type(SyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_qualifying_life_events_with_all_params(self, client: VitableConnect) -> None:
        member = client.members.list_qualifying_life_events(
            member_id="mbr_abc123def456",
            limit=20,
            page=1,
            status="approved",
        )
        assert_matches_type(SyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_qualifying_life_events(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.list_qualifying_life_events(
            member_id="mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(SyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_qualifying_life_events(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.list_qualifying_life_events(
            member_id="mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(SyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_qualifying_life_events(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.list_qualifying_life_events(
                member_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_household(self, client: VitableConnect) -> None:
        member = client.members.retrieve_household(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberRetrieveHouseholdResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_household(self, client: VitableConnect) -> None:
        response = client.members.with_raw_response.retrieve_household(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberRetrieveHouseholdResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_household(self, client: VitableConnect) -> None:
        with client.members.with_streaming_response.retrieve_household(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberRetrieveHouseholdResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_household(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.retrieve_household(
                "",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.retrieve(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberRetrieveResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.retrieve(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberRetrieveResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.retrieve(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberRetrieveResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list()
        assert_matches_type(AsyncPageNumberPage[MemberListResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list(
            limit=20,
            page=1,
            search="search",
        )
        assert_matches_type(AsyncPageNumberPage[MemberListResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(AsyncPageNumberPage[MemberListResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(AsyncPageNumberPage[MemberListResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_dependents(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list_dependents(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListDependentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_dependents(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.list_dependents(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberListDependentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_dependents(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.list_dependents(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberListDependentsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_dependents(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.list_dependents(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_employments(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list_employments(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListEmploymentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_employments(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.list_employments(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberListEmploymentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_employments(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.list_employments(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberListEmploymentsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_employments(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.list_employments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enrollments(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list_enrollments(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListEnrollmentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_enrollments(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.list_enrollments(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberListEnrollmentsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_enrollments(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.list_enrollments(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberListEnrollmentsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_enrollments(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.list_enrollments(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_id_cards(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list_id_cards(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberListIDCardsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_id_cards(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.list_id_cards(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberListIDCardsResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_id_cards(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.list_id_cards(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberListIDCardsResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_id_cards(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.list_id_cards(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_qualifying_life_events(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list_qualifying_life_events(
            member_id="mbr_abc123def456",
        )
        assert_matches_type(AsyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_qualifying_life_events_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.list_qualifying_life_events(
            member_id="mbr_abc123def456",
            limit=20,
            page=1,
            status="approved",
        )
        assert_matches_type(AsyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_qualifying_life_events(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.list_qualifying_life_events(
            member_id="mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(AsyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_qualifying_life_events(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.list_qualifying_life_events(
            member_id="mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(AsyncPageNumberPage[MemberListQualifyingLifeEventsResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_qualifying_life_events(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.list_qualifying_life_events(
                member_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_household(self, async_client: AsyncVitableConnect) -> None:
        member = await async_client.members.retrieve_household(
            "mbr_abc123def456",
        )
        assert_matches_type(MemberRetrieveHouseholdResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_household(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.with_raw_response.retrieve_household(
            "mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberRetrieveHouseholdResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_household(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.with_streaming_response.retrieve_household(
            "mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberRetrieveHouseholdResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_household(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.retrieve_household(
                "",
            )
