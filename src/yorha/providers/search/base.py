from __future__ import annotations

from abc import ABC, abstractmethod

from yorha.modules.web_search.models import (
    SearchRequest,
    SearchResponse,
)


class SearchProvider(ABC):
    """
    Base class for search providers.
    """

    @abstractmethod
    async def search(
        self,
        request: SearchRequest,
    ) -> SearchResponse:
        raise NotImplementedError