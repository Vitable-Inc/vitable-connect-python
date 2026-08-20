# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import auth_issue_access_token_params
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
from ..types.auth_issue_access_token_response import AuthIssueAccessTokenResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    """Issue short-lived access tokens for scoped API access"""

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


class AsyncAuthResource(AsyncAPIResource):
    """Issue short-lived access tokens for scoped API access"""

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


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.issue_access_token = to_raw_response_wrapper(
            auth.issue_access_token,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.issue_access_token = async_to_raw_response_wrapper(
            auth.issue_access_token,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.issue_access_token = to_streamed_response_wrapper(
            auth.issue_access_token,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.issue_access_token = async_to_streamed_response_wrapper(
            auth.issue_access_token,
        )
