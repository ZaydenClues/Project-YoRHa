from __future__ import annotations

from yorha.core.module import Module
from yorha.core.registry import Registry


class ModuleManager:
    """
    Loads modules into the registry.
    """

    def __init__(self, registry: Registry) -> None:
        self._registry = registry

    def load(self, module: Module) -> None:
        self._registry.register_module(module)

    @property
    def registry(self) -> Registry:
        return self._registry