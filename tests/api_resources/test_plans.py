# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import PlanListResponse
from vitable_connect.pagination import SyncPageNumberPage, AsyncPageNumberPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        plan = client.plans.list()
        assert_matches_type(SyncPageNumberPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        plan = client.plans.list(
            limit=20,
            page=1,
        )
        assert_matches_type(SyncPageNumberPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncPageNumberPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncPageNumberPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        plan = await async_client.plans.list()
        assert_matches_type(AsyncPageNumberPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        plan = await async_client.plans.list(
            limit=20,
            page=1,
        )
        assert_matches_type(AsyncPageNumberPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncPageNumberPage[PlanListResponse], plan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncPageNumberPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True
