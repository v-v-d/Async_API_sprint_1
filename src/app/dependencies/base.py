from elasticsearch import AsyncElasticsearch

from app.elastic import es


async def get_elastic() -> AsyncElasticsearch:
    return es
