from fastapi import APIRouter, Depends, status

from app.api import v1
from app.api.schemas import ErrorSchema
from app.dependencies.auth import decode_jwt

api_root = APIRouter(
    responses={
        status.HTTP_424_FAILED_DEPENDENCY: {"model": ErrorSchema},
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorSchema},
    },
    dependencies=[Depends(decode_jwt)],
)

api_root.include_router(v1.search.router, prefix="/v1/search", tags=["v1 search"])
api_root.include_router(v1.films.router, prefix="/v1/films", tags=["v1 films"])
api_root.include_router(v1.genres.router, prefix="/v1/genres", tags=["v1 genres"])
api_root.include_router(v1.persons.router, prefix="/v1/persons", tags=["v1 persons"])
