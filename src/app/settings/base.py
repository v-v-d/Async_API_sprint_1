from pathlib import Path

from pydantic import BaseSettings, AnyHttpUrl, AnyUrl, validator


class UvicornSettings(BaseSettings):
    app: str = "app.main:app"
    host: str = "0.0.0.0"
    port: int = 8088
    reload: bool = False

    class Config:
        env_prefix = "UVICORN_"


class CacheSettings(BaseSettings):
    REDIS_HOST: str = "api-redis"
    REDIS_PORT: int = 6379

    class Config:
        env_prefix = "CACHE_"


class BaseDSNSettings(BaseSettings):
    USER: str = ""
    PASSWORD: str = ""
    HOST: str = ""
    PORT: int = 0
    PROTOCOL: str = ""
    PATH: str = ""
    DSN: AnyUrl = None

    @validator("DSN", pre=True)
    def build_dsn(cls, v, values) -> str:
        if v:
            return v

        protocol = values["PROTOCOL"]
        user = values["USER"]
        passwd = values["PASSWORD"]
        host = values["HOST"]
        port = values["PORT"]
        path = values["PATH"]

        if user and passwd:
            return f"{protocol}://{user}:{passwd}@{host}:{port}/{path}"

        return f"{protocol}://{host}:{port}/{path}"


class ElasticSearchSettings(BaseDSNSettings):
    PROTOCOL: str = "http"
    DSN: AnyHttpUrl = None
    TIMEOUT: int = 30
    DEFAULT_PAGE: int = 1
    DEFAULT_PAGE_SIZE: int = 50

    class Config:
        env_prefix = "ES_"


class CommonSettings(BaseSettings):
    PROJECT_NAME: str = "movies"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    SHARED_DIR: str = "/app/shared"
    DIR_LOGS: Path = Path(SHARED_DIR, "/app/shared/logs")

    UVICORN: UvicornSettings = UvicornSettings()
    CACHE: CacheSettings = CacheSettings()
    ES: ElasticSearchSettings = ElasticSearchSettings()
