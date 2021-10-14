from enum import Enum
from typing import Optional

from elasticsearch import AsyncElasticsearch


class IndexNameEnum(str, Enum):
    movies = "movies"
    persons = "persons"
    genres = "genres"


es: Optional[AsyncElasticsearch]

async def get_elastic() -> AsyncElasticsearch:
    return es
