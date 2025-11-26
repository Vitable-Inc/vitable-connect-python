# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import PlanYear
from vitable_partner_api._utils import parse_date
from vitable_partner_api.types.benefit_products import (
    PlanYearListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlanYears:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        plan_year = client.benefit_products.plan_years.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PlanYear, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnectAPI) -> None:
        plan_year = client.benefit_products.plan_years.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
            contribution_classes=[
                {
                    "compensation": "UNSPECIFIED",
                    "employer_contribution_in_cents": 0,
                    "employment": "UNSPECIFIED",
                    "family_status": "UNSPECIFIED",
                    "location": "UNSPECIFIED",
                    "location_value": "location_value",
                    "max_age": 0,
                    "min_age": 0,
                    "plan_id": "plan_id",
                }
            ],
            plan_costs=[
                {
                    "dependent_cost_in_cents": 0,
                    "employee_cost_in_cents": 0,
                    "plan_id": "plan_id",
                }
            ],
        )
        assert_matches_type(PlanYear, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.benefit_products.plan_years.with_raw_response.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = response.parse()
        assert_matches_type(PlanYear, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.benefit_products.plan_years.with_streaming_response.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = response.parse()
            assert_matches_type(PlanYear, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.benefit_products.plan_years.with_raw_response.create(
                id="",
                coverage_end_date=parse_date("2019-12-27"),
                coverage_start_date=parse_date("2019-12-27"),
                employer_id="empr__1k--w2KifJ1",
                open_enrollment_end_date=parse_date("2019-12-27"),
                open_enrollment_start_date=parse_date("2019-12-27"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        plan_year = client.benefit_products.plan_years.list(
            id="bprd__1k--w2KifJ1",
            employer_id="employer_id",
        )
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.benefit_products.plan_years.with_raw_response.list(
            id="bprd__1k--w2KifJ1",
            employer_id="employer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = response.parse()
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.benefit_products.plan_years.with_streaming_response.list(
            id="bprd__1k--w2KifJ1",
            employer_id="employer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = response.parse()
            assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.benefit_products.plan_years.with_raw_response.list(
                id="",
                employer_id="employer_id",
            )


class TestAsyncPlanYears:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        plan_year = await async_client.benefit_products.plan_years.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(PlanYear, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        plan_year = await async_client.benefit_products.plan_years.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
            contribution_classes=[
                {
                    "compensation": "UNSPECIFIED",
                    "employer_contribution_in_cents": 0,
                    "employment": "UNSPECIFIED",
                    "family_status": "UNSPECIFIED",
                    "location": "UNSPECIFIED",
                    "location_value": "location_value",
                    "max_age": 0,
                    "min_age": 0,
                    "plan_id": "plan_id",
                }
            ],
            plan_costs=[
                {
                    "dependent_cost_in_cents": 0,
                    "employee_cost_in_cents": 0,
                    "plan_id": "plan_id",
                }
            ],
        )
        assert_matches_type(PlanYear, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.benefit_products.plan_years.with_raw_response.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = await response.parse()
        assert_matches_type(PlanYear, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.benefit_products.plan_years.with_streaming_response.create(
            id="bprd__1k--w2KifJ1",
            coverage_end_date=parse_date("2019-12-27"),
            coverage_start_date=parse_date("2019-12-27"),
            employer_id="empr__1k--w2KifJ1",
            open_enrollment_end_date=parse_date("2019-12-27"),
            open_enrollment_start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = await response.parse()
            assert_matches_type(PlanYear, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.benefit_products.plan_years.with_raw_response.create(
                id="",
                coverage_end_date=parse_date("2019-12-27"),
                coverage_start_date=parse_date("2019-12-27"),
                employer_id="empr__1k--w2KifJ1",
                open_enrollment_end_date=parse_date("2019-12-27"),
                open_enrollment_start_date=parse_date("2019-12-27"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        plan_year = await async_client.benefit_products.plan_years.list(
            id="bprd__1k--w2KifJ1",
            employer_id="employer_id",
        )
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.benefit_products.plan_years.with_raw_response.list(
            id="bprd__1k--w2KifJ1",
            employer_id="employer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = await response.parse()
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.benefit_products.plan_years.with_streaming_response.list(
            id="bprd__1k--w2KifJ1",
            employer_id="employer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = await response.parse()
            assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.benefit_products.plan_years.with_raw_response.list(
                id="",
                employer_id="employer_id",
            )
