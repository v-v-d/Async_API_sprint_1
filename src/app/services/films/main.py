from logging import getLogger
from typing import Optional
from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
)
from app.services.films.schemas import FilmSchema
from app.services.schemas import DocSchema
from aiocache import cached
from app.cache import CACHE_CONFIG


logger = getLogger(__name__)


class FilmsService(BaseService):
    @cached(**CACHE_CONFIG)
    async def get_by_id(self, film_id: str) -> Optional[FilmSchema]:
        doc = await self._request_elastic(
            method=MethodEnum.get.value, index=IndexNameEnum.movies.value, id=film_id
        )
        return FilmSchema(**DocSchema(**doc).source)
