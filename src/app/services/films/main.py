from logging import getLogger
from typing import Optional

from aiocache import cached

from app.cache import CACHE_CONFIG
from app.services.base import ElasticsearchService
from app.services.films.schemas import (
    InputFilmSchema,
    InputListFilmSchema,
)
from app.services.schemas import (
    MultiMatchSchema,
    MatchSchema,
    FilterSchema,
    NestedSchema,
    SortSchema,
    OrderSchema,
    RootQuerySchema,
    BoolSchema,
    MultiMatchQuerySchema,
)

logger = getLogger(__name__)


class FilmsService(ElasticsearchService):
    @cached(**CACHE_CONFIG)
    async def get_by_id(self, film_id: str) -> InputFilmSchema:
        doc = await self.filter(id=film_id)
        return InputFilmSchema(**doc.source)

    @cached(**CACHE_CONFIG)
    async def get_all(
        self,
        page: int,
        size: int,
        *,
        genre_id: Optional[str] = None,
        person_id: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> InputListFilmSchema:
        q = self.get_query(genre_id=genre_id, person_id=person_id, sort=sort)
        docs = await self.all(from_=page, size=size, body=q)

        return InputListFilmSchema(
            __root__=[InputFilmSchema(**doc.source) for doc in docs]
        )

    async def search_by_query(
        self,
        page: int,
        size: int,
        *,
        query: Optional[str] = None,
    ) -> InputListFilmSchema:
        q = self.get_query(query=query)
        docs = await self.all(from_=page, size=size, body=q)

        return InputListFilmSchema(
            __root__=[InputFilmSchema(**doc.source) for doc in docs]
        )

    def get_query(
        self,
        query: Optional[str] = None,
        genre_id: Optional[str] = None,
        person_id: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> str:
        """Query management imitation."""
        q = RootQuerySchema(__root__={"query": BoolSchema(bool={})})

        if query or genre_id or person_id:
            q.__root__["query"].bool["must"] = []

        if query:
            mm_q = MultiMatchSchema(
                multi_match=MultiMatchQuerySchema(
                    query=query, fields=["title^3", "description"]
                )
            )
            q.__root__["query"].bool["must"].append(mm_q)

        if genre_id:
            f_query = self._get_filter_by_id_query("genres", genre_id)
            q.__root__["query"].bool["must"].append(f_query)

        if person_id:
            sub_q = BoolSchema(bool={"should": []})

            for field_name in ("directors", "actors", "writers"):
                f_query = self._get_filter_by_id_query(field_name, person_id)
                sub_q.bool["should"].append(f_query)

            q.__root__["query"].bool["must"].append(sub_q)

        if sort:
            field = self._get_sorting_field(sort)

            if field:
                order = self._get_sorting_type(sort)
                q.__root__.update(SortSchema(sort={field: OrderSchema(order=order)}))

        return q.json()

    @staticmethod
    def _get_filter_by_id_query(
        field_name: str,
        field_id: str,
    ) -> FilterSchema:
        nested_field_name = f"{field_name}.id"
        sub_q = BoolSchema(bool={"must": []})
        match = MatchSchema(match={nested_field_name: field_id})
        sub_q.bool["must"].append(match)

        return FilterSchema(nested=NestedSchema(path=field_name, query=sub_q))

    @staticmethod
    def _get_sorting_field(sort: str) -> Optional[str]:
        return sort.removeprefix("-")

    @staticmethod
    def _get_sorting_type(sort: str) -> str:
        if sort.startswith("-"):
            return "desc"

        return "asc"
