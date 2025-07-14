from pydantic import Field, AnyUrl
from pydantic_settings import BaseSettings
import os

class AppSettings(BaseSettings):
    DEBUG: bool = False
    API_HOST: str = "0.0.0.0"
    APP_ENV: str = os.getenv("APP_ENV", "local")
    APP_TAG: str = Field("local")
    # config.py or similar
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = os.getenv("REDIS_PORT", "6379")

settings = AppSettings()
