# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import dependents, plan_years, enrollments, qualifying_life_events, benefit_eligibility_policy
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, VitableConnectAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.members import members
from .resources.employees import employees
from .resources.employers import employers
from .resources.benefit_products import benefit_products

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "VitableConnectAPI",
    "AsyncVitableConnectAPI",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.vitablehealth.com",
    "environment_1": "https://api.uat.vitablehealth.com",
}


class VitableConnectAPI(SyncAPIClient):
    benefit_eligibility_policy: benefit_eligibility_policy.BenefitEligibilityPolicyResource
    benefit_products: benefit_products.BenefitProductsResource
    dependents: dependents.DependentsResource
    employees: employees.EmployeesResource
    employers: employers.EmployersResource
    enrollments: enrollments.EnrollmentsResource
    members: members.MembersResource
    plan_years: plan_years.PlanYearsResource
    qualifying_life_events: qualifying_life_events.QualifyingLifeEventsResource
    with_raw_response: VitableConnectAPIWithRawResponse
    with_streaming_response: VitableConnectAPIWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous VitableConnectAPI client instance.

        This automatically infers the `api_key` argument from the `VITABLE_connect_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("VITABLE_connect_API_API_KEY")
        if api_key is None:
            raise VitableConnectAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the VITABLE_connect_API_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("VITABLE_CONNECT_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `VITABLE_CONNECT_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.benefit_eligibility_policy = benefit_eligibility_policy.BenefitEligibilityPolicyResource(self)
        self.benefit_products = benefit_products.BenefitProductsResource(self)
        self.dependents = dependents.DependentsResource(self)
        self.employees = employees.EmployeesResource(self)
        self.employers = employers.EmployersResource(self)
        self.enrollments = enrollments.EnrollmentsResource(self)
        self.members = members.MembersResource(self)
        self.plan_years = plan_years.PlanYearsResource(self)
        self.qualifying_life_events = qualifying_life_events.QualifyingLifeEventsResource(self)
        self.with_raw_response = VitableConnectAPIWithRawResponse(self)
        self.with_streaming_response = VitableConnectAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncVitableConnectAPI(AsyncAPIClient):
    benefit_eligibility_policy: benefit_eligibility_policy.AsyncBenefitEligibilityPolicyResource
    benefit_products: benefit_products.AsyncBenefitProductsResource
    dependents: dependents.AsyncDependentsResource
    employees: employees.AsyncEmployeesResource
    employers: employers.AsyncEmployersResource
    enrollments: enrollments.AsyncEnrollmentsResource
    members: members.AsyncMembersResource
    plan_years: plan_years.AsyncPlanYearsResource
    qualifying_life_events: qualifying_life_events.AsyncQualifyingLifeEventsResource
    with_raw_response: AsyncVitableConnectAPIWithRawResponse
    with_streaming_response: AsyncVitableConnectAPIWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncVitableConnectAPI client instance.

        This automatically infers the `api_key` argument from the `VITABLE_connect_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("VITABLE_connect_API_API_KEY")
        if api_key is None:
            raise VitableConnectAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the VITABLE_connect_API_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("VITABLE_CONNECT_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `VITABLE_CONNECT_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.benefit_eligibility_policy = benefit_eligibility_policy.AsyncBenefitEligibilityPolicyResource(self)
        self.benefit_products = benefit_products.AsyncBenefitProductsResource(self)
        self.dependents = dependents.AsyncDependentsResource(self)
        self.employees = employees.AsyncEmployeesResource(self)
        self.employers = employers.AsyncEmployersResource(self)
        self.enrollments = enrollments.AsyncEnrollmentsResource(self)
        self.members = members.AsyncMembersResource(self)
        self.plan_years = plan_years.AsyncPlanYearsResource(self)
        self.qualifying_life_events = qualifying_life_events.AsyncQualifyingLifeEventsResource(self)
        self.with_raw_response = AsyncVitableConnectAPIWithRawResponse(self)
        self.with_streaming_response = AsyncVitableConnectAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class VitableConnectAPIWithRawResponse:
    def __init__(self, client: VitableConnectAPI) -> None:
        self.benefit_eligibility_policy = benefit_eligibility_policy.BenefitEligibilityPolicyResourceWithRawResponse(
            client.benefit_eligibility_policy
        )
        self.benefit_products = benefit_products.BenefitProductsResourceWithRawResponse(client.benefit_products)
        self.dependents = dependents.DependentsResourceWithRawResponse(client.dependents)
        self.employees = employees.EmployeesResourceWithRawResponse(client.employees)
        self.employers = employers.EmployersResourceWithRawResponse(client.employers)
        self.enrollments = enrollments.EnrollmentsResourceWithRawResponse(client.enrollments)
        self.members = members.MembersResourceWithRawResponse(client.members)
        self.plan_years = plan_years.PlanYearsResourceWithRawResponse(client.plan_years)
        self.qualifying_life_events = qualifying_life_events.QualifyingLifeEventsResourceWithRawResponse(
            client.qualifying_life_events
        )


