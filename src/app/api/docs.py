from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi

import app.main
from app.settings import settings

router = APIRouter()


@router.get("/docs")
async def get_swagger():
    return get_swagger_ui_html(openapi_url=settings.OPENAPI_URL, title="docs")


@router.get("/redoc")
async def get_redoc():
    return get_redoc_html(openapi_url=settings.OPENAPI_URL, title="docs")


@router.get("/openapi.json")
async def get_openapi_json():
    return get_openapi(
        title=app.main.app.title,
        version=app.main.app.version,
        routes=app.main.app.routes,
    )
