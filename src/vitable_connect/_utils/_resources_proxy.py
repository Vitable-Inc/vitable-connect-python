from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `vitable_connect.resources` module.

    This is used so that we can lazily import `vitable_connect.resources` only when
    needed *and* so that users can just import `vitable_connect` and reference `vitable_connect.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("vitable_connect.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
