from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.schemas import FilmFullSchema
from app.dependencies.films import get_film_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.films.main import FilmsService

router = APIRouter()


@router.get("/{film_id}", response_model=FilmFullSchema)
async def film_details(
    film_id: str, film_service: FilmsService = Depends(get_film_service)
) -> FilmFullSchema:
    try:
        film = await film_service.get_by_id(film_id)
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="film not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return FilmFullSchema(**film.dict())
