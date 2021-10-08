from http import HTTPStatus

from app.services.films.exceptions import BaseFilmsServiceError

from app.dependencies.films import get_film_service

from app.services.films.main import FilmsService
from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.schemas import FilmSchema

router = APIRouter()


@router.get("/{film_id}", response_model=FilmSchema)
async def film_details(
    film_id: str, 
    film_service: FilmsService = Depends(get_film_service)
) -> FilmSchema:
    try:
        film = await film_service.get_by_id(film_id)
    except BaseFilmsServiceError:
        raise HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail="service unavailable"
        )

    if not film:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="film not found"
        )

    return FilmSchema(id=film.id, title=film.title)
