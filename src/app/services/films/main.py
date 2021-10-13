from logging import getLogger
from typing import Optional

from app.elastic import IndexNameEnum
from app.services.base import (
    BaseService,
    MethodEnum,
)
from app.services.films.schemas import (
    InputFilmSchema,
    InputListFilmSchema,
)
from app.services.schemas import DocSchema, ResponseSchema, MatchSchema, MultiMatchQuerySchema

logger = getLogger(__name__)


class FilmsService(BaseService):
    # @cached()  # TODO
    async def get_by_id(self, film_id: str) -> InputFilmSchema:
        response = await self._request(
            method=MethodEnum.get.value, index=IndexNameEnum.movies.value, id=film_id
        )
        return InputFilmSchema(**DocSchema(**response).source)

    # @cached()  # TODO
    async def search(
        self,
        page: int,
        size: int,
        *,
        query: Optional[str] = None,
        genre_id: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> InputListFilmSchema:
        # q = MatchSchema(multi_match=MultiMatchQuerySchema(query=query)).dict()
        q = {
            "query": {
                "bool": {
                    "must": []
                }
            }
        }

        if query:
            search_query = {
                "multi_match": {
                    "query": query,
                    "fields": ["title^3", "description"],
                    "fuzziness": "AUTO"
                }
            }
            q["query"]["bool"]["must"].append(search_query)

        if genre_id:
            filter_by_genre = {
                "nested": {
                    "path": "genres",
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "match": {
                                        "genres.id": genre_id
                                    }
                                }
                            ]
                        }
                    }
                }
            }
            q["query"]["bool"]["must"].append(filter_by_genre)

        if sort:
            mapper = {
                "rating": "asc",
                "-rating": "desc",
            }

            if mapper.get(sort):
                sort_by_rating = {
                    "rating": {
                        "order": mapper.get(sort)
                    }
                }
                q["sort"] = sort_by_rating

        response = await self._request(
            method=MethodEnum.search.value,
            index=IndexNameEnum.movies.value,
            body=q,
            # query=q,
            from_=page,
            size=size,
        )

        result = ResponseSchema(**response)

        return InputListFilmSchema(
            __root__=[
                InputFilmSchema(**doc.source)
                for doc in result.hits.hits
            ]
        )
