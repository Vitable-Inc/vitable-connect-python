# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import EnrollmentResponse, EnrollmentListPlansResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrollments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        enrollment = client.enrollments.retrieve(
            "enrl_abc123def456",
        )
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.enrollments.with_raw_response.retrieve(
            "enrl_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.enrollments.with_streaming_response.retrieve(
            "enrl_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enrollment_id` but received ''"):
            client.enrollments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_plans(self, client: VitableConnect) -> None:
        enrollment = client.enrollments.list_plans(
            "enrl_abc123def456",
        )
        assert_matches_type(EnrollmentListPlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_plans(self, client: VitableConnect) -> None:
        response = client.enrollments.with_raw_response.list_plans(
            "enrl_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentListPlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_plans(self, client: VitableConnect) -> None:
        with client.enrollments.with_streaming_response.list_plans(
            "enrl_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentListPlansResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_plans(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enrollment_id` but received ''"):
            client.enrollments.with_raw_response.list_plans(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reissue(self, client: VitableConnect) -> None:
        enrollment = client.enrollments.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
        )
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reissue_with_all_params(self, client: VitableConnect) -> None:
        enrollment = client.enrollments.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
            reason="reason",
        )
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reissue(self, client: VitableConnect) -> None:
        response = client.enrollments.with_raw_response.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reissue(self, client: VitableConnect) -> None:
        with client.enrollments.with_streaming_response.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reissue(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enrollment_id` but received ''"):
            client.enrollments.with_raw_response.reissue(
                enrollment_id="",
                qle_id="qle_marriage123abc",
            )


class TestAsyncEnrollments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.enrollments.retrieve(
            "enrl_abc123def456",
        )
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.enrollments.with_raw_response.retrieve(
            "enrl_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.enrollments.with_streaming_response.retrieve(
            "enrl_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enrollment_id` but received ''"):
            await async_client.enrollments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_plans(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.enrollments.list_plans(
            "enrl_abc123def456",
        )
        assert_matches_type(EnrollmentListPlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_plans(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.enrollments.with_raw_response.list_plans(
            "enrl_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentListPlansResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_plans(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.enrollments.with_streaming_response.list_plans(
            "enrl_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentListPlansResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_plans(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enrollment_id` but received ''"):
            await async_client.enrollments.with_raw_response.list_plans(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reissue(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.enrollments.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
        )
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reissue_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.enrollments.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
            reason="reason",
        )
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reissue(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.enrollments.with_raw_response.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reissue(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.enrollments.with_streaming_response.reissue(
            enrollment_id="enrl_abc123def456",
            qle_id="qle_marriage123abc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reissue(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enrollment_id` but received ''"):
            await async_client.enrollments.with_raw_response.reissue(
                enrollment_id="",
                qle_id="qle_marriage123abc",
            )
