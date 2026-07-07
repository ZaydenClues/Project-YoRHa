from yorha.config import settings
from yorha.core.container import Container
from yorha.core.registry import Registry
from yorha.kernel.module_manager import ModuleManager
from yorha.modules.web_search.module import WebSearchModule
from yorha.services.logging import configure_logging

import logging


class Runtime:
    def __init__(self):
        self.settings = settings

        self.container = Container()
        self.registry = Registry()
        self.module_manager = ModuleManager(self.registry)

        self.logger = logging.getLogger("yorha")

    async def startup(self):
        configure_logging()

        self.container.register(Registry, self.registry)
        self.container.register(ModuleManager, self.module_manager)

        self.module_manager.load(WebSearchModule())

        self.logger.info(
            "Loaded %d module(s)",
            len(self.registry.list_modules()),
        )

    async def shutdown(self):
        self.logger.info("Stopping YoRHa Runtime")

    def info(self):
        return {
            "runtime": self.settings.app_name,
            "version": self.settings.version,
            "modules": len(self.registry.list_modules()),
            "tools": len(self.registry.list_tools()),
        }


runtime = Runtime()