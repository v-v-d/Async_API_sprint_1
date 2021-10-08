from functools import lru_cache

from app.services.films.main import FilmsService

from app.elastic import get_elastic
from elasticsearch import AsyncElasticsearch
from fastapi import Depends


@lru_cache()
def get_film_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> FilmsService:
    return FilmsService(elastic)
