# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import Dependent
from vitable_partner_api._utils import parse_date
from vitable_partner_api.types.employees import DependentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDependents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        dependent = client.employees.dependents.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
        )
        assert_matches_type(Dependent, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnectAPI) -> None:
        dependent = client.employees.dependents.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
            gender="MALE",
            sex="MALE",
            suffix="suffix",
        )
        assert_matches_type(Dependent, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.employees.dependents.with_raw_response.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = response.parse()
        assert_matches_type(Dependent, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.employees.dependents.with_streaming_response.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = response.parse()
            assert_matches_type(Dependent, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.dependents.with_raw_response.create(
                id="",
                date_of_birth=parse_date("2019-12-27"),
                first_name="first_name",
                last_name="last_name",
                relationship="SPOUSE",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        dependent = client.employees.dependents.list(
            "empl__1k--w2KifJ1",
        )
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.employees.dependents.with_raw_response.list(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = response.parse()
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.employees.dependents.with_streaming_response.list(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = response.parse()
            assert_matches_type(DependentListResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.dependents.with_raw_response.list(
                "",
            )


class TestAsyncDependents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        dependent = await async_client.employees.dependents.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
        )
        assert_matches_type(Dependent, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        dependent = await async_client.employees.dependents.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
            gender="MALE",
            sex="MALE",
            suffix="suffix",
        )
        assert_matches_type(Dependent, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.dependents.with_raw_response.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = await response.parse()
        assert_matches_type(Dependent, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.dependents.with_streaming_response.create(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            last_name="last_name",
            relationship="SPOUSE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = await response.parse()
            assert_matches_type(Dependent, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.dependents.with_raw_response.create(
                id="",
                date_of_birth=parse_date("2019-12-27"),
                first_name="first_name",
                last_name="last_name",
                relationship="SPOUSE",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        dependent = await async_client.employees.dependents.list(
            "empl__1k--w2KifJ1",
        )
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.dependents.with_raw_response.list(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dependent = await response.parse()
        assert_matches_type(DependentListResponse, dependent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.dependents.with_streaming_response.list(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dependent = await response.parse()
            assert_matches_type(DependentListResponse, dependent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.dependents.with_raw_response.list(
                "",
            )
