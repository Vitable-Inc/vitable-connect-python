# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import DependentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDependents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        dependent = client.dependents.retrieve(
            "dpnd_abc123def456",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.dependents.with_raw_response.retrieve(
            "dpnd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = response.parse()
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.dependents.with_streaming_response.retrieve(
            "dpnd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = response.parse()
            assert_matches_type(DependentResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependent_id` but received ''"):
            client.dependents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnect) -> None:
        dependent = client.dependents.update(
            dependent_id="dpnd_abc123def456",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnect) -> None:
        dependent = client.dependents.update(
            dependent_id="dpnd_abc123def456",
            active=True,
            gender="gender",
            relationship="Spouse",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnect) -> None:
        response = client.dependents.with_raw_response.update(
            dependent_id="dpnd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = response.parse()
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnect) -> None:
        with client.dependents.with_streaming_response.update(
            dependent_id="dpnd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = response.parse()
            assert_matches_type(DependentResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependent_id` but received ''"):
            client.dependents.with_raw_response.update(
                dependent_id="",
            )


class TestAsyncDependents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.dependents.retrieve(
            "dpnd_abc123def456",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.dependents.with_raw_response.retrieve(
            "dpnd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = await response.parse()
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.dependents.with_streaming_response.retrieve(
            "dpnd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = await response.parse()
            assert_matches_type(DependentResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependent_id` but received ''"):
            await async_client.dependents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.dependents.update(
            dependent_id="dpnd_abc123def456",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.dependents.update(
            dependent_id="dpnd_abc123def456",
            active=True,
            gender="gender",
            relationship="Spouse",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.dependents.with_raw_response.update(
            dependent_id="dpnd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = await response.parse()
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.dependents.with_streaming_response.update(
            dependent_id="dpnd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = await response.parse()
            assert_matches_type(DependentResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dependent_id` but received ''"):
            await async_client.dependents.with_raw_response.update(
                dependent_id="",
            )
