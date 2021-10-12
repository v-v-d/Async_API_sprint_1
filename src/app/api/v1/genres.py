from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.schemas import OutputGenreSchema
from app.dependencies.genres import get_genre_service
from app.services.base import BaseServiceError, NotFoundError
from app.services.genres.main import GenreService

router = APIRouter()


@router.get("/{genre_id}", response_model=OutputGenreSchema)
async def genre_details(
    genre_id: str, genre_service: GenreService = Depends(get_genre_service)
) -> OutputGenreSchema:
    try:
        genre = await genre_service.get_by_id(genre_id)
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="genre not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return OutputGenreSchema(**genre.dict())


@router.get("/", response_model=OutputGenreSchema)
async def search_genres(
        genres_service: GenreService = Depends(get_genre_service)
) -> list[OutputGenreSchema]:
    try:
        genres = await genres_service.search()
    except NotFoundError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="genre not found.")
    except BaseServiceError:
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY, detail="search service error."
        )

    return [OutputGenreSchema(**genre.dict()) for genre in genres]