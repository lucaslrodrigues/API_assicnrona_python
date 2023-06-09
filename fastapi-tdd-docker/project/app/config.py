import logging
from functools import lru_cache
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    enviroment: str = "dev"
    testing: bool = bool(0)

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the enviroment...")
    return Settings()