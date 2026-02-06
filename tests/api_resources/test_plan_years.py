# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect._utils import parse_date
from vitable_connect.types.benefit_products import PlanYearResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlanYears:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        plan_year = client.plan_years.retrieve(
            "plyr_abc123def456",
        )
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.plan_years.with_raw_response.retrieve(
            "plyr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = response.parse()
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.plan_years.with_streaming_response.retrieve(
            "plyr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = response.parse()
            assert_matches_type(PlanYearResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_year_id` but received ''"):
            client.plan_years.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnect) -> None:
        plan_year = client.plan_years.update(
            plan_year_id="plyr_abc123def456",
        )
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnect) -> None:
        plan_year = client.plan_years.update(
            plan_year_id="plyr_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 18000,
                    "employer_contribution_cents": 47000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 48000,
                    "employer_contribution_cents": 62000,
                    "employment": "full_time",
                },
            ],
            open_enrollment_end=parse_date("2024-11-15"),
            open_enrollment_start=parse_date("2024-10-01"),
            status="active",
        )
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnect) -> None:
        response = client.plan_years.with_raw_response.update(
            plan_year_id="plyr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = response.parse()
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnect) -> None:
        with client.plan_years.with_streaming_response.update(
            plan_year_id="plyr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = response.parse()
            assert_matches_type(PlanYearResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_year_id` but received ''"):
            client.plan_years.with_raw_response.update(
                plan_year_id="",
            )


class TestAsyncPlanYears:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        plan_year = await async_client.plan_years.retrieve(
            "plyr_abc123def456",
        )
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.plan_years.with_raw_response.retrieve(
            "plyr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = await response.parse()
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.plan_years.with_streaming_response.retrieve(
            "plyr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = await response.parse()
            assert_matches_type(PlanYearResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_year_id` but received ''"):
            await async_client.plan_years.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnect) -> None:
        plan_year = await async_client.plan_years.update(
            plan_year_id="plyr_abc123def456",
        )
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        plan_year = await async_client.plan_years.update(
            plan_year_id="plyr_abc123def456",
            contribution_classes=[
                {
                    "coverage_tier": "EE",
                    "employee_contribution_cents": 18000,
                    "employer_contribution_cents": 47000,
                    "employment": "full_time",
                },
                {
                    "coverage_tier": "EF",
                    "employee_contribution_cents": 48000,
                    "employer_contribution_cents": 62000,
                    "employment": "full_time",
                },
            ],
            open_enrollment_end=parse_date("2024-11-15"),
            open_enrollment_start=parse_date("2024-10-01"),
            status="active",
        )
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.plan_years.with_raw_response.update(
            plan_year_id="plyr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_year = await response.parse()
        assert_matches_type(PlanYearResponse, plan_year, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.plan_years.with_streaming_response.update(
            plan_year_id="plyr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_year = await response.parse()
            assert_matches_type(PlanYearResponse, plan_year, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_year_id` but received ''"):
            await async_client.plan_years.with_raw_response.update(
                plan_year_id="",
            )
