from enum import Enum
from functools import wraps
from logging import Logger
from typing import Callable

from elasticsearch import AsyncElasticsearch


class BaseServiceError(Exception):
    pass


class MethodNotAllowed(BaseServiceError):
    pass


class MethodEnum(str, Enum):
    get = "get"
    post = "post"


class BaseService:
    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic

    async def _request(self, method: MethodEnum, *args, **kwargs):
        method = getattr(self.elastic, method, None)

        if not method:
            raise MethodNotAllowed("Method %s not allowed.", method)

        try:
            return await method(*args, **kwargs)
        except Exception as err:
            raise BaseServiceError from err


def exc_handled(logger: Logger, exc: Callable):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except (BaseServiceError, MethodNotAllowed) as err:
                logger.exception("Request to elasticsearch failed!")
                raise exc from err

        return wrapper

    return decorator
