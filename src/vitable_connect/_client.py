# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
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
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, VitableConnectError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        auth,
        members,
        employees,
        employers,
        dependents,
        plan_years,
        enrollments,
        benefit_products,
        benefit_eligibility_policies,
    )
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.dependents import DependentsResource, AsyncDependentsResource
    from .resources.plan_years import PlanYearsResource, AsyncPlanYearsResource
    from .resources.enrollments import EnrollmentsResource, AsyncEnrollmentsResource
    from .resources.members.members import MembersResource, AsyncMembersResource
    from .resources.employees.employees import EmployeesResource, AsyncEmployeesResource
    from .resources.employers.employers import EmployersResource, AsyncEmployersResource
    from .resources.benefit_eligibility_policies import (
        BenefitEligibilityPoliciesResource,
        AsyncBenefitEligibilityPoliciesResource,
    )
    from .resources.benefit_products.benefit_products import BenefitProductsResource, AsyncBenefitProductsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "VitableConnect",
    "AsyncVitableConnect",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.vitablehealth.com",
    "environment_1": "https://api.uat.vitablehealth.com",
}


class VitableConnect(SyncAPIClient):
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
        """Construct a new synchronous VitableConnect client instance.

        This automatically infers the `api_key` argument from the `VITABLE_CONNECT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("VITABLE_CONNECT_API_KEY")
        if api_key is None:
            raise VitableConnectError(
                "The api_key client option must be set either by passing api_key to the client or by setting the VITABLE_CONNECT_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("VITABLE_CONNECT_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `VITABLE_CONNECT_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
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

    @cached_property
    def auth(self) -> AuthResource:
        """Issue short-lived access tokens for scoped API access"""
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def benefit_eligibility_policies(self) -> BenefitEligibilityPoliciesResource:
        """Define rules that determine which employees qualify for benefits"""
        from .resources.benefit_eligibility_policies import BenefitEligibilityPoliciesResource

        return BenefitEligibilityPoliciesResource(self)

    @cached_property
    def benefit_products(self) -> BenefitProductsResource:
        """Browse available benefit products that can be offered to employers"""
        from .resources.benefit_products import BenefitProductsResource

        return BenefitProductsResource(self)

    @cached_property
    def dependents(self) -> DependentsResource:
        """Manage dependent records (spouses, children) for employees"""
        from .resources.dependents import DependentsResource

        return DependentsResource(self)

    @cached_property
    def employees(self) -> EmployeesResource:
        """Manage employee records for employers"""
        from .resources.employees import EmployeesResource

        return EmployeesResource(self)

    @cached_property
    def employers(self) -> EmployersResource:
        from .resources.employers import EmployersResource

        return EmployersResource(self)

    @cached_property
    def enrollments(self) -> EnrollmentsResource:
        """Manage benefit enrollments and elections for employees"""
        from .resources.enrollments import EnrollmentsResource

        return EnrollmentsResource(self)

    @cached_property
    def members(self) -> MembersResource:
        from .resources.members import MembersResource

        return MembersResource(self)

    @cached_property
    def plan_years(self) -> PlanYearsResource:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        from .resources.plan_years import PlanYearsResource

        return PlanYearsResource(self)

    @cached_property
    def with_raw_response(self) -> VitableConnectWithRawResponse:
        return VitableConnectWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VitableConnectWithStreamedResponse:
        return VitableConnectWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
        }

    @property
    def _api_key_auth(self) -> dict[str, str]:
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


class AsyncVitableConnect(AsyncAPIClient):
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
        """Construct a new async AsyncVitableConnect client instance.

        This automatically infers the `api_key` argument from the `VITABLE_CONNECT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("VITABLE_CONNECT_API_KEY")
        if api_key is None:
            raise VitableConnectError(
                "The api_key client option must be set either by passing api_key to the client or by setting the VITABLE_CONNECT_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("VITABLE_CONNECT_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `VITABLE_CONNECT_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
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

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """Issue short-lived access tokens for scoped API access"""
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def benefit_eligibility_policies(self) -> AsyncBenefitEligibilityPoliciesResource:
        """Define rules that determine which employees qualify for benefits"""
        from .resources.benefit_eligibility_policies import AsyncBenefitEligibilityPoliciesResource

        return AsyncBenefitEligibilityPoliciesResource(self)

    @cached_property
    def benefit_products(self) -> AsyncBenefitProductsResource:
        """Browse available benefit products that can be offered to employers"""
        from .resources.benefit_products import AsyncBenefitProductsResource

        return AsyncBenefitProductsResource(self)

    @cached_property
    def dependents(self) -> AsyncDependentsResource:
        """Manage dependent records (spouses, children) for employees"""
        from .resources.dependents import AsyncDependentsResource

        return AsyncDependentsResource(self)

    @cached_property
    def employees(self) -> AsyncEmployeesResource:
        """Manage employee records for employers"""
        from .resources.employees import AsyncEmployeesResource

        return AsyncEmployeesResource(self)

    @cached_property
    def employers(self) -> AsyncEmployersResource:
        from .resources.employers import AsyncEmployersResource

        return AsyncEmployersResource(self)

    @cached_property
    def enrollments(self) -> AsyncEnrollmentsResource:
        """Manage benefit enrollments and elections for employees"""
        from .resources.enrollments import AsyncEnrollmentsResource

        return AsyncEnrollmentsResource(self)

    @cached_property
    def members(self) -> AsyncMembersResource:
        from .resources.members import AsyncMembersResource

        return AsyncMembersResource(self)

    @cached_property
    def plan_years(self) -> AsyncPlanYearsResource:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        from .resources.plan_years import AsyncPlanYearsResource

        return AsyncPlanYearsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncVitableConnectWithRawResponse:
        return AsyncVitableConnectWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVitableConnectWithStreamedResponse:
        return AsyncVitableConnectWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
        }

    @property
    def _api_key_auth(self) -> dict[str, str]:
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


