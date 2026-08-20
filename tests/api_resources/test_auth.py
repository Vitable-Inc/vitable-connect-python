# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vitable_connect import VitableConnect, AsyncVitableConnect
from vitable_connect.types import (
    AuthLoginResponse,
    AuthSignUpResponse,
    AuthRetrieveMeResponse,
    AuthListPersonasResponse,
    AuthCompleteProfileResponse,
    AuthIssueAccessTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_profile(self, client: VitableConnect) -> None:
        auth = client.auth.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
        )
        assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_profile_with_all_params(self, client: VitableConnect) -> None:
        auth = client.auth.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
            user_type="Member",
        )
        assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_profile(self, client: VitableConnect) -> None:
        response = client.auth.with_raw_response.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_profile(self, client: VitableConnect) -> None:
        with client.auth.with_streaming_response.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_issue_access_token(self, client: VitableConnect) -> None:
        auth = client.auth.issue_access_token(
            grant_type="client_credentials",
        )
        assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_issue_access_token_with_all_params(self, client: VitableConnect) -> None:
        auth = client.auth.issue_access_token(
            grant_type="client_credentials",
            bound_entity={
                "id": "id",
                "type": "employer",
            },
        )
        assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_issue_access_token(self, client: VitableConnect) -> None:
        response = client.auth.with_raw_response.issue_access_token(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_issue_access_token(self, client: VitableConnect) -> None:
        with client.auth.with_streaming_response.issue_access_token(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_personas(self, client: VitableConnect) -> None:
        auth = client.auth.list_personas()
        assert_matches_type(AuthListPersonasResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_personas(self, client: VitableConnect) -> None:
        response = client.auth.with_raw_response.list_personas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthListPersonasResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_personas(self, client: VitableConnect) -> None:
        with client.auth.with_streaming_response.list_personas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthListPersonasResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_login(self, client: VitableConnect) -> None:
        auth = client.auth.login(
            email_or_phone="email_or_phone",
            user_type="Member",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_login_with_all_params(self, client: VitableConnect) -> None:
        auth = client.auth.login(
            email_or_phone="email_or_phone",
            user_type="Member",
            app_name="app_name",
            app_version="app_version",
            password="password",
            two_factor_token="two_factor_token",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_login(self, client: VitableConnect) -> None:
        response = client.auth.with_raw_response.login(
            email_or_phone="email_or_phone",
            user_type="Member",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_login(self, client: VitableConnect) -> None:
        with client.auth.with_streaming_response.login(
            email_or_phone="email_or_phone",
            user_type="Member",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_me(self, client: VitableConnect) -> None:
        auth = client.auth.retrieve_me()
        assert_matches_type(AuthRetrieveMeResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_me(self, client: VitableConnect) -> None:
        response = client.auth.with_raw_response.retrieve_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRetrieveMeResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_me(self, client: VitableConnect) -> None:
        with client.auth.with_streaming_response.retrieve_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRetrieveMeResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sign_up(self, client: VitableConnect) -> None:
        auth = client.auth.sign_up()
        assert_matches_type(AuthSignUpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sign_up_with_all_params(self, client: VitableConnect) -> None:
        auth = client.auth.sign_up(
            user_type="Member",
        )
        assert_matches_type(AuthSignUpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sign_up(self, client: VitableConnect) -> None:
        response = client.auth.with_raw_response.sign_up()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSignUpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sign_up(self, client: VitableConnect) -> None:
        with client.auth.with_streaming_response.sign_up() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSignUpResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_profile(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
        )
        assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_profile_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
            user_type="Member",
        )
        assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_profile(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.auth.with_raw_response.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_profile(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.auth.with_streaming_response.complete_profile(
            first_name="first_name",
            last_name="last_name",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthCompleteProfileResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_issue_access_token(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.issue_access_token(
            grant_type="client_credentials",
        )
        assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_issue_access_token_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.issue_access_token(
            grant_type="client_credentials",
            bound_entity={
                "id": "id",
                "type": "employer",
            },
        )
        assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_issue_access_token(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.auth.with_raw_response.issue_access_token(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_issue_access_token(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.auth.with_streaming_response.issue_access_token(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthIssueAccessTokenResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_personas(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.list_personas()
        assert_matches_type(AuthListPersonasResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_personas(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.auth.with_raw_response.list_personas()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthListPersonasResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_personas(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.auth.with_streaming_response.list_personas() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthListPersonasResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_login(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.login(
            email_or_phone="email_or_phone",
            user_type="Member",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.login(
            email_or_phone="email_or_phone",
            user_type="Member",
            app_name="app_name",
            app_version="app_version",
            password="password",
            two_factor_token="two_factor_token",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_login(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.auth.with_raw_response.login(
            email_or_phone="email_or_phone",
            user_type="Member",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.auth.with_streaming_response.login(
            email_or_phone="email_or_phone",
            user_type="Member",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_me(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.retrieve_me()
        assert_matches_type(AuthRetrieveMeResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_me(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.auth.with_raw_response.retrieve_me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRetrieveMeResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_me(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.auth.with_streaming_response.retrieve_me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRetrieveMeResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sign_up(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.sign_up()
        assert_matches_type(AuthSignUpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sign_up_with_all_params(self, async_client: AsyncVitableConnect) -> None:
        auth = await async_client.auth.sign_up(
            user_type="Member",
        )
        assert_matches_type(AuthSignUpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sign_up(self, async_client: AsyncVitableConnect) -> None:
        response = await async_client.auth.with_raw_response.sign_up()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSignUpResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sign_up(self, async_client: AsyncVitableConnect) -> None:
        async with async_client.auth.with_streaming_response.sign_up() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSignUpResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
