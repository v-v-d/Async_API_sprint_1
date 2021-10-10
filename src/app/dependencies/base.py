from app.elastic import es
from elasticsearch import AsyncElasticsearch


async def get_elastic() -> AsyncElasticsearch:
    return es
