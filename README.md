# Vitable Connect Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FVitable-Inc%2Fvitable-connect-python)
[![pypi](https://img.shields.io/pypi/v/vitable-connect)](https://pypi.python.org/pypi/vitable-connect)

The Vitable Connect Python library provides convenient access to the Vitable Connect APIs from Python.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Usage](#async-usage)
- [Using Types](#using-types)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Nested Params](#nested-params)
- [Handling Errors](#handling-errors)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Versioning](#versioning)
- [Requirements](#requirements)
- [Contributing](#contributing)

## Documentation

The REST API documentation can be found on [vitablehealth.com](https://vitablehealth.com/support). The full API of this library can be found in [api.md](api.md).

## Installation

```sh
pip install vitable-connect
```

## Reference

A full reference for this library is available [here](https://github.com/Vitable-Inc/vitable-connect-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from vitable_connect import VitableConnect

client = VitableConnect(
    api_key="<token>",
)

client.auth.issue_access_token(
    grant_type="client_credentials",
)
```

## Async usage

Simply import `AsyncVitableConnect` instead of `VitableConnect` and use `await` with each API call:

```python
import os
import asyncio
from vitable_connect import AsyncVitableConnect

client = AsyncVitableConnect(
    api_key=os.environ.get("VITABLE_CONNECT_API_KEY"),  # This is the default and can be omitted
    # defaults to "production".
    environment="environment_1",
)


async def main() -> None:
    response = await client.auth.issue_access_token(
        grant_type="client_credentials",
    )
    print(response.access_token)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install vitable_connect[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from vitable_connect import DefaultAioHttpClient
from vitable_connect import AsyncVitableConnect


async def main() -> None:
    async with AsyncVitableConnect(
        api_key=os.environ.get("VITABLE_CONNECT_API_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        response = await client.auth.issue_access_token(
            grant_type="client_credentials",
        )
        print(response.access_token)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Environments

This SDK allows you to configure different environments for API requests.

```python
from vitable_connect import VitableConnect
from vitable_connect.environment import VitableConnectEnvironment

client = VitableConnect(
    environment=VitableConnectEnvironment.PRODUCTION,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from vitable_connect import AsyncVitableConnect

client = AsyncVitableConnect(
    api_key="<token>",
)


async def main() -> None:
    await client.auth.issue_access_token(
        grant_type="client_credentials",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from vitable_connect.core.api_error import ApiError

try:
    client.auth.issue_access_token(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from vitable_connect import VitableConnect

client = VitableConnect(
    api_key="<token>",
)

client.employees.list_enrollments(
    employee_id="empl_abc123def456",
    limit=20,
    page=1,
)
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.employees.list_enrollments(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from vitable_connect import VitableConnect

client = VitableConnect()

response = client.auth.issue_access_token(
    grant_type="client_credentials",
    bound_entity={
        "id": "id",
        "type": "employer",
    },
)
print(response.bound_entity)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `vitable_connect.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `vitable_connect.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `vitable_connect.APIError`.

```python
import vitable_connect
from vitable_connect import VitableConnect

client = VitableConnect()

try:
    client.auth.issue_access_token(
        grant_type="client_credentials",
    )
except vitable_connect.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except vitable_connect.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except vitable_connect.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from vitable_connect import VitableConnect

# Configure the default for all requests:
client = VitableConnect(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).auth.issue_access_token(
    grant_type="client_credentials",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from vitable_connect import VitableConnect

# Configure the default for all requests:
client = VitableConnect(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = VitableConnect(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).auth.issue_access_token(
    grant_type="client_credentials",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from vitable_connect import VitableConnect

client = VitableConnect(...)
response = client.auth.with_raw_response.issue_access_token(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.auth.issue_access_token(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from vitable_connect import VitableConnect

client = VitableConnect(..., timeout=20.0)

# Override timeout for a specific method
client.auth.issue_access_token(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from vitable_connect import VitableConnect

client = VitableConnect(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Vitable-Inc/vitable-connect-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import vitable_connect
print(vitable_connect.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
