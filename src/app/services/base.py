from enum import Enum
from logging import getLogger
from aioredis import Redis


import elasticsearch

logger = getLogger(__name__)


class BaseServiceError(Exception):
    pass


class NotFoundError(BaseServiceError):
    pass


class MethodNotAllowed(BaseServiceError):
    pass


class MethodEnum(str, Enum):
    get = "get"
    post = "post"
    search = "search"


class BaseService:
    def __init__(self, elastic: elasticsearch.AsyncElasticsearch, redis: Redis):
        self.redis = redis
        self.elastic = elastic


    async def _request(self, method: MethodEnum, *args, **kwargs):
        method = getattr(self.elastic, method, None)

        if not method:
            raise MethodNotAllowed("Method %s not allowed.", method)

        try:
            return await method(*args, **kwargs)
        except elasticsearch.exceptions.NotFoundError:
            raise NotFoundError
        except Exception as err:
            logger.exception("Request to elasticsearch failed!")
            raise BaseServiceError from err
