from logging import getLogger
from typing import Optional
from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,

)
from app.services.persons.schemas import InputPersonSchema, InputListPersonSchema
from app.services.schemas import DocSchema, ResponseSchema
from app.cache import CACHE_CONFIG
from aiocache import cached

logger = getLogger(__name__)


class PersonService(BaseService):
    @cached(**CACHE_CONFIG)
    async def get_by_id(self, person_id: str) -> Optional[InputPersonSchema]:
        doc = await self._request(
            method=MethodEnum.get.value, index=IndexNameEnum.persons.value, id=person_id
        )
        return InputPersonSchema(**DocSchema(**doc).source)

    @cached(**CACHE_CONFIG)
    async def search(self, query: str) -> InputListPersonSchema:
        response = await self._request(
            method=MethodEnum.search.value, index=IndexNameEnum.persons.value,
            body={'query': {'match': {'full_name': {'query': query, 'fuzziness': 'AUTO'}}}}
        )

        result = ResponseSchema(**response)

        return InputListPersonSchema(
            __root__=[
                InputPersonSchema(**doc.source)
                for doc in result.hits.hits
            ]
        )
