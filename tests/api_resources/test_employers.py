# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import (
    Employer,
    EligibilityPolicy,
    EmployerListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create(
            legal_name="legal_name",
            name="name",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create(
            legal_name="legal_name",
            name="name",
            active=True,
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.create(
            legal_name="legal_name",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.create(
            legal_name="legal_name",
            name="name",
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
            "empr__1k--w2KifJ1",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.retrieve(
            "empr__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.retrieve(
            "empr__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: VitableConnectAPI) -> None:
        employer = client.employers.update(
            id="empr__1k--w2KifJ1",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.update(
            id="empr__1k--w2KifJ1",
            active=True,
            legal_name="legal_name",
            name="name",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.update(
            id="empr__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.update(
            id="empr__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employers.with_raw_response.update(
                id="",
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
            limit=1,
            offset=0,
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
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
        )
        assert_matches_type(EligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_eligibility_policy_with_all_params(self, client: VitableConnectAPI) -> None:
        employer = client.employers.create_eligibility_policy(
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
            policy_to_replace_id="policy_to_replace_id",
        )
        assert_matches_type(EligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        response = client.employers.with_raw_response.create_eligibility_policy(
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = response.parse()
        assert_matches_type(EligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        with client.employers.with_streaming_response.create_eligibility_policy(
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = response.parse()
            assert_matches_type(EligibilityPolicy, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_eligibility_policy(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employers.with_raw_response.create_eligibility_policy(
                id="",
                classification="FULL_TIME",
                waiting_period="FIRST_OF_FOLLOWING_MONTH",
            )


class TestAsyncEmployers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create(
            legal_name="legal_name",
            name="name",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create(
            legal_name="legal_name",
            name="name",
            active=True,
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.create(
            legal_name="legal_name",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.create(
            legal_name="legal_name",
            name="name",
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
            "empr__1k--w2KifJ1",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.retrieve(
            "empr__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.retrieve(
            "empr__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.update(
            id="empr__1k--w2KifJ1",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.update(
            id="empr__1k--w2KifJ1",
            active=True,
            legal_name="legal_name",
            name="name",
        )
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.update(
            id="empr__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(Employer, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.update(
            id="empr__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(Employer, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employers.with_raw_response.update(
                id="",
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
            limit=1,
            offset=0,
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
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
        )
        assert_matches_type(EligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_eligibility_policy_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        employer = await async_client.employers.create_eligibility_policy(
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
            policy_to_replace_id="policy_to_replace_id",
        )
        assert_matches_type(EligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employers.with_raw_response.create_eligibility_policy(
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employer = await response.parse()
        assert_matches_type(EligibilityPolicy, employer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employers.with_streaming_response.create_eligibility_policy(
            id="empr__1k--w2KifJ1",
            classification="FULL_TIME",
            waiting_period="FIRST_OF_FOLLOWING_MONTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employer = await response.parse()
            assert_matches_type(EligibilityPolicy, employer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_eligibility_policy(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employers.with_raw_response.create_eligibility_policy(
                id="",
                classification="FULL_TIME",
                waiting_period="FIRST_OF_FOLLOWING_MONTH",
            )