class VitableConnectWithRawResponse:
    _client: VitableConnect

    def __init__(self, client: VitableConnect) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        """Issue short-lived access tokens for scoped API access"""
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def benefit_eligibility_policies(
        self,
    ) -> benefit_eligibility_policies.BenefitEligibilityPoliciesResourceWithRawResponse:
        """Define rules that determine which employees qualify for benefits"""
        from .resources.benefit_eligibility_policies import BenefitEligibilityPoliciesResourceWithRawResponse

        return BenefitEligibilityPoliciesResourceWithRawResponse(self._client.benefit_eligibility_policies)

    @cached_property
    def benefit_products(self) -> benefit_products.BenefitProductsResourceWithRawResponse:
        """Browse available benefit products that can be offered to employers"""
        from .resources.benefit_products import BenefitProductsResourceWithRawResponse

        return BenefitProductsResourceWithRawResponse(self._client.benefit_products)

    @cached_property
    def dependents(self) -> dependents.DependentsResourceWithRawResponse:
        """Manage dependent records (spouses, children) for employees"""
        from .resources.dependents import DependentsResourceWithRawResponse

        return DependentsResourceWithRawResponse(self._client.dependents)

    @cached_property
    def employees(self) -> employees.EmployeesResourceWithRawResponse:
        """Manage employee records for employers"""
        from .resources.employees import EmployeesResourceWithRawResponse

        return EmployeesResourceWithRawResponse(self._client.employees)

    @cached_property
    def employers(self) -> employers.EmployersResourceWithRawResponse:
        from .resources.employers import EmployersResourceWithRawResponse

        return EmployersResourceWithRawResponse(self._client.employers)

    @cached_property
    def enrollments(self) -> enrollments.EnrollmentsResourceWithRawResponse:
        """Manage benefit enrollments and elections for employees"""
        from .resources.enrollments import EnrollmentsResourceWithRawResponse

        return EnrollmentsResourceWithRawResponse(self._client.enrollments)

    @cached_property
    def members(self) -> members.MembersResourceWithRawResponse:
        from .resources.members import MembersResourceWithRawResponse

        return MembersResourceWithRawResponse(self._client.members)

    @cached_property
    def plan_years(self) -> plan_years.PlanYearsResourceWithRawResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        from .resources.plan_years import PlanYearsResourceWithRawResponse

        return PlanYearsResourceWithRawResponse(self._client.plan_years)