class AsyncVitableConnectAPIWithRawResponse:
    def __init__(self, client: AsyncVitableConnectAPI) -> None:
        self.benefit_eligibility_policy = (
            benefit_eligibility_policy.AsyncBenefitEligibilityPolicyResourceWithRawResponse(
                client.benefit_eligibility_policy
            )
        )
        self.benefit_products = benefit_products.AsyncBenefitProductsResourceWithRawResponse(client.benefit_products)
        self.dependents = dependents.AsyncDependentsResourceWithRawResponse(client.dependents)
        self.employees = employees.AsyncEmployeesResourceWithRawResponse(client.employees)
        self.employers = employers.AsyncEmployersResourceWithRawResponse(client.employers)
        self.enrollments = enrollments.AsyncEnrollmentsResourceWithRawResponse(client.enrollments)
        self.members = members.AsyncMembersResourceWithRawResponse(client.members)
        self.plan_years = plan_years.AsyncPlanYearsResourceWithRawResponse(client.plan_years)
        self.qualifying_life_events = qualifying_life_events.AsyncQualifyingLifeEventsResourceWithRawResponse(
            client.qualifying_life_events
        )


class VitableConnectAPIWithStreamedResponse:
    def __init__(self, client: VitableConnectAPI) -> None:
        self.benefit_eligibility_policy = (
            benefit_eligibility_policy.BenefitEligibilityPolicyResourceWithStreamingResponse(
                client.benefit_eligibility_policy
            )
        )
        self.benefit_products = benefit_products.BenefitProductsResourceWithStreamingResponse(client.benefit_products)
        self.dependents = dependents.DependentsResourceWithStreamingResponse(client.dependents)
        self.employees = employees.EmployeesResourceWithStreamingResponse(client.employees)
        self.employers = employers.EmployersResourceWithStreamingResponse(client.employers)
        self.enrollments = enrollments.EnrollmentsResourceWithStreamingResponse(client.enrollments)
        self.members = members.MembersResourceWithStreamingResponse(client.members)
        self.plan_years = plan_years.PlanYearsResourceWithStreamingResponse(client.plan_years)
        self.qualifying_life_events = qualifying_life_events.QualifyingLifeEventsResourceWithStreamingResponse(
            client.qualifying_life_events
        )


class AsyncVitableConnectAPIWithStreamedResponse:
    def __init__(self, client: AsyncVitableConnectAPI) -> None:
        self.benefit_eligibility_policy = (
            benefit_eligibility_policy.AsyncBenefitEligibilityPolicyResourceWithStreamingResponse(
                client.benefit_eligibility_policy
            )
        )
        self.benefit_products = benefit_products.AsyncBenefitProductsResourceWithStreamingResponse(
            client.benefit_products
        )
        self.dependents = dependents.AsyncDependentsResourceWithStreamingResponse(client.dependents)
        self.employees = employees.AsyncEmployeesResourceWithStreamingResponse(client.employees)
        self.employers = employers.AsyncEmployersResourceWithStreamingResponse(client.employers)
        self.enrollments = enrollments.AsyncEnrollmentsResourceWithStreamingResponse(client.enrollments)
        self.members = members.AsyncMembersResourceWithStreamingResponse(client.members)
        self.plan_years = plan_years.AsyncPlanYearsResourceWithStreamingResponse(client.plan_years)
        self.qualifying_life_events = qualifying_life_events.AsyncQualifyingLifeEventsResourceWithStreamingResponse(
            client.qualifying_life_events
        )


Client = VitableConnectAPI

AsyncClient = AsyncVitableConnectAPI
