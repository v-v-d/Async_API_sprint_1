from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.v1.schemas import (
    OutputPersonSchema,
    OutputFilmSchema,
)
from app.dependencies.api import DefaultParamsSchema, get_default_query_params
from app.dependencies.films import get_film_service
from app.dependencies.persons import get_persons_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.films.main import FilmsService
from app.services.persons.main import PersonService

router = APIRouter()


@router.get("/search", response_model=list[OutputPersonSchema])
async def persons_search(
    query: str,
    default: DefaultParamsSchema = Depends(get_default_query_params),
    person_service: PersonService = Depends(get_persons_service),
) -> list[OutputPersonSchema]:
    try:
        persons = await person_service.search(default.page, default.size, query=query)
    except NotFoundError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="person not found."
        )
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputPersonSchema(**person.dict()) for person in persons]


@router.get("/{person_id}", response_model=OutputPersonSchema)
async def person_details(
    person_id: str, person_service: PersonService = Depends(get_persons_service)
) -> OutputPersonSchema:
    try:
        person = await person_service.get_by_id(person_id)
    except NotFoundError:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="person not found."
        )
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return OutputPersonSchema(**person.dict())


@router.get("/{person_id}/films", response_model=list[OutputFilmSchema])
async def films_by_person_search(
    person_id: str,
    sort: Optional[str] = Query(None),
    default: DefaultParamsSchema = Depends(get_default_query_params),
    film_service: FilmsService = Depends(get_film_service),
) -> list[OutputFilmSchema]:
    try:
        films = await film_service.get_all(
            default.page,
            default.size,
            person_id=person_id,
            sort=sort,
        )
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputFilmSchema(**film.dict()) for film in films]
