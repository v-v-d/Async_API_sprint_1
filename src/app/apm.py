from collections.abc import Callable
from functools import wraps
from typing import Any

from elasticapm import async_capture_span
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI

from app.settings import settings


def init_apm(app: FastAPI):
    if not settings.APM.ENABLED:
        return

    apm = make_apm_client(
        enabled=settings.APM.ENABLED,
        server_url=settings.APM.SERVER_URL,
        service_name=settings.APM.SERVICE_NAME,
        environment=settings.APM.ENVIRONMENT,
    )
    app.add_middleware(ElasticAPM, client=apm)


def traced(name: str) -> Callable:
    """
    Decorator that allow to trace all requests and queries that not
    covered by the project tracer.
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def inner(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
            if not settings.APM.ENABLED:
                return await func(*args, **kwargs)

            async with async_capture_span(name, labels={"args": args, **kwargs}):
                return await func(*args, **kwargs)

        return inner

    return wrapper
