from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class ToolDefinition(BaseModel):
    name: str
    description: str
    input_schema: dict[str, Any]


class ExecuteToolRequest(BaseModel):
    tool: str
    arguments: dict[str, Any]