from __future__ import annotations

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    """
    Normalized search request.
    """

    query: str
    max_results: int = 5


class SearchResult(BaseModel):
    """
    A single normalized search result.
    """

    title: str
    url: str
    snippet: str


class SearchResponse(BaseModel):
    """
    Normalized search response independent of any provider.
    """

    results: list[SearchResult] = Field(default_factory=list)