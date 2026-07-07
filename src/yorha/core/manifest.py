from __future__ import annotations

from pydantic import BaseModel, Field


class ToolManifest(BaseModel):
    """Metadata describing a tool."""

    name: str
    description: str


class ModuleManifest(BaseModel):
    """Metadata describing a module."""

    name: str
    version: str
    description: str

    tools: list[ToolManifest] = Field(default_factory=list)