from enum import Enum
from logging import getLogger
from typing import Any

import backoff
import elasticsearch

from app.cache import get_cache_config
from app.settings import settings


logger = getLogger(__name__)


class BaseServiceError(Exception):
    pass


class ESConnectionError(BaseServiceError):
    pass


class NotFoundError(BaseServiceError):
    pass


class MethodNotAllowed(BaseServiceError):
    pass


class MethodEnum(str, Enum):
    get = "get"
    search = "search"


class BaseService:
    CACHE_CONFIG = get_cache_config()

    def __init__(self, elastic: elasticsearch.AsyncElasticsearch):
        self.elastic = elastic

    @backoff.on_exception(
        wait_gen=backoff.expo,
        max_time=settings.BACKOFF.MAX_TIME_SEC,
        exception=ESConnectionError,
    )
    async def _request_elastic(
        self, method: MethodEnum, *args, **kwargs
    ) -> dict[str, Any]:
        method = getattr(self.elastic, method, None)

        if not method:
            raise MethodNotAllowed("Method %s not allowed.", method)

        try:
            return await method(*args, **kwargs)
        except elasticsearch.exceptions.ConnectionError as err:
            raise ESConnectionError from err
        except elasticsearch.exceptions.NotFoundError:
            raise NotFoundError
        except Exception as err:
            logger.exception("Request to elasticsearch failed!")
            raise BaseServiceError from err
