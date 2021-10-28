from logging import getLogger
from typing import Optional

from aiocache import cached

from app.cache import CACHE_CONFIG
from app.services.base import ElasticsearchService
from app.services.persons.schemas import InputPersonSchema, InputListPersonSchema

logger = getLogger(__name__)


class PersonService(ElasticsearchService):
    @cached(**CACHE_CONFIG)
    async def get_by_id(self, person_id: str) -> Optional[InputPersonSchema]:
        doc = await self.filter(id=person_id)
        return InputPersonSchema(**doc.source)

    async def search(
        self, page: int, size: int, *, query: str
    ) -> InputListPersonSchema:
        docs = await self.all(
            body={
                "query": {"match": {"full_name": {"query": query, "fuzziness": "AUTO"}}}
            },
            from_=page,
            size=size,
        )

        return InputListPersonSchema(
            __root__=[InputPersonSchema(**doc.source) for doc in docs]
        )
