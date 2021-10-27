from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.schemas import OutputFilmSchema, OutputPersonSchema
from app.dependencies.api import DefaultParamsSchema, get_default_query_params
from app.dependencies.films import get_film_service
from app.dependencies.persons import get_persons_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.films.main import FilmsService
from app.services.persons.main import PersonService

router = APIRouter()


@router.get("/films", response_model=list[OutputFilmSchema])
async def films_search(
    query: str,
    default: DefaultParamsSchema = Depends(get_default_query_params),
    film_service: FilmsService = Depends(get_film_service),
) -> list[OutputFilmSchema]:
    try:
        films = await film_service.search_by_query(
            default.page, default.size, query=query
        )
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputFilmSchema(**film.dict()) for film in films]


@router.get("/persons", response_model=list[OutputPersonSchema])
async def persons_search(
    query: str,
    default: DefaultParamsSchema = Depends(get_default_query_params),
    person_service: PersonService = Depends(get_persons_service),
) -> list[OutputPersonSchema]:
    try:
        persons = await person_service.search(default.page, default.size, query=query)
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputPersonSchema(**person.dict()) for person in persons]
