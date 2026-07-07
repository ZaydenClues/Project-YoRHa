from contextlib import asynccontextmanager

from fastapi import FastAPI

from yorha.api.routers import health, tools
from yorha.config import settings
from yorha.kernel.runtime import runtime
from yorha.api.routers import search
from yorha.api.routers import config
from yorha.api.search_app import search_app

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await runtime.startup()
    yield
    await runtime.shutdown()


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    lifespan=lifespan,
)



app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/search", search_app)  # Mount the search app at /search

app.include_router(health.router)
app.include_router(tools.router)
# app.include_router(search.router)
app.include_router(config.router)