from logging import config

from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app import elastic
from app.api.v1 import films, genres, persons
from app.settings import settings
from app.settings.logging import LOGGING

config.dictConfig(LOGGING)


app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    elastic.es = AsyncElasticsearch(
        hosts=[settings.ES.DSN], timeout=settings.ES.TIMEOUT
    )


@app.on_event("shutdown")
async def shutdown():
    await elastic.es.close()


app.include_router(films.router, prefix="/api/v1/films", tags=["films"])
app.include_router(genres.router, prefix="/api/v1/genres", tags=["genres"])
app.include_router(persons.router, prefix="/api/v1/persons", tags=["persons"])
