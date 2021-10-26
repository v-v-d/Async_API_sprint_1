from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from app.elastic import get_elastic, IndexNameEnum
from app.services.genres.main import GenreService


@lru_cache()
def get_genre_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> GenreService:
    return GenreService(elastic, IndexNameEnum.genres.value)
