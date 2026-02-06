# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_connect_api._utils import parse_date
from vitable_connect_api.types.benefit_products import (
    PlanYearListResponse,
    PlanYearCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlanYears:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        plan_year = client.benefit_products.plan_years.create(
            benefit_product_id="bprd_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 20000,
                    "employer_contribution_cents": 45000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 50000,
                    "employer_contribution_cents": 60000,
                    "employment": "full_time",
                },
            ],
            coverage_end=parse_date("2026-12-31"),
            coverage_start=parse_date("2026-01-01"),
            employer_id="empr_abc123",
            open_enrollment_end=parse_date("2025-11-30"),
            open_enrollment_start=parse_date("2025-10-15"),
        )
        assert_matches_type(PlanYearCreateResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.benefit_products.plan_years.with_raw_response.create(
            benefit_product_id="bprd_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 20000,
                    "employer_contribution_cents": 45000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 50000,
                    "employer_contribution_cents": 60000,
                    "employment": "full_time",
                },
            ],
            coverage_end=parse_date("2026-12-31"),
            coverage_start=parse_date("2026-01-01"),
            employer_id="empr_abc123",
            open_enrollment_end=parse_date("2025-11-30"),
            open_enrollment_start=parse_date("2025-10-15"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = response.parse()
        assert_matches_type(PlanYearCreateResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.benefit_products.plan_years.with_streaming_response.create(
            benefit_product_id="bprd_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 20000,
                    "employer_contribution_cents": 45000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 50000,
                    "employer_contribution_cents": 60000,
                    "employment": "full_time",
                },
            ],
            coverage_end=parse_date("2026-12-31"),
            coverage_start=parse_date("2026-01-01"),
            employer_id="empr_abc123",
            open_enrollment_end=parse_date("2025-11-30"),
            open_enrollment_start=parse_date("2025-10-15"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = response.parse()
            assert_matches_type(PlanYearCreateResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_product_id` but received ''"):
            client.benefit_products.plan_years.with_raw_response.create(
                benefit_product_id="",
                contribution_classes=[
                    {
                        "coverage_tier": "EE",
                        "employee_contribution_cents": 20000,
                        "employer_contribution_cents": 45000,
                        "employment": "full_time",
                    },
                    {
                        "coverage_tier": "EF",
                        "employee_contribution_cents": 50000,
                        "employer_contribution_cents": 60000,
                        "employment": "full_time",
                    },
                ],
                coverage_end=parse_date("2026-12-31"),
                coverage_start=parse_date("2026-01-01"),
                employer_id="empr_abc123",
                open_enrollment_end=parse_date("2025-11-30"),
                open_enrollment_start=parse_date("2025-10-15"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        plan_year = client.benefit_products.plan_years.list(
            benefit_product_id="bprd_abc123def456",
        )
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnectAPI) -> None:
        plan_year = client.benefit_products.plan_years.list(
            benefit_product_id="bprd_abc123def456",
            employer_id="empr_abc123def456",
            limit=20,
            page=1,
            status="draft",
        )
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.benefit_products.plan_years.with_raw_response.list(
            benefit_product_id="bprd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = response.parse()
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.benefit_products.plan_years.with_streaming_response.list(
            benefit_product_id="bprd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = response.parse()
            assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_product_id` but received ''"):
            client.benefit_products.plan_years.with_raw_response.list(
                benefit_product_id="",
            )


class TestAsyncPlanYears:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        plan_year = await async_client.benefit_products.plan_years.create(
            benefit_product_id="bprd_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 20000,
                    "employer_contribution_cents": 45000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 50000,
                    "employer_contribution_cents": 60000,
                    "employment": "full_time",
                },
            ],
            coverage_end=parse_date("2026-12-31"),
            coverage_start=parse_date("2026-01-01"),
            employer_id="empr_abc123",
            open_enrollment_end=parse_date("2025-11-30"),
            open_enrollment_start=parse_date("2025-10-15"),
        )
        assert_matches_type(PlanYearCreateResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.benefit_products.plan_years.with_raw_response.create(
            benefit_product_id="bprd_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 20000,
                    "employer_contribution_cents": 45000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 50000,
                    "employer_contribution_cents": 60000,
                    "employment": "full_time",
                },
            ],
            coverage_end=parse_date("2026-12-31"),
            coverage_start=parse_date("2026-01-01"),
            employer_id="empr_abc123",
            open_enrollment_end=parse_date("2025-11-30"),
            open_enrollment_start=parse_date("2025-10-15"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = await response.parse()
        assert_matches_type(PlanYearCreateResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.benefit_products.plan_years.with_streaming_response.create(
            benefit_product_id="bprd_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 20000,
                    "employer_contribution_cents": 45000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 50000,
                    "employer_contribution_cents": 60000,
                    "employment": "full_time",
                },
            ],
            coverage_end=parse_date("2026-12-31"),
            coverage_start=parse_date("2026-01-01"),
            employer_id="empr_abc123",
            open_enrollment_end=parse_date("2025-11-30"),
            open_enrollment_start=parse_date("2025-10-15"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = await response.parse()
            assert_matches_type(PlanYearCreateResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_product_id` but received ''"):
            await async_client.benefit_products.plan_years.with_raw_response.create(
                benefit_product_id="",
                contribution_classes=[
                    {
                        "coverage_tier": "EE",
                        "employee_contribution_cents": 20000,
                        "employer_contribution_cents": 45000,
                        "employment": "full_time",
                    },
                    {
                        "coverage_tier": "EF",
                        "employee_contribution_cents": 50000,
                        "employer_contribution_cents": 60000,
                        "employment": "full_time",
                    },
                ],
                coverage_end=parse_date("2026-12-31"),
                coverage_start=parse_date("2026-01-01"),
                employer_id="empr_abc123",
                open_enrollment_end=parse_date("2025-11-30"),
                open_enrollment_start=parse_date("2025-10-15"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        plan_year = await async_client.benefit_products.plan_years.list(
            benefit_product_id="bprd_abc123def456",
        )
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        plan_year = await async_client.benefit_products.plan_years.list(
            benefit_product_id="bprd_abc123def456",
            employer_id="empr_abc123def456",
            limit=20,
            page=1,
            status="draft",
        )
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.benefit_products.plan_years.with_raw_response.list(
            benefit_product_id="bprd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = await response.parse()
        assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.benefit_products.plan_years.with_streaming_response.list(
            benefit_product_id="bprd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = await response.parse()
            assert_matches_type(PlanYearListResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `benefit_product_id` but received ''"):
            await async_client.benefit_products.plan_years.with_raw_response.list(
                benefit_product_id="",
            )
