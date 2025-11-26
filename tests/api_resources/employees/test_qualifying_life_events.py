# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_partner_api import VitableConnectAPI, AsyncVitableConnectAPI
from vitable_partner_api.types import QualifyingLifeEvent
from vitable_partner_api._utils import parse_date
from vitable_partner_api.types.employees import QualifyingLifeEventListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQualifyingLifeEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.employees.qualifying_life_events.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
        )
        assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.employees.qualifying_life_events.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
            description="description",
            proof_document_url="https://example.com",
        )
        assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: VitableConnectAPI) -> None:
        response = client.employees.qualifying_life_events.with_raw_response.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = response.parse()
        assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: VitableConnectAPI) -> None:
        with client.employees.qualifying_life_events.with_streaming_response.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = response.parse()
            assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.qualifying_life_events.with_raw_response.create(
                id="",
                event_date=parse_date("2019-12-27"),
                event_type="MARRIAGE",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: VitableConnectAPI) -> None:
        qualifying_life_event = client.employees.qualifying_life_events.list(
            "empl__1k--w2KifJ1",
        )
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: VitableConnectAPI) -> None:
        response = client.employees.qualifying_life_events.with_raw_response.list(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = response.parse()
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: VitableConnectAPI) -> None:
        with client.employees.qualifying_life_events.with_streaming_response.list(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = response.parse()
            assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: VitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.employees.qualifying_life_events.with_raw_response.list(
                "",
            )


class TestAsyncQualifyingLifeEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.employees.qualifying_life_events.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
        )
        assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.employees.qualifying_life_events.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
            description="description",
            proof_document_url="https://example.com",
        )
        assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.qualifying_life_events.with_raw_response.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = await response.parse()
        assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.qualifying_life_events.with_streaming_response.create(
            id="empl__1k--w2KifJ1",
            event_date=parse_date("2019-12-27"),
            event_type="MARRIAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = await response.parse()
            assert_matches_type(QualifyingLifeEvent, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.qualifying_life_events.with_raw_response.create(
                id="",
                event_date=parse_date("2019-12-27"),
                event_type="MARRIAGE",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncVitableConnectAPI) -> None:
        qualifying_life_event = await async_client.employees.qualifying_life_events.list(
            "empl__1k--w2KifJ1",
        )
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        response = await async_client.employees.qualifying_life_events.with_raw_response.list(
            "empl__1k--w2KifJ1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualifying_life_event = await response.parse()
        assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVitableConnectAPI) -> None:
        async with async_client.employees.qualifying_life_events.with_streaming_response.list(
            "empl__1k--w2KifJ1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualifying_life_event = await response.parse()
            assert_matches_type(QualifyingLifeEventListResponse, qualifying_life_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncVitableConnectAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.employees.qualifying_life_events.with_raw_response.list(
                "",
            )
