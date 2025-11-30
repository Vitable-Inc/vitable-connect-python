# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_connect_api.types import Employee
from vitable_connect_api._utils import parse_date
from vitable_connect_api.types.employers import (
    EmployeeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        employee = client.employers.employees.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnectAPI) -> None:
        employee = client.employers.employees.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
                "country": "country",
                "street_2": "street_2",
            },
            employee_class="Full Time",
            gender="gender",
            phone="phone",
            suffix="suffix",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.employers.employees.with_raw_response.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.employers.employees.with_streaming_response.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.employees.with_raw_response.create(
                employer_id="",
                date_of_birth=parse_date("2019-12-27"),
                email="dev@stainless.com",
                first_name="x",
                last_name="x",
                sex="Male",
                ssn="xxxxxxxxx",
                start_date=parse_date("2019-12-27"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        employee = client.employers.employees.list(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnectAPI) -> None:
        employee = client.employers.employees.list(
            employer_id="empr_abc123def456",
            active_in=True,
            employee_class="Full Time",
            limit=20,
            page=1,
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.employers.employees.with_raw_response.list(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.employers.employees.with_streaming_response.list(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeListResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.employees.with_raw_response.list(
                employer_id="",
            )


class TestAsyncEmployees:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employers.employees.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employers.employees.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
                "country": "country",
                "street_2": "street_2",
            },
            employee_class="Full Time",
            gender="gender",
            phone="phone",
            suffix="suffix",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.employees.with_raw_response.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(Employee, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.employees.with_streaming_response.create(
            employer_id="empr_abc123def456",
            date_of_birth=parse_date("2019-12-27"),
            email="dev@stainless.com",
            first_name="x",
            last_name="x",
            sex="Male",
            ssn="xxxxxxxxx",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(Employee, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.employees.with_raw_response.create(
                employer_id="",
                date_of_birth=parse_date("2019-12-27"),
                email="dev@stainless.com",
                first_name="x",
                last_name="x",
                sex="Male",
                ssn="xxxxxxxxx",
                start_date=parse_date("2019-12-27"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employers.employees.list(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employee = await async_client.employers.employees.list(
            employer_id="empr_abc123def456",
            active_in=True,
            employee_class="Full Time",
            limit=20,
            page=1,
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.employees.with_raw_response.list(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.employees.with_streaming_response.list(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeListResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.employees.with_raw_response.list(
                employer_id="",
            )
