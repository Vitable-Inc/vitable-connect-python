# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import Enrollment, EnrollmentGetEligiblePlansResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrollments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_eligible_plans(self, client: VitableConnectAPI) -> None:
        enrollment = client.enrollments.get_eligible_plans(
            "enrl__1k--w2KifJ1",
        )
        assert_matches_type(EnrollmentGetEligiblePlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_eligible_plans(self, client: VitableConnectAPI) -> None:
        response = client.enrollments.with_raw_response.get_eligible_plans(
            "enrl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentGetEligiblePlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_eligible_plans(self, client: VitableConnectAPI) -> None:
        with client.enrollments.with_streaming_response.get_eligible_plans(
            "enrl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentGetEligiblePlansResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_eligible_plans(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.enrollments.with_raw_response.get_eligible_plans(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reissue(self, client: VitableConnectAPI) -> None:
        enrollment = client.enrollments.reissue(
            id="enrl__1k--w2KifJ1",
            qualifying_life_event_id="qle__1k--w2KifJ1",
        )
        assert_matches_type(Enrollment, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reissue(self, client: VitableConnectAPI) -> None:
        response = client.enrollments.with_raw_response.reissue(
            id="enrl__1k--w2KifJ1",
            qualifying_life_event_id="qle__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(Enrollment, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reissue(self, client: VitableConnectAPI) -> None:
        with client.enrollments.with_streaming_response.reissue(
            id="enrl__1k--w2KifJ1",
            qualifying_life_event_id="qle__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(Enrollment, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reissue(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.enrollments.with_raw_response.reissue(
                id="",
                qualifying_life_event_id="qle__1k--w2KifJ1",
            )


class TestAsyncEnrollments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_eligible_plans(self, async_client: AsyncVitableConnectAPI) -> None:
        enrollment = await async_client.enrollments.get_eligible_plans(
            "enrl__1k--w2KifJ1",
        )
        assert_matches_type(EnrollmentGetEligiblePlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_eligible_plans(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.enrollments.with_raw_response.get_eligible_plans(
            "enrl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentGetEligiblePlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_eligible_plans(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.enrollments.with_streaming_response.get_eligible_plans(
            "enrl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentGetEligiblePlansResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_eligible_plans(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.enrollments.with_raw_response.get_eligible_plans(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reissue(self, async_client: AsyncVitableConnectAPI) -> None:
        enrollment = await async_client.enrollments.reissue(
            id="enrl__1k--w2KifJ1",
            qualifying_life_event_id="qle__1k--w2KifJ1",
        )
        assert_matches_type(Enrollment, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reissue(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.enrollments.with_raw_response.reissue(
            id="enrl__1k--w2KifJ1",
            qualifying_life_event_id="qle__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(Enrollment, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reissue(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.enrollments.with_streaming_response.reissue(
            id="enrl__1k--w2KifJ1",
            qualifying_life_event_id="qle__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(Enrollment, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reissue(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.enrollments.with_raw_response.reissue(
                id="",
                qualifying_life_event_id="qle__1k--w2KifJ1",
            )
