from __future__ import annotations

from typing import Any


class Container:
    """
    Simple application service container.
    """

    def __init__(self) -> None:
        self._services: dict[type, Any] = {}

    def register(self, service_type: type, instance: Any) -> None:
        self._services[service_type] = instance

    def resolve(self, service_type: type):
        try:
            return self._services[service_type]
        except KeyError as exc:
            raise LookupError(
                f"Service '{service_type.__name__}' is not registered."
            ) from exc