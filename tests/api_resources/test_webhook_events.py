# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import (
    WebhookEvent,
    WebhookEventRetrieveResponse,
    WebhookEventListDeliveriesResponse,
)
from vitable_connect._utils import parse_datetime
from vitable_connect.pagination import SyncPageNumberPage, AsyncPageNumberPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        webhook_event = client.webhook_events.retrieve(
            "event_id",
        )
        assert_matches_type(WebhookEventRetrieveResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.webhook_events.with_raw_response.retrieve(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = response.parse()
        assert_matches_type(WebhookEventRetrieveResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.webhook_events.with_streaming_response.retrieve(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = response.parse()
            assert_matches_type(WebhookEventRetrieveResponse, webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.webhook_events.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnect) -> None:
        webhook_event = client.webhook_events.list()
        assert_matches_type(SyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: VitableConnect) -> None:
        webhook_event = client.webhook_events.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_name="enrollment.accepted",
            limit=20,
            page=1,
            resource_id="x",
            resource_type="enrollment",
        )
        assert_matches_type(SyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnect) -> None:
        response = client.webhook_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = response.parse()
        assert_matches_type(SyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnect) -> None:
        with client.webhook_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = response.parse()
            assert_matches_type(SyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_deliveries(self, client: VitableConnect) -> None:
        webhook_event = client.webhook_events.list_deliveries(
            "event_id",
        )
        assert_matches_type(WebhookEventListDeliveriesResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_deliveries(self, client: VitableConnect) -> None:
        response = client.webhook_events.with_raw_response.list_deliveries(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = response.parse()
        assert_matches_type(WebhookEventListDeliveriesResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_deliveries(self, client: VitableConnect) -> None:
        with client.webhook_events.with_streaming_response.list_deliveries(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = response.parse()
            assert_matches_type(WebhookEventListDeliveriesResponse, webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_deliveries(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.webhook_events.with_raw_response.list_deliveries(
                "",
            )


class TestAsyncWebhookEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        webhook_event = await async_client.webhook_events.retrieve(
            "event_id",
        )
        assert_matches_type(WebhookEventRetrieveResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.webhook_events.with_raw_response.retrieve(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = await response.parse()
        assert_matches_type(WebhookEventRetrieveResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.webhook_events.with_streaming_response.retrieve(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = await response.parse()
            assert_matches_type(WebhookEventRetrieveResponse, webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.webhook_events.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnect) -> None:
        webhook_event = await async_client.webhook_events.list()
        assert_matches_type(AsyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        webhook_event = await async_client.webhook_events.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            event_name="enrollment.accepted",
            limit=20,
            page=1,
            resource_id="x",
            resource_type="enrollment",
        )
        assert_matches_type(AsyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.webhook_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = await response.parse()
        assert_matches_type(AsyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.webhook_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = await response.parse()
            assert_matches_type(AsyncPageNumberPage[WebhookEvent], webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_deliveries(self, async_client: AsyncVitableConnect) -> None:
        webhook_event = await async_client.webhook_events.list_deliveries(
            "event_id",
        )
        assert_matches_type(WebhookEventListDeliveriesResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_deliveries(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.webhook_events.with_raw_response.list_deliveries(
            "event_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_event = await response.parse()
        assert_matches_type(WebhookEventListDeliveriesResponse, webhook_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_deliveries(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.webhook_events.with_streaming_response.list_deliveries(
            "event_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_event = await response.parse()
            assert_matches_type(WebhookEventListDeliveriesResponse, webhook_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_deliveries(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.webhook_events.with_raw_response.list_deliveries(
                "",
            )
