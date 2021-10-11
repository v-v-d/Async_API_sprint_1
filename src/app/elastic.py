from enum import Enum

from elasticsearch import AsyncElasticsearch


class IndexNameEnum(str, Enum):
    movies = "movies"
    persons = "persons"
    genres = "genres"


es: AsyncElasticsearch | None


async def get_elastic() -> AsyncElasticsearch:
    return es
