# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import auth_login_params, auth_sign_up_params, auth_complete_profile_params, auth_issue_access_token_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.auth_login_response import AuthLoginResponse
from ..types.auth_sign_up_response import AuthSignUpResponse
from ..types.auth_retrieve_me_response import AuthRetrieveMeResponse
from ..types.auth_list_personas_response import AuthListPersonasResponse
from ..types.auth_complete_profile_response import AuthCompleteProfileResponse
from ..types.auth_issue_access_token_response import AuthIssueAccessTokenResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def complete_profile(
        self,
        *,
        first_name: str,
        last_name: str,
        phone: str,
        user_type: Literal[
            "Member",
            "NursePractitioner",
            "CompanyAdmin",
            "VitableAdmin",
            "ClinicalAdmin",
            "PartnerEmployee",
            "OrganizationUser",
            "ExternalAdmin",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthCompleteProfileResponse:
        """
        Collects the required profile fields (first_name, last_name, phone) for a
        verified IdP identity and provisions the asclepius user: creates the BaseUser
        (of the app-context's user_type, with the real phone) + the OrganizationUser
        persona (name). An optional `user_type` narrows provisioning/resolution to a
        single persona type. When a same-email account already exists (verified email)
        it links + finishes that account instead. Returns the auth session. Domain
        failures surface as the normalized error envelope with an `app_error_code`: 403
        `email_verification_required` / `user_type_not_allowed`; 409 `identity_conflict`
        / `needs_selection` (fetch candidates via `/personas`); 422 `invalid_phone`.

        Args:
          user_type: - `Member` - Member
              - `NursePractitioner` - Provider
              - `CompanyAdmin` - Company Admin
              - `VitableAdmin` - Vitable Admin
              - `ClinicalAdmin` - Clinical Admin
              - `PartnerEmployee` - Partner Employee
              - `OrganizationUser` - Organization User
              - `ExternalAdmin` - External Admin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/complete-profile",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "user_type": user_type,
                },
                auth_complete_profile_params.AuthCompleteProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthCompleteProfileResponse,
        )

    def issue_access_token(
        self,
        *,
        grant_type: Literal["client_credentials"],
        bound_entity: Optional[auth_issue_access_token_params.BoundEntity] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthIssueAccessTokenResponse:
        """Issues a short-lived access token from the authenticated API key.

        Access tokens
        can optionally be bound to a specific employer or employee for scoped access.
        Tokens expire after 15 minutes.

        Args:
          grant_type: - `client_credentials` - client_credentials

          bound_entity: Optional entity to bind the token to for scoped access

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/access-tokens",
            body=maybe_transform(
                {
                    "grant_type": grant_type,
                    "bound_entity": bound_entity,
                },
                auth_issue_access_token_params.AuthIssueAccessTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthIssueAccessTokenResponse,
        )

    def list_personas(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthListPersonasResponse:
        """
        Returns the personas linked to the bearer's IdP identity that the current
        application is allowed to serve — the candidate set for a 'continue as'
        selection when sign-up returns `needs_selection`. Single-type apps usually get 0
        or 1 entry.
        """
        return self._get(
            "/v1/auth/personas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthListPersonasResponse,
        )

    def login(
        self,
        *,
        email_or_phone: str,
        user_type: Literal[
            "Member",
            "NursePractitioner",
            "CompanyAdmin",
            "VitableAdmin",
            "ClinicalAdmin",
            "PartnerEmployee",
            "OrganizationUser",
            "ExternalAdmin",
        ],
        app_name: str | Omit = omit,
        app_version: str | Omit = omit,
        password: str | Omit = omit,
        two_factor_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthLoginResponse:
        """One body-driven sign-in endpoint.

        Supply `email_or_phone` + `password` for the
        standard flow, or `email_or_phone` (no password) for the passwordless OTP flow.
        When the account has MFA enabled — or on the first passwordless step — an OTP
        challenge is issued and the response is a 200
        `{"pending_2fa": true, "destination_hint": "…"}`; resubmit the same credentials
        plus `two_factor_token` to complete sign-in and receive a session with a freshly
        minted access/refresh token pair. Domain failures surface as the normalized
        error envelope with an `app_error_code`: 401 `invalid_credentials`; 403
        `user_type_not_allowed` or `auth_user_disabled`; 409 `no_organization`; 429
        `otp_cooldown`.

        Args:
          user_type: - `Member` - Member
              - `NursePractitioner` - Provider
              - `CompanyAdmin` - Company Admin
              - `VitableAdmin` - Vitable Admin
              - `ClinicalAdmin` - Clinical Admin
              - `PartnerEmployee` - Partner Employee
              - `OrganizationUser` - Organization User
              - `ExternalAdmin` - External Admin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/login",
            body=maybe_transform(
                {
                    "email_or_phone": email_or_phone,
                    "user_type": user_type,
                    "app_name": app_name,
                    "app_version": app_version,
                    "password": password,
                    "two_factor_token": two_factor_token,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLoginResponse,
        )

    def retrieve_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthRetrieveMeResponse:
        """
        Returns the authenticated caller's IdP identity (email, name, provider).
        Identity-only — no persona (persona selection is `/v1/auth/personas`);
        organization membership and companies are fetched via dedicated endpoints.
        """
        return self._get(
            "/v1/auth/me",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthRetrieveMeResponse,
        )

    def sign_up(
        self,
        *,
        user_type: Optional[
            Literal[
                "Member",
                "NursePractitioner",
                "CompanyAdmin",
                "VitableAdmin",
                "ClinicalAdmin",
                "PartnerEmployee",
                "OrganizationUser",
                "ExternalAdmin",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSignUpResponse:
        """Validates the IdP bearer and resolves the session.

        An optional `user_type` body
        field pins resolution to a single persona (strict login). Domain failures
        surface as the normalized error envelope with an `app_error_code`: 409
        `profile_required` (no BaseUser yet) / `no_organization` / `needs_selection`
        (fetch candidates via `/personas`) / `identity_conflict`; 403
        `email_verification_required` / `user_type_not_allowed`; 404
        `persona_not_found`.

        Args:
          user_type: - `Member` - Member
              - `NursePractitioner` - NursePractitioner
              - `CompanyAdmin` - CompanyAdmin
              - `VitableAdmin` - VitableAdmin
              - `ClinicalAdmin` - ClinicalAdmin
              - `PartnerEmployee` - PartnerEmployee
              - `OrganizationUser` - OrganizationUser
              - `ExternalAdmin` - ExternalAdmin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/sign-up",
            body=maybe_transform({"user_type": user_type}, auth_sign_up_params.AuthSignUpParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthSignUpResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Vitable-Inc/vitable-connect-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def complete_profile(
        self,
        *,
        first_name: str,
        last_name: str,
        phone: str,
        user_type: Literal[
            "Member",
            "NursePractitioner",
            "CompanyAdmin",
            "VitableAdmin",
            "ClinicalAdmin",
            "PartnerEmployee",
            "OrganizationUser",
            "ExternalAdmin",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthCompleteProfileResponse:
        """
        Collects the required profile fields (first_name, last_name, phone) for a
        verified IdP identity and provisions the asclepius user: creates the BaseUser
        (of the app-context's user_type, with the real phone) + the OrganizationUser
        persona (name). An optional `user_type` narrows provisioning/resolution to a
        single persona type. When a same-email account already exists (verified email)
        it links + finishes that account instead. Returns the auth session. Domain
        failures surface as the normalized error envelope with an `app_error_code`: 403
        `email_verification_required` / `user_type_not_allowed`; 409 `identity_conflict`
        / `needs_selection` (fetch candidates via `/personas`); 422 `invalid_phone`.

        Args:
          user_type: - `Member` - Member
              - `NursePractitioner` - Provider
              - `CompanyAdmin` - Company Admin
              - `VitableAdmin` - Vitable Admin
              - `ClinicalAdmin` - Clinical Admin
              - `PartnerEmployee` - Partner Employee
              - `OrganizationUser` - Organization User
              - `ExternalAdmin` - External Admin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/complete-profile",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone": phone,
                    "user_type": user_type,
                },
                auth_complete_profile_params.AuthCompleteProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthCompleteProfileResponse,
        )

    async def issue_access_token(
        self,
        *,
        grant_type: Literal["client_credentials"],
        bound_entity: Optional[auth_issue_access_token_params.BoundEntity] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthIssueAccessTokenResponse:
        """Issues a short-lived access token from the authenticated API key.

        Access tokens
        can optionally be bound to a specific employer or employee for scoped access.
        Tokens expire after 15 minutes.

        Args:
          grant_type: - `client_credentials` - client_credentials

          bound_entity: Optional entity to bind the token to for scoped access

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/access-tokens",
            body=await async_maybe_transform(
                {
                    "grant_type": grant_type,
                    "bound_entity": bound_entity,
                },
                auth_issue_access_token_params.AuthIssueAccessTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthIssueAccessTokenResponse,
        )

    async def list_personas(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthListPersonasResponse:
        """
        Returns the personas linked to the bearer's IdP identity that the current
        application is allowed to serve — the candidate set for a 'continue as'
        selection when sign-up returns `needs_selection`. Single-type apps usually get 0
        or 1 entry.
        """
        return await self._get(
            "/v1/auth/personas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthListPersonasResponse,
        )

    async def login(
        self,
        *,
        email_or_phone: str,
        user_type: Literal[
            "Member",
            "NursePractitioner",
            "CompanyAdmin",
            "VitableAdmin",
            "ClinicalAdmin",
            "PartnerEmployee",
            "OrganizationUser",
            "ExternalAdmin",
        ],
        app_name: str | Omit = omit,
        app_version: str | Omit = omit,
        password: str | Omit = omit,
        two_factor_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthLoginResponse:
        """One body-driven sign-in endpoint.

        Supply `email_or_phone` + `password` for the
        standard flow, or `email_or_phone` (no password) for the passwordless OTP flow.
        When the account has MFA enabled — or on the first passwordless step — an OTP
        challenge is issued and the response is a 200
        `{"pending_2fa": true, "destination_hint": "…"}`; resubmit the same credentials
        plus `two_factor_token` to complete sign-in and receive a session with a freshly
        minted access/refresh token pair. Domain failures surface as the normalized
        error envelope with an `app_error_code`: 401 `invalid_credentials`; 403
        `user_type_not_allowed` or `auth_user_disabled`; 409 `no_organization`; 429
        `otp_cooldown`.

        Args:
          user_type: - `Member` - Member
              - `NursePractitioner` - Provider
              - `CompanyAdmin` - Company Admin
              - `VitableAdmin` - Vitable Admin
              - `ClinicalAdmin` - Clinical Admin
              - `PartnerEmployee` - Partner Employee
              - `OrganizationUser` - Organization User
              - `ExternalAdmin` - External Admin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/login",
            body=await async_maybe_transform(
                {
                    "email_or_phone": email_or_phone,
                    "user_type": user_type,
                    "app_name": app_name,
                    "app_version": app_version,
                    "password": password,
                    "two_factor_token": two_factor_token,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLoginResponse,
        )

    async def retrieve_me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthRetrieveMeResponse:
        """
        Returns the authenticated caller's IdP identity (email, name, provider).
        Identity-only — no persona (persona selection is `/v1/auth/personas`);
        organization membership and companies are fetched via dedicated endpoints.
        """
        return await self._get(
            "/v1/auth/me",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthRetrieveMeResponse,
        )

    async def sign_up(
        self,
        *,
        user_type: Optional[
            Literal[
                "Member",
                "NursePractitioner",
                "CompanyAdmin",
                "VitableAdmin",
                "ClinicalAdmin",
                "PartnerEmployee",
                "OrganizationUser",
                "ExternalAdmin",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSignUpResponse:
        """Validates the IdP bearer and resolves the session.

        An optional `user_type` body
        field pins resolution to a single persona (strict login). Domain failures
        surface as the normalized error envelope with an `app_error_code`: 409
        `profile_required` (no BaseUser yet) / `no_organization` / `needs_selection`
        (fetch candidates via `/personas`) / `identity_conflict`; 403
        `email_verification_required` / `user_type_not_allowed`; 404
        `persona_not_found`.

        Args:
          user_type: - `Member` - Member
              - `NursePractitioner` - NursePractitioner
              - `CompanyAdmin` - CompanyAdmin
              - `VitableAdmin` - VitableAdmin
              - `ClinicalAdmin` - ClinicalAdmin
              - `PartnerEmployee` - PartnerEmployee
              - `OrganizationUser` - OrganizationUser
              - `ExternalAdmin` - ExternalAdmin

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/sign-up",
            body=await async_maybe_transform({"user_type": user_type}, auth_sign_up_params.AuthSignUpParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=AuthSignUpResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.complete_profile = to_raw_response_wrapper(
            auth.complete_profile,
        )
        self.issue_access_token = to_raw_response_wrapper(
            auth.issue_access_token,
        )
        self.list_personas = to_raw_response_wrapper(
            auth.list_personas,
        )
        self.login = to_raw_response_wrapper(
            auth.login,
        )
        self.retrieve_me = to_raw_response_wrapper(
            auth.retrieve_me,
        )
        self.sign_up = to_raw_response_wrapper(
            auth.sign_up,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.complete_profile = async_to_raw_response_wrapper(
            auth.complete_profile,
        )
        self.issue_access_token = async_to_raw_response_wrapper(
            auth.issue_access_token,
        )
        self.list_personas = async_to_raw_response_wrapper(
            auth.list_personas,
        )
        self.login = async_to_raw_response_wrapper(
            auth.login,
        )
        self.retrieve_me = async_to_raw_response_wrapper(
            auth.retrieve_me,
        )
        self.sign_up = async_to_raw_response_wrapper(
            auth.sign_up,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.complete_profile = to_streamed_response_wrapper(
            auth.complete_profile,
        )
        self.issue_access_token = to_streamed_response_wrapper(
            auth.issue_access_token,
        )
        self.list_personas = to_streamed_response_wrapper(
            auth.list_personas,
        )
        self.login = to_streamed_response_wrapper(
            auth.login,
        )
        self.retrieve_me = to_streamed_response_wrapper(
            auth.retrieve_me,
        )
        self.sign_up = to_streamed_response_wrapper(
            auth.sign_up,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.complete_profile = async_to_streamed_response_wrapper(
            auth.complete_profile,
        )
        self.issue_access_token = async_to_streamed_response_wrapper(
            auth.issue_access_token,
        )
        self.list_personas = async_to_streamed_response_wrapper(
            auth.list_personas,
        )
        self.login = async_to_streamed_response_wrapper(
            auth.login,
        )
        self.retrieve_me = async_to_streamed_response_wrapper(
            auth.retrieve_me,
        )
        self.sign_up = async_to_streamed_response_wrapper(
            auth.sign_up,
        )
