# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect._utils import parse_date
from vitable_connect.types.groups.members import SyncSubmitResponse, SyncRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: VitableConnect) -> None:
        sync = client.groups.members.sync.retrieve(
            request_id="request_id",
            group_id="grp_abc123def456",
        )
        assert_matches_type(SyncRetrieveResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: VitableConnect) -> None:
        response = client.groups.members.sync.with_raw_response.retrieve(
            request_id="request_id",
            group_id="grp_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncRetrieveResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: VitableConnect) -> None:
        with client.groups.members.sync.with_streaming_response.retrieve(
            request_id="request_id",
            group_id="grp_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncRetrieveResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.members.sync.with_raw_response.retrieve(
                request_id="request_id",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.groups.members.sync.with_raw_response.retrieve(
                request_id="",
                group_id="grp_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: VitableConnect) -> None:
        sync = client.groups.members.sync.submit(
            group_id="grp_abc123def456",
            members=[
                {
                    "address": {
                        "address_line_1": "x",
                        "city": "x",
                        "state": "xx",
                        "zipcode": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone": "phone",
                    "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "reference_id": "x",
                }
            ],
        )
        assert_matches_type(SyncSubmitResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: VitableConnect) -> None:
        response = client.groups.members.sync.with_raw_response.submit(
            group_id="grp_abc123def456",
            members=[
                {
                    "address": {
                        "address_line_1": "x",
                        "city": "x",
                        "state": "xx",
                        "zipcode": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone": "phone",
                    "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "reference_id": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncSubmitResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: VitableConnect) -> None:
        with client.groups.members.sync.with_streaming_response.submit(
            group_id="grp_abc123def456",
            members=[
                {
                    "address": {
                        "address_line_1": "x",
                        "city": "x",
                        "state": "xx",
                        "zipcode": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone": "phone",
                    "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "reference_id": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncSubmitResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: VitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.groups.members.sync.with_raw_response.submit(
                group_id="",
                members=[
                    {
                        "address": {
                            "address_line_1": "x",
                            "city": "x",
                            "state": "xx",
                            "zipcode": "x",
                        },
                        "date_of_birth": parse_date("2019-12-27"),
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "phone": "phone",
                        "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "reference_id": "x",
                    }
                ],
            )


class TestAsyncSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVitableConnect) -> None:
        sync = await async_client.groups.members.sync.retrieve(
            request_id="request_id",
            group_id="grp_abc123def456",
        )
        assert_matches_type(SyncRetrieveResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.groups.members.sync.with_raw_response.retrieve(
            request_id="request_id",
            group_id="grp_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncRetrieveResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.groups.members.sync.with_streaming_response.retrieve(
            request_id="request_id",
            group_id="grp_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncRetrieveResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.members.sync.with_raw_response.retrieve(
                request_id="request_id",
                group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.groups.members.sync.with_raw_response.retrieve(
                request_id="",
                group_id="grp_abc123def456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncVitableConnect) -> None:
        sync = await async_client.groups.members.sync.submit(
            group_id="grp_abc123def456",
            members=[
                {
                    "address": {
                        "address_line_1": "x",
                        "city": "x",
                        "state": "xx",
                        "zipcode": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone": "phone",
                    "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "reference_id": "x",
                }
            ],
        )
        assert_matches_type(SyncSubmitResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.groups.members.sync.with_raw_response.submit(
            group_id="grp_abc123def456",
            members=[
                {
                    "address": {
                        "address_line_1": "x",
                        "city": "x",
                        "state": "xx",
                        "zipcode": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone": "phone",
                    "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "reference_id": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncSubmitResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.groups.members.sync.with_streaming_response.submit(
            group_id="grp_abc123def456",
            members=[
                {
                    "address": {
                        "address_line_1": "x",
                        "city": "x",
                        "state": "xx",
                        "zipcode": "x",
                    },
                    "date_of_birth": parse_date("2019-12-27"),
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone": "phone",
                    "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "reference_id": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncSubmitResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncVitableConnect) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.groups.members.sync.with_raw_response.submit(
                group_id="",
                members=[
                    {
                        "address": {
                            "address_line_1": "x",
                            "city": "x",
                            "state": "xx",
                            "zipcode": "x",
                        },
                        "date_of_birth": parse_date("2019-12-27"),
                        "first_name": "first_name",
                        "last_name": "last_name",
                        "phone": "phone",
                        "plan_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "reference_id": "x",
                    }
                ],
            )
