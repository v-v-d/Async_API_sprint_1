from logging import getLogger

from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
)
from app.services.films.schemas import (
    InputFilmSchema,
    QuerySchema,
    MatchSchema,
    InputListFilmSchema,
)
from app.services.schemas import DocSchema, ResponseSchema

logger = getLogger(__name__)


class FilmsService(BaseService):
    # @cached()  # TODO
    async def get_by_id(self, film_id: str) -> InputFilmSchema:
        response = await self._request(
            method=MethodEnum.get.value, index=IndexNameEnum.movies.value, id=film_id
        )
        return InputFilmSchema(**DocSchema(**response).source)

    # @cached()  # TODO
    async def search(self, query: str, page: int, size: int) -> InputListFilmSchema:
        q = MatchSchema(multi_match=QuerySchema(query=query)).dict()
        response = await self._request(
            method=MethodEnum.search.value,
            index=IndexNameEnum.movies.value,
            query=q,
            from_=page,
            size=size
        )

        result = ResponseSchema(**response)

        return InputListFilmSchema(
            __root__=[
                InputFilmSchema(**doc.source)
                for doc in result.hits.hits
            ]
        )
