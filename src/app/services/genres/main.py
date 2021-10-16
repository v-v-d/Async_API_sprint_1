from logging import getLogger
from typing import Optional

from aiocache import cached

from app.cache import CACHE_CONFIG
from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
)
from app.services.genres.schemas import InputGenreSchema, InputListGenreSchema
from app.services.schemas import DocSchema, ResponseSchema

logger = getLogger(__name__)


class GenreService(BaseService):
    @cached(**CACHE_CONFIG)
    async def get_by_id(self, genre_id: str) -> Optional[InputGenreSchema]:
        doc = await self._request(
            method=MethodEnum.get.value, index=IndexNameEnum.genres.value, id=genre_id
        )
        return InputGenreSchema(**DocSchema(**doc).source)

    @cached(**CACHE_CONFIG)
    async def search(self, page: int, size: int) -> InputListGenreSchema:
        response = await self._request(
            method=MethodEnum.search.value,
            index=IndexNameEnum.genres.value,
            body={"query": {"match_all": {}}},
            from_=page,
            size=size,
        )
        result = ResponseSchema(**response)
        return InputListGenreSchema(
            __root__=[InputGenreSchema(**doc.source) for doc in result.hits.hits]
        )
