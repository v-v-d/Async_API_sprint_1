from pathlib import Path

from pydantic import BaseSettings, AnyHttpUrl, AnyUrl, validator


class UvicornSettings(BaseSettings):
    """
    Config for running the app. Not used in main app config.
    """

    app: str = "app.main:app"
    host: str = "0.0.0.0"
    port: int = 8088
    reload: bool = False
    workers: int = 3

    class Config:
        env_prefix = "UVICORN_"


class CacheSettings(BaseSettings):
    REDIS_HOST: str = "api-redis"
    REDIS_PORT: int = 6379
    TTL: int = 60 * 5


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
    DEFAULT_PAGE: int = 0
    DEFAULT_PAGE_SIZE: int = 50

    class Config:
        env_prefix = "ES_"


class BackoffSettings(BaseSettings):
    MAX_TIME_SEC: int = 10

    class Config:
        env_prefix = "BACKOFF_"


class AuthSettings(BaseSettings):
    SECRET_KEY: str = "super-secret"
    ALGORITHM: str = "HS256"

    class Config:
        env_prefix = "AUTH_"


class APMSettings(BaseSettings):
    ENABLED: bool
    SERVER_URL: str
    SERVICE_NAME: str
    ENVIRONMENT: str

    class Config:
        env_prefix = "APM_"


class CommonSettings(BaseSettings):
    PROJECT_NAME: str = "movies"
    OPENAPI_URL: str = "/api/openapi.json"
    BASIC_AUTH_USERNAME: str
    BASIC_AUTH_PASSWD: str
    ALLOWED_HOSTS: list[str]

    DEBUG: bool = False
    TESTING: bool = False
    LOG_LEVEL: str = "INFO"
    SHARED_DIR: str = "/code/shared"
    DIR_LOGS: Path = Path(SHARED_DIR, "/code/shared/logs")

    VALID_SORTING_FIELDS: list[str] = ["rating"]

    UVICORN: UvicornSettings = UvicornSettings()
    CACHE: CacheSettings = CacheSettings()
    ES: ElasticSearchSettings = ElasticSearchSettings()
    BACKOFF: BackoffSettings = BackoffSettings()
    AUTH: AuthSettings = AuthSettings()
    APM: APMSettings = APMSettings()
