# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types.employees import (
    EnrollmentList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnrollments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        enrollment = client.employees.enrollments.list(
            employee_id="empl_abc123def456",
        )
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        enrollment = client.employees.enrollments.list(
            employee_id="empl_abc123def456",
            coverage_effective_start_year=2025,
            limit=20,
            page=1,
            plan_year=2025,
            status="pending",
        )
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.employees.enrollments.with_raw_response.list(
            employee_id="empl_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.employees.enrollments.with_streaming_response.list(
            employee_id="empl_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentList, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_id` but received ''"):
            client.employees.enrollments.with_raw_response.list(
                employee_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_elections(self, client: VitableConnect) -> None:
        enrollment = client.employees.enrollments.submit_elections(
            employee_id="empl_abc123def456",
            elections=[
                {
                    "coverage_tier": "EF",
                    "decision": "Enrolled",
                    "enrollment_id": "enrl_pending123abc",
                },
                {
                    "coverage_tier": "Unspecified",
                    "decision": "Waived",
                    "enrollment_id": "enrl_pending456def",
                },
            ],
        )
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_elections(self, client: VitableConnect) -> None:
        response = client.employees.enrollments.with_raw_response.submit_elections(
            employee_id="empl_abc123def456",
            elections=[
                {
                    "coverage_tier": "EF",
                    "decision": "Enrolled",
                    "enrollment_id": "enrl_pending123abc",
                },
                {
                    "coverage_tier": "Unspecified",
                    "decision": "Waived",
                    "enrollment_id": "enrl_pending456def",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = response.parse()
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_elections(self, client: VitableConnect) -> None:
        with client.employees.enrollments.with_streaming_response.submit_elections(
            employee_id="empl_abc123def456",
            elections=[
                {
                    "coverage_tier": "EF",
                    "decision": "Enrolled",
                    "enrollment_id": "enrl_pending123abc",
                },
                {
                    "coverage_tier": "Unspecified",
                    "decision": "Waived",
                    "enrollment_id": "enrl_pending456def",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = response.parse()
            assert_matches_type(EnrollmentList, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_elections(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_id` but received ''"):
            client.employees.enrollments.with_raw_response.submit_elections(
                employee_id="",
                elections=[
                    {
                        "coverage_tier": "EF",
                        "decision": "Enrolled",
                        "enrollment_id": "enrl_pending123abc",
                    },
                    {
                        "coverage_tier": "Unspecified",
                        "decision": "Waived",
                        "enrollment_id": "enrl_pending456def",
                    },
                ],
            )


class TestAsyncEnrollments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.employees.enrollments.list(
            employee_id="empl_abc123def456",
        )
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.employees.enrollments.list(
            employee_id="empl_abc123def456",
            coverage_effective_start_year=2025,
            limit=20,
            page=1,
            plan_year=2025,
            status="pending",
        )
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employees.enrollments.with_raw_response.list(
            employee_id="empl_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employees.enrollments.with_streaming_response.list(
            employee_id="empl_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentList, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_id` but received ''"):
            await async_client.employees.enrollments.with_raw_response.list(
                employee_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_elections(self, async_client: AsyncVitableConnect) -> None:
        enrollment = await async_client.employees.enrollments.submit_elections(
            employee_id="empl_abc123def456",
            elections=[
                {
                    "coverage_tier": "EF",
                    "decision": "Enrolled",
                    "enrollment_id": "enrl_pending123abc",
                },
                {
                    "coverage_tier": "Unspecified",
                    "decision": "Waived",
                    "enrollment_id": "enrl_pending456def",
                },
            ],
        )
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_elections(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.employees.enrollments.with_raw_response.submit_elections(
            employee_id="empl_abc123def456",
            elections=[
                {
                    "coverage_tier": "EF",
                    "decision": "Enrolled",
                    "enrollment_id": "enrl_pending123abc",
                },
                {
                    "coverage_tier": "Unspecified",
                    "decision": "Waived",
                    "enrollment_id": "enrl_pending456def",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enrollment = await response.parse()
        assert_matches_type(EnrollmentList, enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_elections(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.employees.enrollments.with_streaming_response.submit_elections(
            employee_id="empl_abc123def456",
            elections=[
                {
                    "coverage_tier": "EF",
                    "decision": "Enrolled",
                    "enrollment_id": "enrl_pending123abc",
                },
                {
                    "coverage_tier": "Unspecified",
                    "decision": "Waived",
                    "enrollment_id": "enrl_pending456def",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enrollment = await response.parse()
            assert_matches_type(EnrollmentList, enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_elections(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `employee_id` but received ''"):
            await async_client.employees.enrollments.with_raw_response.submit_elections(
                employee_id="",
                elections=[
                    {
                        "coverage_tier": "EF",
                        "decision": "Enrolled",
                        "enrollment_id": "enrl_pending123abc",
                    },
                    {
                        "coverage_tier": "Unspecified",
                        "decision": "Waived",
                        "enrollment_id": "enrl_pending456def",
                    },
                ],
            )
