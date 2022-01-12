from logging import getLogger
from typing import Optional

from app.cache import cached_and_traced
from app.services.base import ElasticsearchService
from app.services.genres.schemas import InputGenreSchema, InputListGenreSchema

logger = getLogger(__name__)


class GenreService(ElasticsearchService):
    @cached_and_traced
    async def get_by_id(self, genre_id: str) -> Optional[InputGenreSchema]:
        doc = await self.filter(id=genre_id)
        return InputGenreSchema(**doc.source)

    @cached_and_traced
    async def search(self, page: int, size: int) -> InputListGenreSchema:
        docs = await self.all(
            body={"query": {"match_all": {}}},
            from_=page,
            size=size,
        )

        return InputListGenreSchema(
            __root__=[InputGenreSchema(**doc.source) for doc in docs]
        )
