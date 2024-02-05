from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.logger import log


@asynccontextmanager
async def event_manager(app: FastAPI):
    log.info(msg="Welcome 🛬")
    log.info(msg=f"Application v{app.version} started elegantly!")
    yield
    log.info(msg="Goodbye 🚀")
    log.info(msg=f"Application v{app.version} shut down gracefully!")
