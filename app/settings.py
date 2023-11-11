from functools import lru_cache
from os.path import exists
from pydantic_settings import BaseSettings, SettingsConfigDict
from .db_init import populate_db


class Settings(BaseSettings):
    db_url: str = "sqlite:///./timetracker.db"
    jwt_secret_key: str
    jwt_secret_refresh_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()


env_settings = get_settings()

db_url: str = env_settings.db_url

if db_url.startswith("sqlite:///") and not exists(db_url[10:]):
    populate_db(db_url)

jwt_secret_key: str = env_settings.jwt_secret_key
jwt_secret_refresh_key: str = env_settings.jwt_secret_refresh_key
algorithm: str = env_settings.algorithm
access_token_expire_minutes: int = env_settings.access_token_expire_minutes
refresh_token_expire_minutes: int = env_settings.refresh_token_expire_minutes
