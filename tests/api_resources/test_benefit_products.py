# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import (
    Quote,
    BenefitProductListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBenefitProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        benefit_product = client.benefit_products.list()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnectAPI) -> None:
        benefit_product = client.benefit_products.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.benefit_products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit_product = response.parse()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.benefit_products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit_product = response.parse()
            assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_quote(self, client: VitableConnectAPI) -> None:
        benefit_product = client.benefit_products.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
        )
        assert_matches_type(Quote, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_quote_with_all_params(self, client: VitableConnectAPI) -> None:
        benefit_product = client.benefit_products.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Quote, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_quote(self, client: VitableConnectAPI) -> None:
        response = client.benefit_products.with_raw_response.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit_product = response.parse()
        assert_matches_type(Quote, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_quote(self, client: VitableConnectAPI) -> None:
        with client.benefit_products.with_streaming_response.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit_product = response.parse()
            assert_matches_type(Quote, benefit_product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_quote(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.benefit_products.with_raw_response.generate_quote(
                id="",
                employer_id="empr__1k--w2KifJ1",
            )


class TestAsyncBenefitProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        benefit_product = await async_client.benefit_products.list()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        benefit_product = await async_client.benefit_products.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.benefit_products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit_product = await response.parse()
        assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.benefit_products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit_product = await response.parse()
            assert_matches_type(BenefitProductListResponse, benefit_product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_quote(self, async_client: AsyncVitableConnectAPI) -> None:
        benefit_product = await async_client.benefit_products.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
        )
        assert_matches_type(Quote, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_quote_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        benefit_product = await async_client.benefit_products.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Quote, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_quote(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.benefit_products.with_raw_response.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        benefit_product = await response.parse()
        assert_matches_type(Quote, benefit_product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_quote(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.benefit_products.with_streaming_response.generate_quote(
            id="bprd__1k--w2KifJ1",
            employer_id="empr__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            benefit_product = await response.parse()
            assert_matches_type(Quote, benefit_product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_quote(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.benefit_products.with_raw_response.generate_quote(
                id="",
                employer_id="empr__1k--w2KifJ1",
            )
