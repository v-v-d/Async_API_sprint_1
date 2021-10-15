from functools import lru_cache

from app.services.genres.main import GenreService

from app.elastic import get_elastic
from elasticsearch import AsyncElasticsearch
from fastapi import Depends


@lru_cache()
def get_genre_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> GenreService:
    return GenreService(elastic)
