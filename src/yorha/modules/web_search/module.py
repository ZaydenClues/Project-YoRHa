from __future__ import annotations

from yorha.core.manifest import ModuleManifest
from yorha.core.module import Module

from yorha.providers.search.duckduckgo import DuckDuckGoProvider

from .tool import WebSearchTool


class WebSearchModule(Module):
    def __init__(self) -> None:
        provider = DuckDuckGoProvider()

        self._tools = (
            WebSearchTool(provider),
        )

    @property
    def manifest(self) -> ModuleManifest:
        return ModuleManifest(
            name="web_search",
            version="0.1.0",
            description="Web search module.",
            tools=[
                tool.manifest
                for tool in self._tools
            ],
        )

    def tools(self):
        return self._tools