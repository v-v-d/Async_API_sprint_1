from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.schemas import OutputPersonSchema
from app.dependencies.persons import get_persons_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.persons.main import PersonService

router = APIRouter()


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


@router.get("/", response_model=OutputPersonSchema)
async def person_details(
    person_service: PersonService = Depends(get_persons_service)
) -> OutputPersonSchema:
    try:
        person = await person_service.get_all_id()
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="person not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return OutputPersonSchema(**person.dict())


@router.get("/search/{person_name}", response_model=OutputPersonSchema)
async def person_details(
    person_name: str, person_service: PersonService = Depends(get_persons_service)
) -> OutputPersonSchema:
    try:
        persons = await person_service.get_name_person(person_name)

    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="person not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputPersonSchema(**person.dict()) for person in persons]





