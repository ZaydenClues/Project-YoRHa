from contextlib import asynccontextmanager

from fastapi import FastAPI

from yorha.kernel.runtime import runtime
from yorha.modules.web_search.models import (
    SearchRequest,
    SearchResponse,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runtime is already started by the parent app.
    yield


search_app = FastAPI(
    title="YoRHa Search",
    version="0.1.0",
    lifespan=lifespan,
)

from fastapi import APIRouter

config_router = APIRouter(prefix="/api")


@config_router.get("/config")
async def config():
    return {
        "name": "YoRHa Search",
        "description": "Web search tool",
        "version": "0.1.0",
    }


search_app.include_router(config_router)

@search_app.post(
    "/search",
    operation_id="web_search",
    summary="Search the public web",
    description="""
Search the live public web.

Use this tool whenever the user asks for:
- current events
- recent news
- today's information
- live facts
- information after the model's training cutoff
- verification of uncertain facts

Do not rely on internal knowledge if the user requests recent or live information.
""",
)
async def search(request: SearchRequest):
    tool = runtime.registry.get_tool("search_web")

    result = await tool.execute(**request.model_dump())

    return result.data