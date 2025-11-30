# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_connect_api.types import (
    Employer,
    EmployerListResponse,
    BenefitEligibilityPolicy,
)
from vitable_connect_api._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
                "country": "country",
                "street_2": "street_2",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnectAPI) -> None:
        employer = client.employers.retrieve(
            "empr_abc123def456",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.retrieve(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.retrieve(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnectAPI) -> None:
        employer = client.employers.update(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.update(
            employer_id="empr_abc123def456",
            active=True,
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
                "country": "country",
                "street_2": "street_2",
            },
            legal_name="x",
            name="x",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.update(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.update(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.update(
                employer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        employer = client.employers.list()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.list(
            active_in=True,
            limit=20,
            name="Acme",
            page=1,
        )
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EmployerListResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_eligibility_policy_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
            policy_to_replace_id="epol_abc123def456",
            description="description",
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            client.employers.with_raw_response.create_eligibility_policy(
                employer_id="",
                effective_date=parse_date("2019-12-27"),
                name="x",
                rules=[
                    {
                        "operator": "operator",
                        "rule_type": "rule_type",
                        "value": "value",
                    }
                ],
            )


class TestAsyncEmployers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
                "country": "country",
                "street_2": "street_2",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.create(
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
            },
            ein="xxxxxxxxx",
            legal_name="x",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.retrieve(
            "empr_abc123def456",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.retrieve(
            "empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.retrieve(
            "empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.update(
            employer_id="empr_abc123def456",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.update(
            employer_id="empr_abc123def456",
            active=True,
            address={
                "city": "city",
                "state": "xx",
                "street_1": "street_1",
                "zip_code": "zip_code",
                "country": "country",
                "street_2": "street_2",
            },
            legal_name="x",
            name="x",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.update(
            employer_id="empr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.update(
            employer_id="empr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.update(
                employer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.list()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.list(
            active_in=True,
            limit=20,
            name="Acme",
            page=1,
        )
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EmployerListResponse, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EmployerListResponse, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_eligibility_policy_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
            policy_to_replace_id="epol_abc123def456",
            description="description",
        )
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.create_eligibility_policy(
            employer_id="empr_abc123def456",
            effective_date=parse_date("2019-12-27"),
            name="x",
            rules=[
                {
                    "operator": "operator",
                    "rule_type": "rule_type",
                    "value": "value",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(BenefitEligibilityPolicy, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employer_id` but received ''"):
            await async_client.employers.with_raw_response.create_eligibility_policy(
                employer_id="",
                effective_date=parse_date("2019-12-27"),
                name="x",
                rules=[
                    {
                        "operator": "operator",
                        "rule_type": "rule_type",
                        "value": "value",
                    }
                ],
            )
