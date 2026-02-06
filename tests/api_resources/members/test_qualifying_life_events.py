# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_connect_api._utils import parse_date
from vitable_connect_api.types.members import (
    QualifyingLifeEventListResponse,
    QualifyingLifeEventRecordResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQualifyingLifeEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.members.qualifying_life_events.list(
            member_id="mbr_abc123def456",
        )
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.members.qualifying_life_events.list(
            member_id="mbr_abc123def456",
            event_type="Marriage",
            limit=20,
            page=1,
            status="pending",
        )
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.members.qualifying_life_events.with_raw_response.list(
            member_id="mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = response.parse()
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.members.qualifying_life_events.with_streaming_response.list(
            member_id="mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = response.parse()
            assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.qualifying_life_events.with_raw_response.list(
                member_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.members.qualifying_life_events.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
        )
        assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_record_with_all_params(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.members.qualifying_life_events.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
            notes="Employee got married, adding spouse to coverage",
        )
        assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_record(self, client: VitableConnectAPI) -> None:
        response = client.members.qualifying_life_events.with_raw_response.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = response.parse()
        assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_record(self, client: VitableConnectAPI) -> None:
        with client.members.qualifying_life_events.with_streaming_response.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = response.parse()
            assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_record(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.qualifying_life_events.with_raw_response.record(
                member_id="",
                event_date=parse_date("2024-11-15"),
                event_type="Marriage",
            )


class TestAsyncQualifyingLifeEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.members.qualifying_life_events.list(
            member_id="mbr_abc123def456",
        )
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.members.qualifying_life_events.list(
            member_id="mbr_abc123def456",
            event_type="Marriage",
            limit=20,
            page=1,
            status="pending",
        )
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.members.qualifying_life_events.with_raw_response.list(
            member_id="mbr_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = await response.parse()
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.members.qualifying_life_events.with_streaming_response.list(
            member_id="mbr_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = await response.parse()
            assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.qualifying_life_events.with_raw_response.list(
                member_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.members.qualifying_life_events.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
        )
        assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_record_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.members.qualifying_life_events.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
            notes="Employee got married, adding spouse to coverage",
        )
        assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_record(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.members.qualifying_life_events.with_raw_response.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = await response.parse()
        assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_record(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.members.qualifying_life_events.with_streaming_response.record(
            member_id="mbr_abc123def456",
            event_date=parse_date("2024-11-15"),
            event_type="Marriage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = await response.parse()
            assert_matches_type(QualifyingLifeEventRecordResponse, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_record(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.qualifying_life_events.with_raw_response.record(
                member_id="",
                event_date=parse_date("2024-11-15"),
                event_type="Marriage",
            )
