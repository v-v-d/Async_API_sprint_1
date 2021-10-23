from logging import getLogger
from typing import Optional

from aiocache import cached

from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
)
from app.services.persons.schemas import InputPersonSchema, InputListPersonSchema
from app.services.schemas import DocSchema, ResponseSchema

logger = getLogger(__name__)


class PersonService(BaseService):
    @cached(**BaseService.CACHE_CONFIG)
    async def get_by_id(self, person_id: str) -> Optional[InputPersonSchema]:
        doc = await self._request_elastic(
            method=MethodEnum.get.value, index=IndexNameEnum.persons.value, id=person_id
        )
        return InputPersonSchema(**DocSchema(**doc).source)

    async def search(
        self, page: int, size: int, *, query: str
    ) -> InputListPersonSchema:
        response = await self._request_elastic(
            method=MethodEnum.search.value,
            index=IndexNameEnum.persons.value,
            body={
                "query": {"match": {"full_name": {"query": query, "fuzziness": "AUTO"}}}
            },
            from_=page,
            size=size,
        )

        result = ResponseSchema(**response)

        return InputListPersonSchema(
            __root__=[InputPersonSchema(**doc.source) for doc in result.hits.hits]
        )
