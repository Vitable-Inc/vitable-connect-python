# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import (
    EmployerResponse,
    EmployerListResponse,
    BenefitEligibilityPolicy,
)
from vitable_connect._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnect) -> None:
        employer = client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
                "address_line_2": "Floor 5",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        employer = client.employers.retrieve(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.retrieve(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.retrieve(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnect) -> None:
        employer = client.employers.update(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.update(
            employer_id="empr_abc123def456",
            active=True,
            address={
                "address_line_1": "456 New Address Ave",
                "city": "San Francisco",
                "state": "CA",
                "zipcode": "94103",
                "address_line_2": "Suite 200",
            },
            legal_name="x",
            name="Acme Corp (Updated)",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.update(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.update(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.update(
                employer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        employer = client.employers.list()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.list(
            active_in=True,
            limit=20,
            name="Acme",
            page=1,
        )
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerListResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_eligibility_policy(self, client: VitableConnect) -> None:
        employer = client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_eligibility_policy_with_all_params(self, client: VitableConnect) -> None:
        employer = client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
            policy_to_replace_id="epol_abc123def456",
            description="Eligibility policy for full-time employees working 30+ hours per week",
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_eligibility_policy(self, client: VitableConnect) -> None:
        response = client.employers.with_raw_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_eligibility_policy(self, client: VitableConnect) -> None:
        with client.employers.with_streaming_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_eligibility_policy(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.create_eligibility_policy(
                employer_id="",
                effective_date=parse_date("2025-01-01"),
                name="Standard Full-Time Eligibility",
                rules=[
                    {
                        "operator": "in",
                        "rule_type": "employment_status",
                        "value": "full_time,part_time_30_plus",
                    },
                    {
                        "operator": "greater_than_or_equal",
                        "rule_type": "waiting_period_days",
                        "value": "30",
                    },
                ],
            )


class TestAsyncEmployers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
                "address_line_2": "Floor 5",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.create(
            address={
                "address_line_1": "789 Business Blvd",
                "city": "Seattle",
                "state": "WA",
                "zipcode": "98101",
            },
            ein="12-3456789",
            email="hr@newco.com",
            legal_name="NewCo Industries LLC",
            name="NewCo Industries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.retrieve(
            "empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.retrieve(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.retrieve(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.update(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.update(
            employer_id="empr_abc123def456",
            active=True,
            address={
                "address_line_1": "456 New Address Ave",
                "city": "San Francisco",
                "state": "CA",
                "zipcode": "94103",
                "address_line_2": "Suite 200",
            },
            legal_name="x",
            name="Acme Corp (Updated)",
        )
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.update(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.update(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.update(
                employer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.list(
            active_in=True,
            limit=20,
            name="Acme",
            page=1,
        )
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerListResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_eligibility_policy(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_eligibility_policy_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        employer = await async_client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
            policy_to_replace_id="epol_abc123def456",
            description="Eligibility policy for full-time employees working 30+ hours per week",
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_eligibility_policy(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employers.with_raw_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_eligibility_policy(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employers.with_streaming_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2025-01-01"),
            name="Standard Full-Time Eligibility",
            rules=[
                {
                    "operator": "in",
                    "rule_type": "employment_status",
                    "value": "full_time,part_time_30_plus",
                },
                {
                    "operator": "greater_than_or_equal",
                    "rule_type": "waiting_period_days",
                    "value": "30",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_eligibility_policy(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.create_eligibility_policy(
                employer_id="",
                effective_date=parse_date("2025-01-01"),
                name="Standard Full-Time Eligibility",
                rules=[
                    {
                        "operator": "in",
                        "rule_type": "employment_status",
                        "value": "full_time,part_time_30_plus",
                    },
                    {
                        "operator": "greater_than_or_equal",
                        "rule_type": "waiting_period_days",
                        "value": "30",
                    },
                ],
            )
