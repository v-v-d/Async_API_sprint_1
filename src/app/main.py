from logging import config

from app.api.v1 import films, genres, persons
from elasticsearch import AsyncElasticsearch

from app import elastic
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

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
    elastic.es = AsyncElasticsearch(hosts=[settings.ES.DSN], timeout=settings.ES.TIMEOUT)


@app.on_event("shutdown")
async def shutdown():
    await elastic.es.close()


app.include_router(films.router, prefix='/api/v1/film', tags=['film'])
app.include_router(genres.router, prefix='/api/v1/genre', tags=['genre'])
app.include_router(persons.router, prefix='/api/v1/person', tags=['person'])
app.include_router(persons.router, prefix='/api/v1/person', tags=['person'])
app.include_router(persons.router, prefix='/api/v1/person', tags=['person'])

