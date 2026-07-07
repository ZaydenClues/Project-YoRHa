from __future__ import annotations

import asyncio

from ddgs import DDGS

from yorha.modules.web_search.models import (
    SearchRequest,
    SearchResponse,
    SearchResult,
)
from yorha.providers.search.base import SearchProvider


class DuckDuckGoProvider(SearchProvider):
    """
    DuckDuckGo implementation of the SearchProvider interface.
    """

    async def search(
        self,
        request: SearchRequest,
    ) -> SearchResponse:
        return await asyncio.to_thread(
            self._search_sync,
            request,
        )

    def _search_sync(
        self,
        request: SearchRequest,
    ) -> SearchResponse:
        with DDGS() as ddgs:
            raw_results = list(
                ddgs.text(
                    request.query,
                    max_results=request.max_results,
                )
            )
        print(f"Raw results: {raw_results}")

        results = [
            SearchResult(
                title=item.get("title", ""),
                url=item.get("href", ""),
                snippet=item.get("body", ""),
            )
            for item in raw_results
        ]

        return SearchResponse(results=results)