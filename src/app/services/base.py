from enum import Enum
from logging import getLogger
from typing import Any

import backoff
import elasticsearch

from app.settings import settings
from app.utils import get_backoff_type

logger = getLogger(__name__)


class BaseServiceError(Exception):
    pass


class NotFoundError(BaseServiceError):
    pass


class MethodNotAllowed(BaseServiceError):
    pass


class MethodEnum(str, Enum):
    get = "get"
    search = "search"


class BaseService:
    BACKOFF_TYPE = get_backoff_type()

    def __init__(self, elastic: elasticsearch.AsyncElasticsearch):
        self.elastic = elastic

    @backoff.on_exception(
        wait_gen=BACKOFF_TYPE,
        max_time=settings.BACKOFF.MAX_TIME_SEC,
        exception=elasticsearch.ConnectionError,
    )
    async def _request_elastic(self, method: MethodEnum, *args, **kwargs) -> dict[str, Any]:
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
