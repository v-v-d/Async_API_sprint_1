from functools import lru_cache

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from app.elastic import get_elastic, IndexNameEnum
from app.services.persons.main import PersonService


@lru_cache()
def get_persons_service(
    elastic: AsyncElasticsearch = Depends(get_elastic),
) -> PersonService:
    return PersonService(elastic, IndexNameEnum.persons.value)
