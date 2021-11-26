from typing import Optional

from app.services.schemas import ORJSONModel, BaseListRootModel


class InputItemSchema(ORJSONModel):
    id: str
    name: str


class InputFilmSchema(ORJSONModel):
    id: str
    rating: Optional[float]
    title: str
    description: str
    genres: list[InputItemSchema]
    directors: list[InputItemSchema]
    actors: list[InputItemSchema]
    writers: list[InputItemSchema]
    actors_names: list[str]
    writers_names: list[str]
    directors_names: list[str]
    subscription_required: bool


class InputListFilmSchema(BaseListRootModel):
    __root__: list[InputFilmSchema]
