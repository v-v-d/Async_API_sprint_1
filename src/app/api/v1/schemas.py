from typing import Optional

from app.services.schemas import ORJSONModel


class ItemSchema(ORJSONModel):
    id: str
    name: str


class FilmFullSchema(ORJSONModel):
    id: str
    rating: Optional[float]
    title: str
    description: str
    genres: list[ItemSchema]
    directors: list[ItemSchema]
    actors: list[ItemSchema]
    writers: list[ItemSchema]
    actors_names: list[str]
    writers_names: list[str]
    directors_names: list[str]