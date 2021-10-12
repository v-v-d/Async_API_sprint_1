from logging import getLogger

from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
)
from app.services.persons.schemas import InputPersonSchema, InputListPersonSchema
from app.services.schemas import DocSchema, ResponseSchema

logger = getLogger(__name__)


class PersonService(BaseService):
    # @cached()  # TODO
    async def get_by_id(self, person_id: str) -> InputPersonSchema | None:
        doc = await self._request(
            method=MethodEnum.get.value, index=IndexNameEnum.persons.value, id=person_id
        )
        return InputPersonSchema(**DocSchema(**doc).source)

    async def get_all_id(self) -> InputPersonSchema | None:
        doc = await self._request(
            method=MethodEnum.search.value, index=IndexNameEnum.persons.value
        )
        return InputPersonSchema(**DocSchema(**doc).source)

    async def get_name_person(self, name_person: str) -> InputPersonSchema:
        response = await self._request(
            method=MethodEnum.search.value, index=IndexNameEnum.persons.value,
            body={'query': {'match': {'full_name': {'query': name_person, 'fuzziness': 'AUTO'}}}}
        )
        result = ResponseSchema(**response)
        return InputListPersonSchema(
            __root__=[
                InputPersonSchema(**doc.source)
                for doc in result.hits.hits
            ]
        )
