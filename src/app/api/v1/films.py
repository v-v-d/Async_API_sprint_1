from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.v1.schemas import OutputFilmSchema
from app.dependencies.api import DefaultParamsSchema, get_default_query_params
from app.dependencies.auth import check_for_subscription
from app.dependencies.films import get_film_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.films.main import FilmsService, FilmSubscriptionError

router = APIRouter()


@router.get("/", response_model=list[OutputFilmSchema])
async def films_list(
    genre_id: Optional[str] = Query(None),
    person_id: Optional[str] = Query(None),
    sort: Optional[str] = Query(None, regex="-rating|rating"),
    default: DefaultParamsSchema = Depends(get_default_query_params),
    film_service: FilmsService = Depends(get_film_service),
    is_subscriber: bool = Depends(check_for_subscription),
) -> list[OutputFilmSchema]:
    try:
        films = await film_service.get_all(
            default.page,
            default.size,
            genre_id=genre_id,
            person_id=person_id,
            sort=sort,
            is_subscriber=is_subscriber,
        )
    except BaseServiceError:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail="search service error.",
        )

    return [OutputFilmSchema(**film.dict()) for film in films]


@router.get("/{film_id}", response_model=OutputFilmSchema)
async def film_details(
    film_id: str,
    film_service: FilmsService = Depends(get_film_service),
    is_subscriber: bool = Depends(check_for_subscription),
) -> OutputFilmSchema:
    try:
        film = await film_service.get_by_id(film_id, is_subscriber)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="film not found."
        )
    except BaseServiceError:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail="search service error.",
        )
    except FilmSubscriptionError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="only for subscribers."
        )

    return OutputFilmSchema(**film.dict())
