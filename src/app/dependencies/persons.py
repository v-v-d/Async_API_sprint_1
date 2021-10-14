from functools import lru_cache

from app.services.persons.main import PersonService

from app.elastic import get_elastic
from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from aioredis import Redis

redis: Redis = None


async def get_redis() -> Redis:
    return redis


@lru_cache()
def get_persons_service(
        redis: Redis = Depends(get_redis),
        elastic: AsyncElasticsearch = Depends(get_elastic),
) -> PersonService:
    return PersonService(elastic, redis)
