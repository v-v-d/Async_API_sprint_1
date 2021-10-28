from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from app.elastic import get_elastic, IndexNameEnum
from app.services.films.main import FilmsService


@lru_cache()
def get_film_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> FilmsService:
    return FilmsService(elastic, IndexNameEnum.movies.value)
