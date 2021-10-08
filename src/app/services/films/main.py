from logging import getLogger

from app.services.films.schemas import FilmSchema
from elasticsearch import AsyncElasticsearch

logger = getLogger(__name__)


class FilmsService:
    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic
    
    # @cached()  # TODO
    async def get_by_id(self, film_id: str) -> FilmSchema | None:
        return await self._get_film_from_elastic(film_id)

    async def _get_film_from_elastic(self, film_id: str) -> FilmSchema | None:
        doc = await self.elastic.get("movies", film_id)
        return FilmSchema(**doc["_source"])
