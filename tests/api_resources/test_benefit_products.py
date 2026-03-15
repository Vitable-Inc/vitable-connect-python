# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import BenefitProductListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenefitProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        benefit_product = client.benefit_products.list()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        benefit_product = client.benefit_products.list(
            active_in=True,
            category="Medical",
            limit=20,
            page=1,
            product_code="EBA",
        )
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.benefit_products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit_product = response.parse()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.benefit_products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit_product = response.parse()
            assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBenefitProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        benefit_product = await async_client.benefit_products.list()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        benefit_product = await async_client.benefit_products.list(
            active_in=True,
            category="Medical",
            limit=20,
            page=1,
            product_code="EBA",
        )
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.benefit_products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit_product = await response.parse()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.benefit_products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit_product = await response.parse()
            assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

        assert cast(Any, response.is_closed) is True
