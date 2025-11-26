# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types.employees import (
    EnrollmentListResponse,
    EnrollmentElectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrollments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        enrollment = client.employees.enrollments.list(
            id="empl__1k--w2KifJ1",
        )
        assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnectAPI) -> None:
        enrollment = client.employees.enrollments.list(
            id="empl__1k--w2KifJ1",
            status="pending",
        )
        assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.employees.enrollments.with_raw_response.list(
            id="empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.employees.enrollments.with_streaming_response.list(
            id="empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.enrollments.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_elect(self, client: VitableConnectAPI) -> None:
        enrollment = client.employees.enrollments.elect(
            id="empl__1k--w2KifJ1",
            elections=[
                {
                    "decision": "enrolled",
                    "enrollment_id": "enrl__1k--w2KifJ1",
                }
            ],
        )
        assert_matches_type(EnrollmentElectResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_elect(self, client: VitableConnectAPI) -> None:
        response = client.employees.enrollments.with_raw_response.elect(
            id="empl__1k--w2KifJ1",
            elections=[
                {
                    "decision": "enrolled",
                    "enrollment_id": "enrl__1k--w2KifJ1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentElectResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_elect(self, client: VitableConnectAPI) -> None:
        with client.employees.enrollments.with_streaming_response.elect(
            id="empl__1k--w2KifJ1",
            elections=[
                {
                    "decision": "enrolled",
                    "enrollment_id": "enrl__1k--w2KifJ1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentElectResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_elect(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.enrollments.with_raw_response.elect(
                id="",
                elections=[
                    {
                        "decision": "enrolled",
                        "enrollment_id": "enrl__1k--w2KifJ1",
                    }
                ],
            )


class TestAsyncEnrollments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        enrollment = await async_client.employees.enrollments.list(
            id="empl__1k--w2KifJ1",
        )
        assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        enrollment = await async_client.employees.enrollments.list(
            id="empl__1k--w2KifJ1",
            status="pending",
        )
        assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.enrollments.with_raw_response.list(
            id="empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.enrollments.with_streaming_response.list(
            id="empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentListResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.enrollments.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_elect(self, async_client: AsyncVitableConnectAPI) -> None:
        enrollment = await async_client.employees.enrollments.elect(
            id="empl__1k--w2KifJ1",
            elections=[
                {
                    "decision": "enrolled",
                    "enrollment_id": "enrl__1k--w2KifJ1",
                }
            ],
        )
        assert_matches_type(EnrollmentElectResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_elect(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.enrollments.with_raw_response.elect(
            id="empl__1k--w2KifJ1",
            elections=[
                {
                    "decision": "enrolled",
                    "enrollment_id": "enrl__1k--w2KifJ1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentElectResponse, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_elect(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.enrollments.with_streaming_response.elect(
            id="empl__1k--w2KifJ1",
            elections=[
                {
                    "decision": "enrolled",
                    "enrollment_id": "enrl__1k--w2KifJ1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentElectResponse, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_elect(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.enrollments.with_raw_response.elect(
                id="",
                elections=[
                    {
                        "decision": "enrolled",
                        "enrollment_id": "enrl__1k--w2KifJ1",
                    }
                ],
            )
