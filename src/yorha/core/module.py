from __future__ import annotations

from abc import ABC
from collections.abc import Sequence

from yorha.core.manifest import ModuleManifest
from yorha.core.tool import Tool


class Module(ABC):
    """
    Base class for all YoRHa modules.
    """

    manifest: ModuleManifest

    def tools(self) -> Sequence[Tool]:
        """
        Return all tools exposed by this module.
        """
        return ()