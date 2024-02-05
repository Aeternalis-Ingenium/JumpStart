from enum import Enum
from functools import lru_cache
from logging import INFO
from os import environ
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvironment(str, Enum):
    STAGING = "staging"
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class AppSettings(BaseSettings):
    TITLE: str = "PLENO - Data Infrastructure"
    VERSION: str = environ["APP_VERSION"]
    TIMEZONE: str = "UTC"
    DESCRIPTION: str = ""
    IS_DEBUG: bool = False
    API_PREFIX: str = environ["API_PREFIX"]
    DOCS_URL: str = environ["DOCS_URL"]
    OPENAPI_URL: str = environ["OPENAPI_URL"]
    REDOC_URL: str = environ["REDOC_URL"]
    OPENAPI_PREFIX: str = ""

    HOST: str = environ["SERVER_HOST"]
    PORT: int = int(environ["SERVER_PORT"])
    WORKERS: int = int(environ["SERVER_WORKERS"])
    IS_ALLOWED_CREDENTIALS: bool = bool(environ["IS_ALLOWED_CREDENTIALS"])
    ALLOWED_ORIGIN_LIST: list[str] = ["*"]
    ALLOWED_METHOD_LIST: list[str] = [
        environ["METHOD_1"],
        environ["METHOD_2"],
        environ["METHOD_3"],
        environ["METHOD_4"],
        environ["METHOD_5"],
    ]
    ALLOWED_HEADER_LIST: list[str] = [environ["ALL_HEADERS"]]
    LOGGING_LEVEL: int = INFO
    LOGGERS: tuple[str, str] = (environ["ASGI_LOGGER"], environ["ACCESS_LOGGER"])
    SECRET_KEY: SecretStr = SecretStr(environ["SECRET_KEY"])

    model_config = SettingsConfigDict(
        env_file=f"{Path().resolve()}/.env",
        case_sensitive=True,
        validate_assignment=True,
        extra="allow",
    )

    @property
    def set_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.IS_DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }


class AppStagingSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.STAGING
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."
    IS_DEBUG: bool = True


class AppDevelopmentSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.DEVELOPMENT
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."
    IS_DEBUG: bool = True


class AppProductionSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.PRODUCTION
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."


class FactoryAppSettings:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> AppSettings:
        if self.environment == AppEnvironment.PRODUCTION:
            return AppProductionSettings()
        elif self.environment == AppEnvironment.STAGING:
            return AppStagingSettings()
        return AppDevelopmentSettings()


@lru_cache()
def get_settings() -> AppSettings:
    return FactoryAppSettings(environment=environ["APP_ENV"])()


settings = get_settings()
