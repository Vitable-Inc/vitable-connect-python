# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import DependentResponse
from vitable_connect._utils import parse_date
from vitable_connect.types.members import (
    DependentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDependents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnect) -> None:
        dependent = client.members.dependents.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnect) -> None:
        dependent = client.members.dependents.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
            gender="gender",
            ssn="123-45-6789",
            suffix="suffix",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnect) -> None:
        response = client.members.dependents.with_raw_response.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = response.parse()
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnect) -> None:
        with client.members.dependents.with_streaming_response.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = response.parse()
            assert_matches_type(DependentResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.dependents.with_raw_response.create(
                member_id="",
                date_of_birth=parse_date("2020-05-15"),
                first_name="Emily",
                last_name="Doe",
                relationship="Child",
                sex="Female",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        dependent = client.members.dependents.list(
            member_id="mbr_abc123def456",
        )
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        dependent = client.members.dependents.list(
            member_id="mbr_abc123def456",
            active_in=True,
            limit=20,
            page=1,
            relationship="Spouse",
        )
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.members.dependents.with_raw_response.list(
            member_id="mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = response.parse()
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.members.dependents.with_streaming_response.list(
            member_id="mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = response.parse()
            assert_matches_type(DependentListResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.dependents.with_raw_response.list(
                member_id="",
            )


class TestAsyncDependents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.members.dependents.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.members.dependents.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
            gender="gender",
            ssn="123-45-6789",
            suffix="suffix",
        )
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.dependents.with_raw_response.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = await response.parse()
        assert_matches_type(DependentResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.dependents.with_streaming_response.create(
            member_id="mbr_abc123def456",
            date_of_birth=parse_date("2020-05-15"),
            first_name="Emily",
            last_name="Doe",
            relationship="Child",
            sex="Female",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = await response.parse()
            assert_matches_type(DependentResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.dependents.with_raw_response.create(
                member_id="",
                date_of_birth=parse_date("2020-05-15"),
                first_name="Emily",
                last_name="Doe",
                relationship="Child",
                sex="Female",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.members.dependents.list(
            member_id="mbr_abc123def456",
        )
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        dependent = await async_client.members.dependents.list(
            member_id="mbr_abc123def456",
            active_in=True,
            limit=20,
            page=1,
            relationship="Spouse",
        )
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.members.dependents.with_raw_response.list(
            member_id="mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = await response.parse()
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.members.dependents.with_streaming_response.list(
            member_id="mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = await response.parse()
            assert_matches_type(DependentListResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.dependents.with_raw_response.list(
                member_id="",
            )
