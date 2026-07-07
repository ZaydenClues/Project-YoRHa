from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

from yorha.core.manifest import ToolManifest
from yorha.models.execution_result import ExecutionResult


class Tool(ABC):
    """
    Base class for every executable YoRHa tool.
    """

    @property
    @abstractmethod
    def manifest(self) -> ToolManifest:
        ...

    @property
    @abstractmethod
    def input_model(self) -> type[BaseModel]:
        """
        Pydantic model describing this tool's input.
        """
        ...

    @abstractmethod
    async def execute(self, **kwargs: Any) -> ExecutionResult:
        ...