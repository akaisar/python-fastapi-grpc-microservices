import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    database_url: AnyUrl = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10
    SECRET_KEY: str = "12345"


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()

settings = get_settings()
