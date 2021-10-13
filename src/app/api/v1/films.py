from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.v1.schemas import OutputFilmSchema
from app.dependencies.api import DefaultParamsSchema, get_default_query_params
from app.dependencies.films import get_film_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.films.main import FilmsService

router = APIRouter()


@router.get("/search", response_model=list[OutputFilmSchema])
async def films_search(
    query: str,
    default: DefaultParamsSchema = Depends(get_default_query_params),
    film_service: FilmsService = Depends(get_film_service),
) -> list[OutputFilmSchema]:
    try:
        films = await film_service.search(default.page, default.size, query=query)
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputFilmSchema(**film.dict()) for film in films]


@router.get("/", response_model=list[OutputFilmSchema])
async def films_list(
    genre_id: Optional[str] = Query(None),
    person_id: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
    default: DefaultParamsSchema = Depends(get_default_query_params),
    film_service: FilmsService = Depends(get_film_service),
) -> list[OutputFilmSchema]:
    try:
        films = await film_service.search(
            default.page,
            default.size,
            genre_id=genre_id,
            person_id=person_id,
            sort=sort,
        )
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="film not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputFilmSchema(**film.dict()) for film in films]


@router.get("/{film_id}", response_model=OutputFilmSchema)
async def film_details(
    film_id: str, film_service: FilmsService = Depends(get_film_service)
) -> OutputFilmSchema:
    try:
        film = await film_service.get_by_id(film_id)
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="film not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return OutputFilmSchema(**film.dict())
