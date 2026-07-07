from __future__ import annotations

from yorha.core.module import Module
from yorha.core.tool import Tool


class Registry:
    """
    Stores all loaded modules and exposes their tools.
    """

    def __init__(self) -> None:
        self._modules: dict[str, Module] = {}

    def register_module(self, module: Module) -> None:
        name = module.manifest.name

        if name in self._modules:
            raise ValueError(f"Module '{name}' already registered.")

        self._modules[name] = module

    def get_module(self, name: str) -> Module:
        return self._modules[name]

    def list_modules(self) -> list[Module]:
        return list(self._modules.values())

    def list_tools(self) -> list[Tool]:
        tools: list[Tool] = []

        for module in self._modules.values():
            tools.extend(module.tools())

        return tools

    def get_tool(self, name: str) -> Tool:
        for tool in self.list_tools():
            if tool.manifest.name == name:
                return tool

        raise KeyError(f"Tool '{name}' not found.")