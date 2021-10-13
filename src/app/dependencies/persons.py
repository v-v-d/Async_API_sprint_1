from functools import lru_cache

from app.services.persons.main import PersonService

from app.elastic import get_elastic
from elasticsearch import AsyncElasticsearch
from fastapi import Depends


@lru_cache()
def get_persons_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> PersonService:
    return PersonService(elastic)
