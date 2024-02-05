from typing import Callable

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from src.api.endpoint import router
from src.core.config import AppSettings, settings
from src.core.event import event_manager


class App:
    def __init__(self, event_manager: Callable, router: APIRouter, settings: AppSettings):
        self.__app = FastAPI(lifespan=event_manager, **settings.set_app_attributes)  # type: ignore
        self.__setup_middlewares(settings=settings)
        self.__add_routes(router=router, settings=settings)

    def __setup_middlewares(self, settings: AppSettings):
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_ORIGIN_LIST,
            allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
            allow_methods=settings.ALLOWED_METHOD_LIST,
            allow_headers=settings.ALLOWED_HEADER_LIST,
        )

    def __add_routes(self, router: APIRouter, settings: AppSettings):
        self.__app.include_router(router=router, prefix=settings.API_PREFIX)

    def __call__(self) -> FastAPI:
        return self.__app


def initialize_application() -> FastAPI:
    return App(event_manager=event_manager, router=router, settings=settings)()


app = initialize_application()


if __name__ == "__main__":
    run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.IS_DEBUG,
        workers=settings.WORKERS,
    )