class AsyncVitableConnectWithRawResponse:
    _client: AsyncVitableConnect

    def __init__(self, client: AsyncVitableConnect) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        """Issue short-lived access tokens for scoped API access"""
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def benefit_eligibility_policies(
        self,
    ) -> benefit_eligibility_policies.AsyncBenefitEligibilityPoliciesResourceWithRawResponse:
        """Define rules that determine which employees qualify for benefits"""
        from .resources.benefit_eligibility_policies import AsyncBenefitEligibilityPoliciesResourceWithRawResponse

        return AsyncBenefitEligibilityPoliciesResourceWithRawResponse(self._client.benefit_eligibility_policies)

    @cached_property
    def benefit_products(self) -> benefit_products.AsyncBenefitProductsResourceWithRawResponse:
        """Browse available benefit products that can be offered to employers"""
        from .resources.benefit_products import AsyncBenefitProductsResourceWithRawResponse

        return AsyncBenefitProductsResourceWithRawResponse(self._client.benefit_products)

    @cached_property
    def dependents(self) -> dependents.AsyncDependentsResourceWithRawResponse:
        """Manage dependent records (spouses, children) for employees"""
        from .resources.dependents import AsyncDependentsResourceWithRawResponse

        return AsyncDependentsResourceWithRawResponse(self._client.dependents)

    @cached_property
    def employees(self) -> employees.AsyncEmployeesResourceWithRawResponse:
        """Manage employee records for employers"""
        from .resources.employees import AsyncEmployeesResourceWithRawResponse

        return AsyncEmployeesResourceWithRawResponse(self._client.employees)

    @cached_property
    def employers(self) -> employers.AsyncEmployersResourceWithRawResponse:
        from .resources.employers import AsyncEmployersResourceWithRawResponse

        return AsyncEmployersResourceWithRawResponse(self._client.employers)

    @cached_property
    def enrollments(self) -> enrollments.AsyncEnrollmentsResourceWithRawResponse:
        """Manage benefit enrollments and elections for employees"""
        from .resources.enrollments import AsyncEnrollmentsResourceWithRawResponse

        return AsyncEnrollmentsResourceWithRawResponse(self._client.enrollments)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithRawResponse:
        from .resources.members import AsyncMembersResourceWithRawResponse

        return AsyncMembersResourceWithRawResponse(self._client.members)

    @cached_property
    def plan_years(self) -> plan_years.AsyncPlanYearsResourceWithRawResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        from .resources.plan_years import AsyncPlanYearsResourceWithRawResponse

        return AsyncPlanYearsResourceWithRawResponse(self._client.plan_years)


