# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import Employee
from vitable_partner_api._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnectAPI) -> None:
        employee = client.employees.retrieve(
            "empl__1k--w2KifJ1",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnectAPI) -> None:
        response = client.employees.with_raw_response.retrieve(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnectAPI) -> None:
        with client.employees.with_streaming_response.retrieve(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnectAPI) -> None:
        employee = client.employees.update(
            id="empl__1k--w2KifJ1",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnectAPI) -> None:
        employee = client.employees.update(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            gender="MALE",
            last_name="last_name",
            sex="MALE",
            start_date=parse_date("2019-12-27"),
            suffix="suffix",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnectAPI) -> None:
        response = client.employees.with_raw_response.update(
            id="empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnectAPI) -> None:
        with client.employees.with_streaming_response.update(
            id="empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_terminate(self, client: VitableConnectAPI) -> None:
        employee = client.employees.terminate(
            "empl__1k--w2KifJ1",
        )
        assert employee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: VitableConnectAPI) -> None:
        response = client.employees.with_raw_response.terminate(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert employee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: VitableConnectAPI) -> None:
        with client.employees.with_streaming_response.terminate(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert employee is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.with_raw_response.terminate(
                "",
            )


class TestAsyncEmployees:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employees.retrieve(
            "empl__1k--w2KifJ1",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.with_raw_response.retrieve(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.with_streaming_response.retrieve(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employees.update(
            id="empl__1k--w2KifJ1",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employees.update(
            id="empl__1k--w2KifJ1",
            date_of_birth=parse_date("2019-12-27"),
            first_name="first_name",
            gender="MALE",
            last_name="last_name",
            sex="MALE",
            start_date=parse_date("2019-12-27"),
            suffix="suffix",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.with_raw_response.update(
            id="empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.with_streaming_response.update(
            id="empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employees.terminate(
            "empl__1k--w2KifJ1",
        )
        assert employee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.with_raw_response.terminate(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert employee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.with_streaming_response.terminate(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert employee is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.with_raw_response.terminate(
                "",
            )
