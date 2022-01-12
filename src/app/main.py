from logging import config

from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import ORJSONResponse

from app import elastic
from app.api import api_root
from app.api.docs import router as api_docs
from app.apm import init_apm
from app.settings import settings
from app.settings.logging import LOGGING

config.dictConfig(LOGGING)


app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    default_response_class=ORJSONResponse,
)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)


@app.on_event("startup")
async def startup():
    elastic.es = AsyncElasticsearch(
        hosts=[settings.ES.DSN], timeout=settings.ES.TIMEOUT
    )


@app.on_event("shutdown")
async def shutdown():
    await elastic.es.close()


app.include_router(api_docs)
app.include_router(api_root, prefix="/api")

init_apm(app)
