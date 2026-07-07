from fastapi import APIRouter

from yorha.kernel.runtime import runtime
from yorha.modules.web_search.models import SearchRequest, SearchResponse

router = APIRouter(
    prefix="/search",
    tags=["Web Search"],
)


@router.post(
    "",
    response_model=SearchResponse,
    summary="Search the web",
    description="Search the web using YoRHa's configured search provider.",
)
async def search(request: SearchRequest) -> SearchResponse:
    tool = runtime.registry.get_tool("search_web")

    result = await tool.execute(**request.model_dump())

    if not result.success:
        raise RuntimeError(result.message)

    return result.data