class VitableConnectWithStreamedResponse:
    _client: VitableConnect

    def __init__(self, client: VitableConnect) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        """Issue short-lived access tokens for scoped API access"""
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def benefit_eligibility_policies(
        self,
    ) -> benefit_eligibility_policies.BenefitEligibilityPoliciesResourceWithStreamingResponse:
        """Define rules that determine which employees qualify for benefits"""
        from .resources.benefit_eligibility_policies import BenefitEligibilityPoliciesResourceWithStreamingResponse

        return BenefitEligibilityPoliciesResourceWithStreamingResponse(self._client.benefit_eligibility_policies)

    @cached_property
    def benefit_products(self) -> benefit_products.BenefitProductsResourceWithStreamingResponse:
        """Browse available benefit products that can be offered to employers"""
        from .resources.benefit_products import BenefitProductsResourceWithStreamingResponse

        return BenefitProductsResourceWithStreamingResponse(self._client.benefit_products)

    @cached_property
    def dependents(self) -> dependents.DependentsResourceWithStreamingResponse:
        """Manage dependent records (spouses, children) for employees"""
        from .resources.dependents import DependentsResourceWithStreamingResponse

        return DependentsResourceWithStreamingResponse(self._client.dependents)

    @cached_property
    def employees(self) -> employees.EmployeesResourceWithStreamingResponse:
        """Manage employee records for employers"""
        from .resources.employees import EmployeesResourceWithStreamingResponse

        return EmployeesResourceWithStreamingResponse(self._client.employees)

    @cached_property
    def employers(self) -> employers.EmployersResourceWithStreamingResponse:
        from .resources.employers import EmployersResourceWithStreamingResponse

        return EmployersResourceWithStreamingResponse(self._client.employers)

    @cached_property
    def enrollments(self) -> enrollments.EnrollmentsResourceWithStreamingResponse:
        """Manage benefit enrollments and elections for employees"""
        from .resources.enrollments import EnrollmentsResourceWithStreamingResponse

        return EnrollmentsResourceWithStreamingResponse(self._client.enrollments)

    @cached_property
    def members(self) -> members.MembersResourceWithStreamingResponse:
        from .resources.members import MembersResourceWithStreamingResponse

        return MembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def plan_years(self) -> plan_years.PlanYearsResourceWithStreamingResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        from .resources.plan_years import PlanYearsResourceWithStreamingResponse

        return PlanYearsResourceWithStreamingResponse(self._client.plan_years)


class AsyncVitableConnectWithStreamedResponse:
    _client: AsyncVitableConnect

    def __init__(self, client: AsyncVitableConnect) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        """Issue short-lived access tokens for scoped API access"""
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def benefit_eligibility_policies(
        self,
    ) -> benefit_eligibility_policies.AsyncBenefitEligibilityPoliciesResourceWithStreamingResponse:
        """Define rules that determine which employees qualify for benefits"""
        from .resources.benefit_eligibility_policies import AsyncBenefitEligibilityPoliciesResourceWithStreamingResponse

        return AsyncBenefitEligibilityPoliciesResourceWithStreamingResponse(self._client.benefit_eligibility_policies)

    @cached_property
    def benefit_products(self) -> benefit_products.AsyncBenefitProductsResourceWithStreamingResponse:
        """Browse available benefit products that can be offered to employers"""
        from .resources.benefit_products import AsyncBenefitProductsResourceWithStreamingResponse

        return AsyncBenefitProductsResourceWithStreamingResponse(self._client.benefit_products)

    @cached_property
    def dependents(self) -> dependents.AsyncDependentsResourceWithStreamingResponse:
        """Manage dependent records (spouses, children) for employees"""
        from .resources.dependents import AsyncDependentsResourceWithStreamingResponse

        return AsyncDependentsResourceWithStreamingResponse(self._client.dependents)

    @cached_property
    def employees(self) -> employees.AsyncEmployeesResourceWithStreamingResponse:
        """Manage employee records for employers"""
        from .resources.employees import AsyncEmployeesResourceWithStreamingResponse

        return AsyncEmployeesResourceWithStreamingResponse(self._client.employees)

    @cached_property
    def employers(self) -> employers.AsyncEmployersResourceWithStreamingResponse:
        from .resources.employers import AsyncEmployersResourceWithStreamingResponse

        return AsyncEmployersResourceWithStreamingResponse(self._client.employers)

    @cached_property
    def enrollments(self) -> enrollments.AsyncEnrollmentsResourceWithStreamingResponse:
        """Manage benefit enrollments and elections for employees"""
        from .resources.enrollments import AsyncEnrollmentsResourceWithStreamingResponse

        return AsyncEnrollmentsResourceWithStreamingResponse(self._client.enrollments)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithStreamingResponse:
        from .resources.members import AsyncMembersResourceWithStreamingResponse

        return AsyncMembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def plan_years(self) -> plan_years.AsyncPlanYearsResourceWithStreamingResponse:
        """Configure annual benefit periods with coverage dates and contribution settings"""
        from .resources.plan_years import AsyncPlanYearsResourceWithStreamingResponse

        return AsyncPlanYearsResourceWithStreamingResponse(self._client.plan_years)


Client = VitableConnect

AsyncClient = AsyncVitableConnect
