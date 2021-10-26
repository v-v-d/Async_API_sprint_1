from abc import ABC, abstractmethod
from enum import Enum
from logging import getLogger
from typing import Any, Union

import backoff
import elasticsearch

from app.elastic import IndexNameEnum
from app.services.schemas import DocSchema, ResponseSchema
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


class AbstractService(ABC):
    @abstractmethod
    async def filter(self, value: Any, *args, **kwargs):
        pass

    @abstractmethod
    async def all(self, *args, **kwargs):
        pass

    @abstractmethod
    def backoff_exc(self) -> Union[Exception, tuple[Exception, ...]]:
        pass

    @abstractmethod
    async def _execute(self, *args, **kwargs):
        pass

    async def execute(self, *args, **kwargs):
        # standard decorator syntax sugar doesn't work with abstract methods, because
        # it rises TypeError: catching classes that do not inherit from BaseException
        # is not allowed
        return await backoff.on_exception(
            wait_gen=backoff.expo,
            max_time=settings.BACKOFF.MAX_TIME_SEC,
            exception=self.backoff_exc,
        )(self._execute)(*args, **kwargs)


class ElasticsearchService(AbstractService):
    backoff_exc = ESConnectionError

    def __init__(self, elastic: elasticsearch.AsyncElasticsearch, index: IndexNameEnum):
        self.elastic = elastic
        self.index = index

    async def filter(self, *args, **kwargs) -> DocSchema:
        response = await self.execute(method=MethodEnum.get.value, *args, **kwargs)
        return DocSchema(**response)

    async def all(self, *args, **kwargs) -> list[DocSchema]:
        response = await self.execute(method=MethodEnum.search.value, *args, **kwargs)
        return ResponseSchema(**response).hits.hits

    async def _execute(self, method: MethodEnum, *args, **kwargs) -> dict[str, Any]:
        method = getattr(self.elastic, method, None)

        if not method:
            raise MethodNotAllowed("Method %s not allowed.", method)

        try:
            return await method(index=self.index, *args, **kwargs)
        except elasticsearch.exceptions.ConnectionError as err:
            raise ESConnectionError from err
        except elasticsearch.exceptions.NotFoundError:
            raise NotFoundError
        except Exception as err:
            logger.exception("Request to elasticsearch failed!")
            raise BaseServiceError from err
