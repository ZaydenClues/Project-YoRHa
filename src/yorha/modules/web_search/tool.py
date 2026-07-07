from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from .models import SearchRequest

from yorha.core.manifest import ToolManifest
from yorha.core.tool import Tool
from yorha.models.execution_result import ExecutionResult
from yorha.modules.web_search.models import SearchRequest
from yorha.providers.search.duckduckgo import DuckDuckGoProvider


class WebSearchTool(Tool):
    def __init__(
        self,
        provider: DuckDuckGoProvider,
    ) -> None:
        self._provider = provider

    @property
    def manifest(self) -> ToolManifest:
        return ToolManifest(
            name="search_web",
            description="Search the web.",
        )
    
    @property
    def input_model(self) -> type[BaseModel]:
        return SearchRequest

    async def execute(
        self,
        **kwargs: Any,
    ) -> ExecutionResult:
        query = kwargs.get("query")

        if not query:
            return ExecutionResult(
                success=False,
                message="Missing required parameter: query",
            )

        request = SearchRequest(query=query)

        response = await self._provider.search(request)

        return ExecutionResult(
            success=True,
            data=response,
        )