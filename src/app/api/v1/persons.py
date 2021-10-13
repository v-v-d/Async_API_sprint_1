from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.schemas import OutputPersonSchema, OutputFilmPersonSchema
from app.dependencies.persons import get_persons_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.persons.main import PersonService

router = APIRouter()


@router.get("/search", response_model=list[OutputPersonSchema])
async def persons_search(
    query: str,
    person_service: PersonService = Depends(get_persons_service)
) -> list[OutputPersonSchema]:
    try:
        persons = await person_service.search(query)
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="person not found.")
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
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="person not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return OutputPersonSchema(**person.dict())


@router.get("/{person_id}/film", response_model=list[OutputFilmPersonSchema])
async def search_film_by_person(
        person_id: str,
        person_service: PersonService = Depends(get_persons_service)
) -> list[OutputFilmPersonSchema]:
    try:
        film_person = await person_service.get_all_film_by_person(person_id)
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="film not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputFilmPersonSchema(**film.dict()) for film in film_person]
