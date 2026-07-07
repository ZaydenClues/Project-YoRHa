from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ExecutionResult(BaseModel):
    """
    Standard response returned by every YoRHa tool.

    The runtime only understands this object. The `data` field may
    contain any module-specific response model.
    """

    success: bool = True

    message: str = ""

    data: Any | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)